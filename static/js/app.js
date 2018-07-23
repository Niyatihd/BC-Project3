/****** TEST ******/
console.log("app.js link Works!!!!!!!!!!!")

//##########################################################
//Post, get values to and from app.py and render sliderplot 
//##########################################################

function updatePlot(ddl1) {
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
    });

}

