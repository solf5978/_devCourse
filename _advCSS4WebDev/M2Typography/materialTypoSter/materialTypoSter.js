/**
 * My version of Lettering.JS
 */
function lettering(elId) {
    var string = document.getElementById(elId);
    var array = [...string.innerText];
  
    string.innerHTML = "";
  
    var lettered = [];
    array.forEach((c, i) => {
      var el = document.createElement("span");
      el.innerText = c;
      el.className = "char" + ++i;
      lettered.push(el);
      string.appendChild(el);
    });
  }
  
  lettering("cover");
  lettering("happy-cover");
  lettering("focus");
  
  addEyes();
  
  /* Hide All but this */
  function addEyes() {
    var headings = document.getElementsByTagName("h4");
  
    for (var i = 0; i < headings.length; i++) {
      var el = document.createElement("i");
      el.className = "fas fa-eye";
      el.setAttribute("title", "Show ONLY this poster");
      el.addEventListener("click", function (e) {
        hideArts(e);
      });
      headings[i].appendChild(el);
    }
  }
  
  function hideArts(e) {
    var arts = document.getElementsByTagName("article");
    var nav = document.getElementsByClassName("section-nav-buttons");
  
    /* Hide Table of Contents */
    var toc = document.getElementsByClassName("table-of-contents")[0];
    toc.style.display = "none";
  
    /* Hide all articles */
    for (var i = 0; i < arts.length; i++) {
      arts[i].style.display = "none";
    }
  
    /* Hide all navigation buttons */
    for (var i = 0; i < nav.length; i++) {
      nav[i].style.display = "none";
    }
  
    /* Reveal THIS article only, but remove the button */
    e.target.parentNode.parentNode.parentNode.style.display = "block";
    e.target.parentNode.parentNode.style.display = "block";
    e.target.remove();
  
    /* Add a new "Show all" button */
    var title = document.getElementsByTagName("h2");
    var el = document.createElement("i");
    el.className = "fas fa-eye";
    el.setAttribute("title", "Show ALL");
    el.addEventListener("click", function (e) {
      showAll(e, arts, nav, toc);
    });
    title[0].appendChild(el);
  }
  
  function showAll(e, arr1, arr2, obj) {
    e.target.remove();
    obj.style.display = "block";
    for (var i = 0; i < arr1.length; i++) {
      arr1[i].style.display = "block";
    }
    for (var i = 0; i < arr2.length; i++) {
      arr2[i].style.display = "block";
    }
    addEyes();
  }
  