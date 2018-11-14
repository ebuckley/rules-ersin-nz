import json

from .db import get_db
from . import geometry
from flask import (
    Blueprint, request, url_for,
    render_template, redirect)
import requests

bp = Blueprint('rules', __name__, url_prefix='/rules')


@bp.route('/', methods=('GET',))
def view_index():
    sql = """   
        SELECT ST_AsGeoJSON(zones.wkb_geometry) as geometry, rules.id as rule_id, rules.rule_uri, zones.zone_description, zones.ogc_fid zone_id
        FROM rules
        JOIN district_plan_zones zones on rules.zone_id = zones.ogc_fid
        LIMIT 20;
        """
    db = get_db()
    result = db.query(sql)
    return render_template('rules/index.html', data=result)


@bp.route('/view')
def rules_view():
    location = request.args.get('property_location', None).split(',')
    if not location:
        raise Exception("Could not look up rules because no location was specified")

    point = geometry.get_point(location[0], location[1])
    sql = """
        SELECT ST_AsGeoJSON(zones.wkb_geometry) as geometry, rules.id as rule_id, rules.rule_uri, zones.zone_description, zones.ogc_fid zone_id
        FROM rules
        JOIN district_plan_zones zones on rules.zone_id = zones.ogc_fid
        WHERE zones.ogc_fid=:point_id
        """
    db = get_db()
    result = db.query(sql, point_id=point.ogc_fid)
    return render_template('rules/view.html', geometry=point.geometry, data=result)

@bp.route('/new', methods=('GET', 'POST'))
def new_rule():
    if request.method == 'GET':
        return render_template('rules/new.html')
    else:
        href = request.form['rule_uri']
        geom = request.form['geometry'].split(',')
        location = geometry.get_point(geom[0], geom[1])

        sql = """
            INSERT INTO rules (zone_id, rule_uri)
            VALUES (:zone_id, :rule_uri);
        """
        db = get_db()
        db.query(sql, zone_id=location.ogc_fid, rule_uri=href)
        return redirect(url_for('rules.view_index'))

@bp.route('/evaluate', methods=('POST', ))
def evaluate():
    situation_json = json.loads(request.form['situation'])
    zone_id = int(request.form['zone_id'])
    sql = """
            SELECT ST_AsGeoJSON(zones.wkb_geometry) as geometry, rules.id as rule_id, rules.rule_uri, zones.zone_description, zones.ogc_fid zone_id
            FROM rules
            JOIN district_plan_zones zones on rules.zone_id = zones.ogc_fid
            WHERE zones.ogc_fid=:point_id
            """
    db = get_db()
    result = db.query(sql, point_id=zone_id)
    for row in result:
        r = requests.get(row.rule_uri)
        if r.status_code != 200:
            raise Exception("expected to get the row uri")
        body = r.json()
        variable = body['id']
        return json.dumps(body)