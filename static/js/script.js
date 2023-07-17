"use strict";

/*Capture elements within variables:*/
let phospherousAsFed = document.getElementById('phospherousAsFed');
let phospherous = document.getElementById('phospherous');

window.onload = function() {
	if (phospherousAsFed.textContent === '%') {
		phospherous.classList.add("hidden");
	}   
}