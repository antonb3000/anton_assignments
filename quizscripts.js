function getQuestions() {
    $.ajax({
        url: 'http://localhost:3000/quiz.json',
        async: false,
        dataType: 'json',
        success: function(data) {
            questions = data;
        }
    });
    return questions;
}
getQuestions();

function makeIdName(questionIndex, choiceIndex) {
    return `q_${questionIndex}_${choiceIndex}`;
}

function makeQuestions() {
    let s = "";
    for (let [i, question] of questions.entries()) {
        s += `<br> <p class="text-muted"><b> ${question.question} </b></p> `;

        for (let [j, choice] of question.choices.entries()) {
            let questionId = makeIdName(i, j);
            s +=
                `<input type="radio" name="q${i}" ="${j}" id="${questionId}">` +
                ` <label for="${questionId}">${choice.text}</label><br>`;
        }
    }
    document.getElementById("dynamic").innerHTML = s;
}

var howmany = questions.length;

function reply() {
    let points = 0;
    for (let [i, question] of questions.entries()) {
        for (let [j, choice] of question.choices.entries()) {
            if (document.getElementById(makeIdName(i, j)).checked) {
                points += choice.value;
            }
        }
    }


    function checkFunc() {
        if (document.querySelectorAll('input[type="radio"]:checked').length !== howmany)
            document.getElementById('output').innerHTML = (`<p class="text-danger">Please answer all the questions!</p>`);
        else
            document.getElementById('output').innerHTML = (`Your score: ${points}/${howmany} `);
    }
    checkFunc()


    if (points === howmany)
        document.getElementById('output').innerHTML = (`Your score: ${points}/${howmany} <br>`);

    event.preventDefault();
    return false;
}