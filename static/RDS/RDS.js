//  pop up content --------------------------------------------------

const con = document.getElementById('container');
const con1 = document.getElementById('container1');
const con2 = document.getElementById('container2');
const con3 = document.getElementById('container3');
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
const txt11 = document.getElementById('txt11');
const btn1 = document.getElementById('btn1');
const out1 = document.getElementById('output1');
const popup = document.getElementById('popup');


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
  out1.innerText += '\n';
  out1.innerText += txt11.value;
  out1.innerText += '\n';
})


document.querySelector(".close").addEventListener("click", function () {
  document.querySelector(".popup").style.display = "none";
  out1.innerText = "";
  out1.innerText += '\n';
})


//  pop up content --------------------------------------------------

// let slideIndex = 1;
// showSlides(slideIndex);

// function plusSlides(n) {
//   showSlides(slideIndex += n);
// }

// function currentSlide(n) {
//   showSlides(slideIndex = n);
// }

// function showSlides(n) {
//   let i;
//   let slides = document.getElementsByClassName("mySlides");
//   let dots = document.getElementsByClassName("dot");
//   if (n > slides.length) { slideIndex = 1 }
//   if (n < 1) { slideIndex = slides.length }
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   for (i = 0; i < dots.length; i++) {
//     dots[i].className = dots[i].className.replace(" active", "");
//   }
//   slides[slideIndex - 1].style.display = "block";
//   dots[slideIndex - 1].className += " active";
// }