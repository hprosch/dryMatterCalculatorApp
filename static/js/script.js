"use strict";

let calculate = document.getElementById('result');

//Selecting table elements to alter later:
let resultHeader = document.getElementById('resultHeader');
resultHeader.classList.add('hidden');

function showResultHeader() {
	resultHeader.classList.remove('hidden');
}

//calculate.addEventListener("click", showResultHeader);