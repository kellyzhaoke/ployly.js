function buildPlot() {
    /* data route */
    var url = "/pie";
    Plotly.d3.json(url, function(error, response) {

        console.log(response);

        var data = [response]

        var layout = {
            title: "Belly Button",
            
            }
        };

        Plotly.newPlot("plot", data, layout);
    });
}

buildPlot();
