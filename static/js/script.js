"use strict";

/*Capture elements within variables:*/
let phospherousAsFed = document.getElementById('phospherousAsFed');
let phospherous = document.getElementById('phospherous');

/*When page loads, check if there was a value entered for 
phospherous.  If not, then hide the phospherous row from the table:*/
window.onload = function() {
	if (phospherousAsFed.textContent === '%') {
		phospherous.classList.add("hidden");
	}   
}