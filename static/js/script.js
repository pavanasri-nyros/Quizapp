const questionNumberSpan=document.querySelector(".question-num-value");
const totalNumberSpan = document.querySelector(".total-question");
const totalQuestionSpan=document.querySelector(".total-question")
const question = document.querySelector(".question")
const op1 = document.querySelector(".option1");
const op2 = document.querySelector(".option2");
const op3 = document.querySelector(".option3");
const op4 = document.querySelector(".option4");
const answer = docuement.querySelector(".answer");
let questionIndex = 0;
let index = 1;


const questions = [
//     {% for result in results %}
     {
         q : question,
         options : [op1,op2,op3,op4],
         answer : answer
    }

 //    {% endfor %}   
 ]

// const Questions =[
//     {
//         q : "what is c?",
//         options :["Programming laguage","Webframework","Scripting laguage","token"],
//         answer : 0
//     },
//     {
//         q : "what is java",
//         options : ["programming laguage","webframework","SCripting laguage","token"],
//         answer : 0
//     }
// ] 

function load(){
    questionNumberSpan.innerHTML = index+1;
    question.innerHTML = questions[questionIndex].q;
    op1.innerHTML = questions[questionIndex].options[1];
    op2.innerHTML = questions[questionIndex].options[2];
    op3.innerHTML = questions[questionIndex].options[3];
    op4.innerHTML = questions[questionIndex].options[4];
    index++;

    
}

window.onload=function(){
    load();

}