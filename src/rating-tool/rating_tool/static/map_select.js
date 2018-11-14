const mymap = L.map('mapid').setView([ -43.55072467468882, 172.69602298736572], 15);
let marker = null;


L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.{ext}', {
	attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
	subdomains: 'abcd',
	minZoom: 0,
	maxZoom: 20,
	ext: 'png'
}).addTo(mymap);

mymap.on('click', onMapClick)


function onMapClick(e) {
    console.log('cloicked it at', e)
    console.log('zoom', mymap.getZoom(), 'bounds', mymap.getBounds(), mymap.getBounds().toBBoxString())
    if (!marker) {
        marker = L.marker(e.latlng)
        marker.addTo(mymap)
    } else {
        marker.setLatLng(e.latlng)
    }
    document.querySelector('#form-property-location').value = `${e.latlng.lng}, ${e.latlng.lat}`;

    // const bbox = mymap.getBounds().toBBoxString();
    // if (mymap.getZoom() >= 15) {
    //     fetch(`/g/district_zone_layer?bbox=${bbox}`)
    //         .then(result => result.json())
    //         .then(data => {
    //             console.log('got district zone data', data)
    //             L.geoJSON(data).addTo(mymap)
    //         })
    //         .catch( e => {
    //             console.error("Failed to fetch district zone data", e)
    //         })
    //
    // }
}