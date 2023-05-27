const con = document.getElementById('container');
const out1 = document.getElementById('output1')
const txt1 = document.getElementById('txt1');
const txt2 = document.getElementById('txt2');
const txt3 = document.getElementById('txt3');
const txt4 = document.getElementById('txt4');
const txt5 = document.getElementById('txt5');
const txt6 = document.getElementById('txt6');
const txt7 = document.getElementById('txt7');
const txt8 = document.getElementById('txt8');
const txt9 = document.getElementById('txt9');
const txt10 = document.getElementById('txt10');


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
    out1.innerText += txt5.value;
    out1.innerText += '\n';
    out1.innerText += txt6.value;
    out1.innerText += '\n';
    out1.innerText += txt7.value;
    out1.innerText += '\n';
    out1.innerText += txt8.value;
    out1.innerText += '\n';
    out1.innerText += txt9.value;
    out1.innerText += '\n';
    out1.innerText += txt10.value;
})


document.querySelector(".close").addEventListener("click", function () {
    document.querySelector(".popup").style.display = "none";
    out1.innerText = "";
    out1.innerText += '\n';
})