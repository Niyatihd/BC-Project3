/****** TEST ******/
console.log("app.js link Works!!!!!!!!!!!")

//##########################################################
//Post, get values to and from app.py and render sliderplot 
//##########################################################

var bayareaData = {'Bay Area': {'household': [0.0087934836,
                                                0.0089488675,
                                                0.0075442035,
                                                0.007663956800000001,
                                                0.0073744557,
                                                0.0069410449,
                                                0.010347578500000001,
                                                0.0112222659,
                                                0.0834517088,
                                                -0.0583628022,
                                                0.0066970986000000005,
                                                0.006975574500000001,
                                                0.0055656825,
                                                0.0068928694,
                                                0.0068378212,
                                                0.0059839912,
                                                0.0060574519,
                                                0.0034575887,
                                                0.0020228876,
                                                0.0056658485,
                                                0.0056285865,
                                                0.0043133274,
                                                0.0061211323,
                                                0.0092656868,
                                                0.0075978203000000005],
                                'income': [0.0651705198,
                                                0.0208659614,
                                                0.027893059100000003,
                                                0.0387347493,
                                                0.040309736000000006,
                                                0.0687720898,
                                                0.0569008555,
                                                0.0889562414,
                                                0.1455935045,
                                                -0.009706628200000001,
                                                -0.0114544623,
                                                0.0320932264,
                                                0.0556882556,
                                                0.044239905,
                                                0.0447980508,
                                                0.051824144700000005,
                                                0.007701561700000001,
                                                0.0058753966,
                                                0.025853524000000003,
                                                0.0351167471,
                                                0.0637450059,
                                                0.013708707700000001,
                                                0.0328507179,
                                                0.046420913800000005,
                                                0.0347413444],
                                            'jobs': [-0.0185976184,
                                                -0.0028206376,
                                                0.0072571627,
                                                0.0219497538,
                                                0.0385791786,
                                                0.0337791153,
                                                0.0380313958,
                                                0.0266293075,
                                                0.0453730558,
                                                -0.0170548172,
                                                -0.0494328242,
                                                -0.03001347,
                                                -0.0065945147,
                                                0.006907093400000001,
                                                0.0191594044,
                                                0.0146750435,
                                                0.0048073943,
                                                -0.0568315203,
                                                -0.0115019527,
                                                0.0168262684,
                                                0.0372867876,
                                                0.0369053445,
                                                0.0354417525,
                                                0.0398833435,
                                                0.0306605723],
                                            'medianHomePrice': [-0.0009948889,
                                                -0.0070267221000000005,
                                                0.028335916000000003,
                                                0.0017245493,
                                                0.0328771703,
                                                0.0879308043,
                                                0.1180582929,
                                                0.153612314,
                                                0.2509369991,
                                                0.0599414598,
                                                0.07070480850000001,
                                                0.0831250063,
                                                0.166516358,
                                                0.1017506807,
                                                0.0286740495,
                                                0.0461142674,
                                                -0.30268398690000003,
                                                -0.2359729686,
                                                0.14275245050000002,
                                                -0.0780693316,
                                                0.1228999005,
                                                0.3061396565,
                                                0.1148820895,
                                                0.0790766926,
                                                0.0742961333],
                                            'year': [1992,
                                                1993,
                                                1994,
                                                1995,
                                                1996,
                                                1997,
                                                1998,
                                                1999,
                                                2000,
                                                2001,
                                                2002,
                                                2003,
                                                2004,
                                                2005,
                                                2006,
                                                2007,
                                                2008,
                                                2009,
                                                2010,
                                                2011,
                                                2012,
                                                2013,
                                                2014,
                                                2015,
                                                2016]}};


function buildPlot() {
    // Plotly.d3.json("/plotlyData", function(error, response) {
    //     if (error) return console.warn(error);
    //     console.log(response);
        // Grab values from the response json object to build the plots
        var year = bayareaData['Bay Area'].year;
        var households = bayareaData['Bay Area'].household;
        var income = bayareaData['Bay Area'].income;
        var jobs = bayareaData['Bay Area'].jobs;
        var medianHomePrice = bayareaData['Bay Area'].medianHomePrice;
        // console.log(year, households, income, jobs, medianHomePrice);
        console.log("Initial plot done!!")
    //   function init() {
        var trace1 = {
            type: "scatter",
            mode: "lines",
            name: "Households",
            x: year,
            y: households.map(function(element) {return element * 100;}),
            line: {
            color: "#17BECF"
            }
        };

        var trace2 = {
            type: "scatter",
            mode: "lines",
            name: "Income",
            x: year,
            y: income.map(function(element) {return element * 100;}),
            line: {
            color: "red"
            }
        };

        var trace3 = {
            type: "scatter",
            mode: "lines",
            name: "Jobs",
            x: year,
            y: jobs.map(function(element) {return element * 100;}),
            line: {
            color: "blue"
            }
        };

        var trace4 = {
            type: "scatter",
            label: "medianHomePrice",
            mode: "lines",
            name: "Median Home Price",
            x: year,
            y: medianHomePrice.map(function(element) {return element * 100;}),
            line: {
            color: "black"
            }
        };
    
        var data = [trace1, trace2, trace3, trace4];
    
        var layout = {
        title: `% Change in Predictor Variables : Bay Area`,
        xaxis: {
           // title: "Year",
            type: "date"
        },
        yaxis: {
            //title: "Percentage Change(%)",
            autorange: true,
            type: "linear"
        },
        showlegend: true,
        legend: {"orientation": "h"}
        };
    
        Plotly.newPlot("plotlyPlot", data, layout);
    }

    function updatePlotly(newdata) {
        console.log(newdata);
        var LINE = document.getElementById("plotlyPlot");
        var layout = {
            title: `% Change in Predictor Variables`,
            xaxis: {
                //title: "Year",
                type: "date"
            },
            yaxis: {
               // title: "Percentage Change(%)",
                autorange: true,
                type: "linear"
            },
            showlegend: true,
            legend: {"orientation": "h"}
            };
        Plotly.newPlot(LINE, newdata, layout);
    }

    // function updatePlotlyPlot2(newdata) {
    //     console.log(newdata);
    //     var LINE = document.getElementById("plotlyPlot");
    //     var layout = {
    //         title: `Affordability Gap`,
    //         xaxis: {
    //             //title: "Year",
    //             type: "date"
    //         },
    //         yaxis: {
    //            // title: "Percentage Change(%)",
    //             autorange: true,
    //             type: "linear"
    //         },
    //         showlegend: true,
    //         legend: {"orientation": "h"}
    //         };
    //     Plotly.newPlot(LINE, newdata, layout);
    // }

buildPlot();               



function updatePlot(ddl1) {
    var userSel = ddl1;
    // console.log("creating historical plot with prediction");
    console.log(ddl1);
    var selectedArea = (ddl1 === "Select Area")?"":ddl1;
    // console.log(selectedArea);
    var selectedAreaObj = {areaselected: selectedArea};
    console.log(selectedAreaObj); 
    // console.log(JSON.stringify(selectedAreaObj)); 

    fetch('/predictFuture', {
        body: JSON.stringify(selectedAreaObj), // must match 'Content-Type' header
        headers: {
          'content-type': 'application/json'
        },
        method: 'POST', 
    })
    .then((response) => {
        // console.log(response.json());
        return response.json();
    })
    .then((data) => {
        console.log(data);
        return data;
    })
    .then((data) => {
    
    //var empCoeff = data.employees_wt;
    //console.log("empCoeff is: " + empCoeff);
    //var householdCoeff = data.household_wt;
    //var wageCoeff = data.wage_wt;

    //You are getting a table 

    // Set variable for the prediction button
    var buttonClick = document.querySelector("#viewAffordability");

    // Add click even listener to the prediction button
    buttonClick.addEventListener("click", function() {

        var predictionTable= document.querySelector('tbody');

        //textclean= data.replace(/"/g,' ');
        //textclean2 = textclean.replace(/\\n/g,'');
        //predictionTable.innerHTML = textclean2;;
        //predictionTable.innerHTML = data;
        for (var i = 0; i < data.length; i++) {

            // Insert a row into the table at position i
            var $row = $predictionTable.insertRow(i);
            // Insert cells into the newly created row
            var rowEntry = Object.values(data[i]);
            console.log(rowEntry);
          //console.log(rowEntry.length);
          for (var j = 0; j < rowEntry.length; j++) {
    
              var $cell = $row.insertCell(j);
              
              $cell.innerText = rowEntry[j]; 
            } 
          }



        console.log(data)

        Plotly.d3.json("/plot2Data", function(error, response) {
            if (error) return console.warn(error);
            console.log("for plot2 = " + response[userSel].avgAnnualIncome);
          // Grab values from the response json object to build the plots
          var year = response[userSel].year;
          var qualifyingIncome = response[userSel].qualifyingIncome;
          var avgAnnualIncome = response[userSel].avgAnnualIncome;
          var medianHomePrice = response[userSel].medianHomePrice;
        //   console.log(userSel, year, qualifyingIncome, avgAnnualIncome, medianHomePrice);
            console.log("Values for plot2 check!");
            var trace1 = {
                type: "scatter",
                mode: "lines",
                name: "Qualifying Income",
                x: year,
                y: qualifyingIncome,
                line: {
                color: "#17BECF"
                }
            };
    
            var trace2 = {
                type: "scatter",
                mode: "lines",
                name: "Avg. Annual Income",
                x: year,
                y: avgAnnualIncome,
                line: {
                color: "red"
                }
            };
    
            var trace3 = {
                type: "scatter",
                mode: "lines",
                name: "Median Home Price",
                x: year,
                y: medianHomePrice,
                line: {
                color: "blue"
                }
            };

            var data = [trace1, trace2, trace3];
    
            var layout = {
            title: `Affordability Gap`,
            xaxis: {
               // title: "Year",
                type: "date"
            },
            yaxis: {
                //title: "Percentage Change(%)",
                autorange: true,
                type: "linear"
            },
            showlegend: true,
            legend: {"orientation": "h" },
            };
        
            Plotly.newPlot("plotlyPlot", data, layout);
            
        });

    });

    //-------------------------------------------------------------------------------------------
    //  // Set variable for the affordability button
    //  var buttonClick = document.querySelector("#viewAffordability");

    //  // Add click even listener to the affordability button
    //  buttonClick.addEventListener("click", function() {
 
    //      Plotly.d3.json("/plot2Data", function(error, response) {
    //          if (error) return console.warn(error);
    //          console.log("for plot2 = " + response[userSel].avgAnnualIncome);
    //        // Grab values from the response json object to build the plots
    //        var year = response[userSel].year;
    //        var qualifyingIncome = response[userSel].qualifyingIncome;
    //        var avgAnnualIncome = response[userSel].avgAnnualIncome;
    //        var medianHomePrice = response[userSel].medianHomePrice;
    //      //   console.log(userSel, year, qualifyingIncome, avgAnnualIncome, medianHomePrice);
    //          console.log("Values for plot2 check!");
    //          var trace1 = {
    //              type: "scatter",
    //              mode: "lines",
    //              name: "Qualifying Income",
    //              x: year,
    //              y: qualifyingIncome,
    //              line: {
    //              color: "#17BECF"
    //              }
    //          };
     
    //          var trace2 = {
    //              type: "scatter",
    //              mode: "lines",
    //              name: "Avg. Annual Income",
    //              x: year,
    //              y: avgAnnualIncome,
    //              line: {
    //              color: "red"
    //              }
    //          };
     
    //          var trace3 = {
    //              type: "scatter",
    //              mode: "lines",
    //              name: "Median Home Price",
    //              x: year,
    //              y: medianHomePrice,
    //              line: {
    //              color: "blue"
    //              }
    //          };
 
    //          var data = [trace1, trace2, trace3];
     
    //          var layout = {
    //          title: `Affordability Gap`,
    //          xaxis: {
    //             // title: "Year",
    //              type: "date"
    //          },
    //          yaxis: {
    //              //title: "Percentage Change(%)",
    //              autorange: true,
    //              type: "linear"
    //          },
    //          showlegend: true,
    //          legend: {"orientation": "h"}
    //          };
         
    //          Plotly.newPlot("plotlyPlot", data, layout);
             
    //      });
 
    //  });
    //-------------------------------------------------------------------------------------------


    // function rePlotPlotly() {
        Plotly.d3.json("/plotlyData", function(error, response) {
            if (error) return console.warn(error);
            // console.log(response);
          // Grab values from the response json object to build the plots
          var year = response[userSel].year;
          var households = response[userSel].household;
          var income = response[userSel].income;
          var jobs = response[userSel].jobs;
          var medianHomePrice = response[userSel].medianHomePrice;
        //   console.log(userSel, year, households, income, jobs, medianHomePrice);
        console.log(userSel + "for plot1");

        //   function init() {
            var trace1 = {
                type: "scatter",
                mode: "lines",
                name: "Households",
                x: year,
                y: households.map(function(element) {return element * 100;}),
                line: {
                color: "#17BECF"
                }
            };
    
            var trace2 = {
                type: "scatter",
                mode: "lines",
                name: "Income",
                x: year,
                y: income.map(function(element) {return element * 100;}),
                line: {
                color: "red"
                }
            };
    
            var trace3 = {
                type: "scatter",
                mode: "lines",
                name: "Jobs",
                x: year,
                y: jobs.map(function(element) {return element * 100;}),
                line: {
                color: "blue"
                }
            };
    
            var trace4 = {
                type: "scatter",
                label: "medianHomePrice",
                mode: "lines",
                name: "Median Home Price",
                x: year,
                y: medianHomePrice.map(function(element) {return element * 100;}),
                line: {
                color: "black"
                }
            };
        
            var data1 = [trace1, trace2, trace3, trace4];
            console.log("data1 : " + data1);
            updatePlotly(data1);
        
        });
    // }
    // rePlotPlotly();
});
}


var images = [
    "../static/images/carousel/1968-2010_US-CA-SF_Median_Price.jpg",
    "../static/images/carousel/Affordability_Bay-Area-Counties_Chart.jpg",
    "../static/images/carousel/BayAreaReakEstateMarketCycles.jpg",
    "../static/images/carousel/Case-Shiller_HT_1996-2011.jpg",
    "../static/images/carousel/Case-Shiller_HT_from_1988_V2-bar-chart.jpg",
    "../static/images/carousel/National-Housing-Affordability-Index_NAR_by-MSA.jpg",
    "../static/images/carousel/titleimage3.jpg",
  ];
  
  var imageHead = document.getElementById("image-head");
  imageHead.style.backgroundImage = "../static/images/titleimage4.jpg";

  var i = 0;
  
  setInterval(function() {
        imageHead.style.backgroundImage = "url(" + images[i] + ")";
        i = i + 1;
        if (i == images.length) {
            i =  0;
        }
  }, 7500);