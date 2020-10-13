"use strict"

function writeJob() {
    // create a new form and populate with selected mode
    var form = document.querySelector('form');
    var formData = new FormData(form);
    console.log(formData)

    // create a url with current host
    var url = 'http://' + window.location.host + "/job"
    console.log(url)

    // post data with our form data and api key
    fetch(url, {
        method: "post",
        body: formData,
    })
    .then( (response) => { 
        console.log(response);
    });
}
