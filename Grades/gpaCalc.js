var grades = [];

function calculate() {
    let onlyDigits = true;
    for (var i = 1; i < numClass + 1; i++) {
        let id = `grade${i}`;
        let rowValue = document.getElementById(id).value;
        // console.log(id);
        switch (rowValue) {
            case "":
                console.log("This is empty");
                break;
            default:
                rowValue = parseInt(rowValue);
                grades.push(rowValue);
        }

    }
    if (onlyDigits) {
        let gpa = grades.reduce((a, b) => a + b, 0)
        console.log(gpa);
    }
}