"use strict"

function readData() {
    // checks the status from adafruit
    fetch("http://localhost:5000/data")
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        console.log(data);
        document.getElementById('redis-data').innerHTML = JSON.stringify(data);
    }).catch(function(error) {
        console.log(error);
    });

}

function writeData() {
    // create a new form and populate with selected mode
    var form = document.querySelector('form');
    var formData = new FormData(form);
    console.log(formData)

    // post data with our form data and api key
    fetch("http://localhost:5000/data", {
        method: "post",
        body: formData,
    })
    .then( (response) => { 
        console.log(response);
    });
}
