function coordinateFromRangeToInput() {
    var slider = document.getElementById("sliderInput") as HTMLInputElement | null;
    var sliderValue = slider?.value;
    console.log(sliderValue)
    var inputBox = document.getElementById("initialangle") as HTMLInputElement | null;
    inputBox!.value = sliderValue!;
}


function coordinateFromInputToRange() {
    var inputBox = document.getElementById("initialangle") as HTMLInputElement | null;
    var inputValue = inputBox?.value;
    if (Number(inputValue) > 90) {
        inputBox!.value = "90";
    } else if (Number(inputValue) < -90) {
        inputBox!.value = "-90";
    } else if (inputValue![1] === "-") {
        inputBox!.value = "-";
    }

    var slider = document.getElementById("sliderInput") as HTMLInputElement | null;
    slider!.value = inputValue!;

    for (let i = 2; i < inputValue!.length; i++) {
        if (inputValue![i] === "-") {
            inputBox!.value = inputValue!.slice(0, i);
            slider!.value = inputBox!.value;
            break;
        }
    }
}