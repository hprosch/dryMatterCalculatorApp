"use strict";
//Select the calculate button:
let calculate = document.getElementById('calculate');

//Selecting table elements to alter later:
let resultTable = document.getElementById('resultTable');
resultTable.classList.add('hidden');

let dmProteinResult = document.getElementById('dmProtein');
let dmFatResult = document.getElementById('dmFat');
let dmFiberResult = document.getElementById('dmFiber');
let dmOtherResult = document.getElementById('other');

/*Grabbing Error Message Areas:*/
let errorProtein = document.getElementById('spanProtein');
let errorFat = document.getElementById('spanFat');
let errorFiber = document.getElementById('spanFiber');
let errorMoisture = document.getElementById('spanMoisture');

let protein;
let fat;
let fiber;
let moisture;
let other;

function clearErrorMessages() {
	errorProtein.textContent = "";
	errorFat.textContent = "";
	errorFiber.textContent = "";
	errorMoisture.textContent = "";
}

function validateInput() {

	clearErrorMessages();
	resultTable.classList.add('hidden');

	let errorCount = 0;

	protein = +document.getElementById('asProtein').value;
	fat = +document.getElementById('asFat').value;
	fiber = +document.getElementById('asFiber').value;
	moisture = +document.getElementById('asMoisture').value;

	if (protein == 0 || protein == null) {
		errorProtein.textContent = "Please enter a value for protein";
		errorCount++;
	}
	if (fat == 0 || fat == null) {
		errorFat.textContent = "Please enter a value for fat";
		errorCount++;
	}
	if (fiber == 0 || fiber == null) {
		errorFiber.textContent = "Please enter a value for fiber";
		errorCount++;
	}
	if (moisture == 0 || moisture == null) {
		errorMoisture.textContent = "Please enter a value for moisture";
		errorCount++;
	}
	if (errorCount == 0) {
		calculateDryMatterPercentages();
	}
}


function calculateDryMatterPercentages() {

	clearErrorMessages();

	other = 100 - protein - fat - fiber - moisture;

	dmProteinResult.textContent = ((protein * 100) / (100 - moisture)).toFixed(2);
	dmFatResult.textContent = ((fat * 100) / (100 - moisture)).toFixed(2);
	dmFiberResult.textContent = ((fiber * 100) / (100 - moisture)).toFixed(2);
	dmOtherResult.textContent = ((other * 100) / (100 - moisture)).toFixed(2);

	resultTable.classList.remove('hidden');

}

calculate.addEventListener("click", validateInput);