const con = document.getElementById('container');
const txt1 = document.getElementById('txt1');
const txt2 = document.getElementById('txt2');
const txt3 = document.getElementById('txt3');
const txt4 = document.getElementById('txt4');
const txt5 = document.getElementById('txt5');
const txt6 = document.getElementById('txt6');
const txt7 = document.getElementById('txt7');
const btn1 = document.getElementById('btn1');
const out1 = document.getElementById('output1');
const popup = document.getElementById('popup');
const radioButtons = document.querySelectorAll('input[name="gender"]');
const scan = document.querySelectorAll('input[name="scan"]');


document.getElementById('button').addEventListener("click", function () {
    document.querySelector('.popup').style.display = "flex";
    out1.innerText += txt1.value;
    out1.innerText += '\n';
    out1.innerText += txt2.value;
    out1.innerText += '\n';
    out1.innerText += txt3.value;
    out1.innerText += '\n';
    out1.innerText += txt4.value;
    out1.innerText += '\n';
    for (const radioButton of radioButtons){
        if(radioButton.checked){
            out1.innerText += radioButton.value;
            out1.innerText += '\n';
        }
    }
    for(const Scans of scan){
        if(Scans.checked){
            out1.innerText +=Scans.value;
            out1.innerText += '\n';
        }
    }
})


document.querySelector(".close").addEventListener("click", function () {
    document.querySelector(".popup").style.display = "none";
    out1.innerText = "";
    out1.innerText += '\n';
})








