/****** TEST ******/
console.log("plotlyplot.js link Works!!!!!!!!!!!")

//##########################################################
//Post, get values to and from app.py and render sliderplot 
//##########################################################

function buildPlot() {
    Plotly.d3.json("/plotlyData", function(error, response) {
        if (error) return console.warn(error);
        console.log(response);
      // Grab values from the response json object to build the plots
      var year = response.Alameda.year;
      var households = response.Alameda.Households;
      var income = response.Alameda.Income;
      var jobs = response.Alameda.Jobs;
      var medianHomePrice = response.Alameda["Median Home Price"];
      console.log(year, households, income, jobs, medianHomePrice);
      
      function init() {
        var trace1 = {
            type: "scatter",
            mode: "lines",
            name: name,
            x: year,
            y: households,
            line: {
            color: "#17BECF"
            }
        };

        var trace2 = {
            type: "scatter",
            mode: "lines",
            name: name,
            x: year,
            y: income,
            line: {
            color: "red"
            }
        };

        var trace3 = {
            type: "scatter",
            mode: "lines",
            name: name,
            x: year,
            y: jobs,
            line: {
            color: "blue"
            }
        };

        var trace4 = {
            type: "scatter",
            label: "medianHomePrice",
            mode: "lines",
            name: name,
            x: year,
            y: medianHomePrice,
            line: {
            color: "black"
            }
        };
    
        var data = [trace1, trace2, trace3, trace4];
    
        //   var layout = {
        //     title: `${stock} closing prices`,
        //     xaxis: {
        //       range: [startDate, endDate],
        //       type: "date"
        //     },
        //     yaxis: {
        //       autorange: true,
        //       type: "linear"
        //     }
        //   };
    
        Plotly.newPlot("plotlyPlot", data); //layout);
        }

    // function updatePlotly(newdata) {
    //     var LINE = document.getElementById("plotlyPlot");
    //     Plotly.restyle(LINE, "y", [newdata]);
    //     }

    // function getData(dataset) {
    //     var data = [];
    //     switch (dataset) {
    //     case "dataset1":
    //         data = [1, 2, 3, 39];
    //         break;
    //     case "dataset2":
    //         data = [10, 20, 30, 37];
    //         break;
    //     case "dataset3":
    //         data = [100, 200, 300, 23];
    //         break;
    //     default:
    //         data = [30, 30, 30, 11];
    //     }
    //     updatePlotly(data);
    //     }

    init();
    });
}
  


  
// buildPlot();