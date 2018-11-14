const submap = document.querySelectorAll('.view-map')

submap.forEach(el => {
    const geojson = JSON.parse(el.getAttribute('data-map'))
    console.log('attr', geojson)
    const map = L.map(el)
    const geoLayer = L.geoJSON(geojson);
    L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.{ext}', {
        subdomains: 'abcd',
        minZoom: 0,
        maxZoom: 20,
        ext: 'png'
    }).addTo(map);
    geoLayer.addTo(map)
    map.fitBounds(geoLayer.getBounds());
})