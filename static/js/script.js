"use strict";

let calculate = document.getElementById('result');

//Selecting table elements to alter later:
let resultHeader = document.getElementById('resultHeader');
resultHeader.classList.add('hidden');


/*Add functionality to make image full screen and translucent
in mobile sized screens.  Image stays left aligned and opaque
in tablet and full screen renditions. -HP */

function showResultHeader() {
	resultHeader.classList.remove('hidden');
}

//calculate.addEventListener("click", showResultHeader);