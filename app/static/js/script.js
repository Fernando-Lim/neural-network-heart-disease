function validateForm() {
    let inputs = document.querySelectorAll("input[type='number']");
    let selects = document.querySelectorAll("select");
    for (let input of inputs) {
        if (input.value === "" || input.value === null) {
            alert("Please fill in all fields");
            return false;
        }
    }

    for (let select of selects) {
        if (select.value === "") {
            alert("Please make a selection for all dropdown fields");
            return false;
        }
    }

    return true;
}

let lastValidInputValue;
let selectedDot = false;

// Restrict input for number fields
function restrictNumberInput(event) {
    let key = event.key;

    // Allow only numbers for age input
    if (event.target.name === 'age') {
        if (!/[0-9]/.test(key) && key !== "Backspace" && key !== "Delete") {
            event.preventDefault();
        }
    } else {
        // Allow numbers, Backspace, Delete, and a single dot for other inputs
        if (!/[0-9]/.test(key) && key !== "Backspace" && key !== "Delete" && key !== ".") {
            event.preventDefault();
        }

        // Allow the dot only if there is no existing dot in the input
        if (key === ".") {
            if (event.target.value.indexOf(".") !== -1 && !selectedDot) {
                event.preventDefault();
            }
            // Prevent dot if the input is empty
            if (event.target.value.length === 0) {
                event.preventDefault();
            }
        }
        selectedDot = false;
    }
}

// Validate input and control decimal places
function onInput(event) {
    const input = event.target;
    const dataToFixed = parseInt(input.getAttribute("data-toFixed"));

    // Check for decimal places for non-age fields
    if (input.name !== 'age' && input.value.indexOf(".") < input.value.length - dataToFixed - 1 && input.value.indexOf(".") !== -1) {
        let newValue = input.value.slice(0, input.value.indexOf(".") + dataToFixed + 1);
        input.value = parseFloat(newValue);
    }

    // Save the last valid input value
    if (input.value !== "") {
        lastValidInputValue = input.value;
    } else if (event.inputType.match(/delete/g)) {
        lastValidInputValue = "";
    } else {
        input.value = lastValidInputValue;
    }
}

// Allow typing a new dot if the existing dot is selected
const onSelect = (event) => {
    if (window.getSelection().toString().indexOf(".") > -1) {
        selectedDot = true;
    }
}

// Function to show loading state
function showLoading() {
    document.querySelector('.loading').style.display = 'block';
    document.querySelector('#predict_button').disabled = true;
}

// Run when the window loads
window.onload = function () {
    let numberInputs = document.querySelectorAll("input[type='number']");
    numberInputs.forEach(input => {
        input.addEventListener('keypress', restrictNumberInput);
        input.addEventListener('input', onInput);
        input.addEventListener('select', onSelect);
    });

    let form = document.querySelector('form');
    form.onsubmit = function () {
        if (validateForm()) {
            showLoading();
        }
    };
};