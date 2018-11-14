import json

from .db import get_db
from flask import (
    Blueprint, request, Response,
    render_template)

bp = Blueprint('geometry', __name__, url_prefix='/g')

def row_to_feature(row):
    properties = row.as_dict()
    geometry = json.loads(row.get('geometry'))
    del properties['geometry']
    return {
        'type': 'Feature',
        'properties': properties,
        'geometry': geometry,
    }
def rows_to_feature_collection(rows):
    features = map(row_to_feature, rows)
    feature_collection = {
        'type': 'FeatureCollection',
        'features': features
    }
    return Response(json.dumps(feature_collection), mimetype='application/json')

def get_point(lng, lat):
    sql = """
            select ST_AsGeoJSON(wkb_geometry) as geometry, ogc_fid, description, zone_code, id, link, source, zone_description, zone_type
            from district_plan_zones
            WHERE ST_INTERSECTS(ST_SetSRID(ST_MakePoint(:lng,:lat), 4326),
                   wkb_geometry)
            """
    db = get_db()
    return db.query(sql, lng=lng, lat=lat)[0]


@bp.route('/district_zone_layer', methods=('GET',))
def get_geom():
    db = get_db()
    bbox = request.args.get('bbox', None)
    if not bbox:
        # TODO actually we should throw an exception here...
        raise Exception('Please supply a bbox argument')

    sql = """
    select ST_AsGeoJSON(wkb_geometry) as geometry, ogc_fid, description, zone_code, id, link, source, zone_description, zone_type
    from district_plan_zones
    WHERE ST_INTERSECTS(ST_MakeEnvelope(:nw,:ne,:sw,:se, 4326),
           wkb_geometry)
    """
    bbox = [float(v) for v in bbox.split(',')]
    result = db.query(sql, nw=bbox[0], ne=bbox[1], sw=bbox[2], se=bbox[3])

    return rows_to_feature_collection(result)

@bp.route('/', methods=('GET',))
def view_map():
    return render_template('map.html')


@bp.route('/rules')
def rules_view():
    location = request.args.get('property_location', None).split(',')
    property_cv = request.args.get('property_cv', None)
    if not location:
        raise Exception("Could not look up rules because no location was specified")

    loc = get_point(location[0], location[1])

    return render_template('rules.html')