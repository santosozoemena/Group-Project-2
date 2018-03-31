var url = "https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9.html?fresh=true&title=true&access_token=pk.eyJ1Ijoic2FudG9zb3pvZW1lbmEiLCJhIjoiY2plbHE0dXNnM2thMDMzbzdyZGFza2U5cCJ9.kcNpr7mekfrSVH6dF2WzPA#0.0/0.000000/0.000000/0"
var map = L.map("map",{
  center:[23.8859, 45.0792],
  zoom: 2
});

L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoic2FudG9zb3pvZW1lbmEiLCJhIjoiY2plbHE0dXNnM2thMDMzbzdyZGFza2U5cCJ9.kcNpr7mekfrSVH6dF2WzPA").addTo(map)
function marker(){

}

d3.csv('excess/2018top1.csv', function(data){
    data.forEach(function(d){
      d.lat = +d.lat
      d.lng = +d.lng
      var marker = L.marker([d.lat , d.lng], {
       draggable: true,
       title: "My First Marker",
       color: "green"

      }).addTo(map);

      marker.bindPopup('<b>' + d.Countrys + '</b>' + '<br>' + 'Artist: '+ d.Artist + '<br>' + ' Track Name: '  + '<a href=' + d.URL + '>' +d['Track Name'] + '</a>');
    
    });
});



var scatterPolar_server = "/scatter_polar";

function initiate_scatter(){
    Plotly.d3.json(scatterPolar_server, function(error, response){
        if(error) return console.warn(error);
        var data = response;
        var layout = 
        {
            showlegend: true,
            polar: 
            {
                domain: {
                    x: [0, 0.46],
                    y: [0.56, 1]
                },
                radialaxis: {
                    angle: 360
                },
                angularaxis: {
                    direction: "clockwise",
                    period: 1
                }
            },
            height:1500,
            width:1500,   
        }
    Plotly.newPlot('scatterPolar',data,layout)
    })
}

initiate_scatter();