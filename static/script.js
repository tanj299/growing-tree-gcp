'use strict';

window.addEventListener('load', function () {

    console.log("Hello World!");

});

function sayHello() {
    alert("Hello World")
}

function startCounter() {
    interval = setInterval(function () {
        document.getElementById("seconds").innerHTML = pad(++sec % 60);
        document.getElementById("minutes").innerHTML = pad(parseInt(sec / 60, 10));
    }, 1000);
}

function test() {
    document.getElementById("demo").innerHTML = "Hello World";
}