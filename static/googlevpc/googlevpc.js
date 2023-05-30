var x, i, j, l, ll, selElmnt, a, b, c;
/*look for any elements with the class "custom-select":*/
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  /*for each element, create a new DIV that will act as the selected item:*/
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected select-selected-bottom-rounded");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  /*for each element, create a new DIV that will contain the option list:*/
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    /*for each option in the original select element,
    create a new DIV that will act as an option item:*/
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function (e) {
      /*when an item is clicked, update the original select box,
      and the selected item:*/
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
          y = this.parentNode.getElementsByClassName("same-as-selected");
          yl = y.length;
          for (k = 0; k < yl; k++) {
            y[k].removeAttribute("class");
          }
          this.setAttribute("class", "same-as-selected");
          break;
        }
      }
      h.click();
    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function (e) {
    /*when the select box is clicked, close any other select boxes,
    and open/close the current select box:*/
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
    this.classList.toggle("select-selected-bottom-square");
  });
}
function closeAllSelect(elmnt) {
  /*a function that will close all select boxes in the document,
  except the current select box:*/
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
      y[i].classList.remove("select-selected-bottom-square");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}
/*if the user clicks anywhere outside the select box,
then close all select boxes:*/
document.addEventListener("click", closeAllSelect);

// popup content ---------------
// const con = document.getElementById('container');
// const txt1 = document.getElementById('txt1');
// const txt2 = document.getElementById('txt2');
// const txt3 = document.getElementById('txt3');
// const txt4 = document.getElementById('txt4');
// const txt5 = document.getElementById('txt5');
// const txt6 = document.getElementById('txt6');
// const txt7 = document.getElementById('txt7');
// const txt8 = document.getElementById('txt8');
// const txt9 = document.getElementById('txt9');
// const txt10 = document.getElementById('txt10');
// const txt11 = document.getElementById('txt11');
// const txt12 = document.getElementById('txt12');
// const txt13 = document.getElementById('txt13');
// const txt14 = document.getElementById('txt14');
// const txt15 = document.getElementById('txt15');
// const txt16 = document.getElementById('txt16');
// const txt17 = document.getElementById('txt17');
// const txt18 = document.getElementById('txt18');
// const txt19 = document.getElementById('txt19');
// const txt20 = document.getElementById('txt20');
// const txt21 = document.getElementById('txt21');
// const txt22 = document.getElementById('txt22');
// const txt23 = document.getElementById('txt23');
// const txt24 = document.getElementById('txt24');
// const txt25 = document.getElementById('txt25');
// const txt26 = document.getElementById('txt26');
// const txt27 = document.getElementById('txt27');
// const txt28 = document.getElementById('txt28');
// const txt29 = document.getElementById('txt29');
// const txt30 = document.getElementById('txt30');
// const txt31 = document.getElementById('txt31');
// const txt32 = document.getElementById('txt32');
// const txt33 = document.getElementById('txt33');
// const txt34 = document.getElementById('txt34');
// const btn1 = document.getElementById('btn1');
// const out1 = document.getElementById('output1');
// const popup = document.getElementById('popup');
// const selectElement1 = document.getElementById('select1'); 
// const selectElement2 = document.getElementById('select2'); 
// const radioButtons = document.querySelectorAll('input[name="gender"]');
// const scan = document.querySelectorAll('input[name="scan"]');


// document.getElementById('button').addEventListener("click", function () {
//   document.querySelector('.popup').style.display = "flex";
//   out1.innerText += txt1.value;
//   out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement1.value;
//   // out1.innerText += '\n';
//   out1.innerText += selectElement1.value;
//   out1.innerText += '\n';
//   out1.innerText += selectElement2.value;
//   out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += selectElement2.value;
//   // out1.innerText += '\n';
//   // out1.innerText += txt28.value;
//   // out1.innerText += '\n';
//   out1.innerText += txt29.value;
//   out1.innerText += '\n';
//   out1.innerText += txt30.value;
//   out1.innerText += '\n';
//   out1.innerText += txt31.value;
//   out1.innerText += '\n';
//   out1.innerText += txt32.value;
//   out1.innerText += '\n';
//   out1.innerText += txt33.value;
//   out1.innerText += '\n';
//   out1.innerText += txt34.value;
//   out1.innerText += '\n';
//   for (const radioButton of radioButtons) {
//     if (radioButton.checked) {
//       out1.innerText += radioButton.value;
//       out1.innerText += '\n';
//     }
//   }
//   for (const Scans of scan) {
//     if (Scans.checked) {
//       out1.innerText += Scans.value;
//       out1.innerText += '\n';
//     }
//   }
// })


// document.querySelector(".close").addEventListener("click", function () {
//   document.querySelector(".popup").style.display = "none";
//   out1.innerText = "";
//   out1.innerText += '\n';
// })
// // popup content ---------------