$(document).ready(function () {
    if (typeof proj4 != 'undefined') {
        proj4.defs("EPSG:31370","+proj=lcc +lat_1=51.16666723333333 +lat_2=49.8333339 +lat_0=90 +lon_0=4.367486666666666 +x_0=150000.013 +y_0=5400088.438 +ellps=intl +towgs84=-106.869,52.2978,-103.724,0.3366,-0.457,1.8422,-1.2747 +units=m +no_defs");

    } else {
        console.log("pas de proj");
    }
    var belgiumProjection = new ol.proj.Projection({
      code: 'EPSG:31370',
      // The extent is used to determine zoom level 0. Recommended values for a
      // projection's validity extent can be found at https://epsg.io/.
      extent: [0, 0, 300000, 300000],
      units: 'm'
    });
    ol.proj.addProjection(belgiumProjection);
});
