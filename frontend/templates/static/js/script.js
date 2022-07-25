function coordinateFromRangeToInput() {
    var slider = document.getElementById("sliderInput");
    var sliderValue = slider === null || slider === void 0 ? void 0 : slider.value;
    console.log(sliderValue);
    var inputBox = document.getElementById("initialangle");
    inputBox.value = sliderValue;
}
function coordinateFromInputToRange() {
    var inputBox = document.getElementById("initialangle");
    var inputValue = inputBox === null || inputBox === void 0 ? void 0 : inputBox.value;
    if (Number(inputValue) > 90) {
        inputBox.value = "90";
    }
    else if (Number(inputValue) < -90) {
        inputBox.value = "-90";
    }
    else if (inputValue[1] === "-") {
        inputBox.value = "-";
    }
    var slider = document.getElementById("sliderInput");
    slider.value = inputValue;
    for (var i = 2; i < inputValue.length; i++) {
        if (inputValue[i] === "-") {
            inputBox.value = inputValue.slice(0, i);
            slider.value = inputBox.value;
            break;
        }
    }
}
