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
        todoListItem1.innerHTML = "Jobs: " + (empCoeff*100).toFixed(0) + "%";
        var todoListItem2= document.createElement("p1");
        todoListItem2.innerHTML = "Household: " + (householdCoeff*100).toFixed(0) + "%";
        var todoListItem3= document.createElement("p1");
        todoListItem3.innerHTML = "Wages: " + (wageCoeff*100).toFixed(0) + "%";
        empCoeffid.appendChild(todoListItem1);
        empCoeffid.appendChild(todoListItem2);
        empCoeffid.appendChild(todoListItem3);

    });
});
}