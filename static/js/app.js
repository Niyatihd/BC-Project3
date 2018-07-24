/****** TEST ******/
console.log("app.js link Works!!!!!!!!!!!")

//##########################################################
//Post, get values to and from app.py and render sliderplot 
//##########################################################

function updatePlot(ddl1) {
    var userSel = ddl1;
    // console.log("creating historical plot with prediction");
    console.log(ddl1);
    var selectedArea = (ddl1 === "Select Area")?"":ddl1;
    // console.log(selectedArea);
    var selectedAreaObj = {areaselected: selectedArea};
    console.log(selectedAreaObj); 
    console.log(JSON.stringify(selectedAreaObj)); 

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

    var empCoeff = data.employees_wt;
    console.log("empCoeff is: " + empCoeff);
    var householdCoeff = data.household_wt;
    var wageCoeff = data.wage_wt;

    // Set variable for the button
    var buttonClick = document.querySelector("#predictionButton");

    // Add click even listener to the button
    buttonClick.addEventListener("click", function() {

        var empCoeffid = document.querySelector('#employeecoeff');
        var todoListItem1= document.createElement("p1");
        todoListItem1.innerHTML = "Jobs: " + (empCoeff*100).toFixed(0) + "%\n";
        var todoListItem2= document.createElement("p1");
        todoListItem2.innerHTML = "Household: " + (householdCoeff*100).toFixed(0) + "%\n";
        var todoListItem3= document.createElement("p1");
        todoListItem3.innerHTML = "Wages: " + (wageCoeff*100).toFixed(0) + "%\n";
        empCoeffid.appendChild(todoListItem1);
        empCoeffid.appendChild(todoListItem2);
        empCoeffid.appendChild(todoListItem3);
    });

        function buildPlot() {
            Plotly.d3.json("/plotlyData", function(error, response) {
                if (error) return console.warn(error);
                console.log(response);
              // Grab values from the response json object to build the plots
              var year = response[userSel].year;
              var households = response[userSel].household;
              var income = response[userSel].income;
              var jobs = response[userSel].jobs;
              var medianHomePrice = response[userSel].medianHomePrice;
              console.log(userSel, year, households, income, jobs, medianHomePrice);
              
            //   function init() {
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
                })
        
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
        
            // init();
            // });
        }

        buildPlot();

    });

}

var images = [
    "../static/images/titleimage.jpeg",
    "../static/images/titleimage1.jpg",
    "../static/images/titleimage2.jpg",
    "../static/images/titleimage3.jpg",
    "../static/images/titleimage4.jpg",
  ]
  
  var imageHead = document.getElementById("image-head");
  imageHead.style.backgroundImage = "../static/images/titleimage4.jpg";

  var i = 0;
  
  setInterval(function() {
        imageHead.style.backgroundImage = "url(" + images[i] + ")";
        i = i + 1;
        if (i == images.length) {
            i =  0;
        }
  }, 5000);