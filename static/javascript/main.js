function appendToExpression(value) {
    const exprField = document.getElementById('expression');
    exprField.value += value;
}

function clearExpression() {
    const exprField = document.getElementById('expression');
    exprField.value = '';  // Clear the input field
}

function toggleSign() {
    const exprField = document.getElementById('expression');
    let currentValue = exprField.value.trim();

    const regex = /(-?\d+(\.\d+)?)(?=[^\d]*$)/;
    const match = currentValue.match(regex);

    if (match) {
        const lastNumber = match[0];
        const newNumber = lastNumber.startsWith('-')
            ? lastNumber.substring(1)
            : '-' + lastNumber;
        currentValue = currentValue.replace(regex, newNumber);
        exprField.value = currentValue;
    }
}

function backspace() {
    const exprField = document.getElementById('expression');
    exprField.value = exprField.value.slice(0, -1);  // Remove last character
}

let openParenthesis = true;
function toggleParenthesis() {
    const exprField = document.getElementById('expression');
    exprField.value += openParenthesis ? '(' : ')';
    openParenthesis = !openParenthesis;
}