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