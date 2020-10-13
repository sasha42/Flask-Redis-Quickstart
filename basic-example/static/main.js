"use strict"

// create a url with current host
var url = 'http://' + window.location.host + "/data"
console.log(url)

function readData() {
    // checks the status from adafruit
    fetch(url)
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
    fetch(url, {
        method: "post",
        body: formData,
    })
    .then( (response) => { 
        console.log(response);
    });
}
