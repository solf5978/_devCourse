var IE = document.getElementsByClassName("fa-internet-explorer");
var EDGE = document.getElementsByClassName("fa-edge");
var CHROME = document.getElementsByClassName("fa-chrome");
var FIREFOX = document.getElementsByClassName("fa-firefox");
var OPERA = document.getElementsByClassName("fa-opera");
var SAFARI = document.getElementsByClassName("fa-safari");

addEventListeners();

/**
 * Selectable Browser Icons
 */
function reset() {
  /* IE */
  for (var i = 0; i < IE.length; i++) {
    IE[i].className = "fab fa-internet-explorer";
  }
  /* EDGE */
  for (var i = 0; i < EDGE.length; i++) {
    EDGE[i].className = "fab fa-edge";
  }
  /* CHROME */
  for (var i = 0; i < CHROME.length; i++) {
    CHROME[i].className = "fab fa-chrome";
  }
  /* FIREFOX */
  for (var i = 0; i < FIREFOX.length; i++) {
    FIREFOX[i].className = "fab fa-firefox";
  }
  /* OPERA */
  for (var i = 0; i < OPERA.length; i++) {
    OPERA[i].className = "fab fa-opera";
  }
  /* SAFARI */
  for (var i = 0; i < SAFARI.length; i++) {
    SAFARI[i].className = "fab fa-safari";
  }
}

function addEventListeners() {
  /* IE */
  for (var i = 0; i < IE.length; i++) {
    IE[i].addEventListener("click", function () {
      toggleActive("ie");
    });
  }
  /* EDGE */
  for (var i = 0; i < EDGE.length; i++) {
    EDGE[i].addEventListener("click", function () {
      toggleActive("edge");
    });
  }
  /* CHROME */
  for (var i = 0; i < CHROME.length; i++) {
    CHROME[i].addEventListener("click", function () {
      toggleActive("chrome");
    });
  }
  /* FIREFOX */
  for (var i = 0; i < FIREFOX.length; i++) {
    FIREFOX[i].addEventListener("click", function () {
      toggleActive("firefox");
    });
  }
  /* OPERA */
  for (var i = 0; i < OPERA.length; i++) {
    OPERA[i].addEventListener("click", function () {
      toggleActive("opera");
    });
  }
  /* SAFARI */
  for (var i = 0; i < SAFARI.length; i++) {
    SAFARI[i].addEventListener("click", function () {
      toggleActive("safari");
    });
  }
  /* PRE */
  document.getElementById("old-code").addEventListener("click", function () {
    showNewCode();
  });
}

function toggleActive(browser) {
  reset();
  switch (browser) {
    case "ie":
      for (var i = 0; i < IE.length; i++) {
        IE[i].className += " active";
      }
      break;
    case "edge":
      for (var i = 0; i < EDGE.length; i++) {
        EDGE[i].className += " active";
      }
      break;
    case "chrome":
      for (var i = 0; i < CHROME.length; i++) {
        CHROME[i].className += " active";
      }
      break;
    case "firefox":
      for (var i = 0; i < FIREFOX.length; i++) {
        FIREFOX[i].className += " active";
      }
      break;
    case "opera":
      for (var i = 0; i < OPERA.length; i++) {
        OPERA[i].className += " active";
      }
      break;
    case "safari":
      for (var i = 0; i < SAFARI.length; i++) {
        SAFARI[i].className += " active";
      }
      break;
    default:
      reset();
  }
}

function showNewCode() {
  var height = document.getElementById("old-code").clientHeight;
  var width = document.getElementById("old-code").clientWidth;
  console.log(width, "+", height);

  document.getElementById("new-code").style.height = height + "px";
  document.getElementById("new-code").style.width = width + "px";
  document.getElementById("new-code").style.display = "block";
}

/* Change Font Stack (in order) */
/* Serif */
document.getElementById("stack-serif").onclick = function () {
  this.className += " strike";
  document.getElementById("font-stack").style.fontFamily = "sans-serif";
};

/* Sans-serif */
document.getElementById("stack-sans").onclick = function () {
  this.className += " strike";
  document.getElementById("font-stack").style.fontFamily = "cursive";
};

/* Script */
document.getElementById("stack-script").onclick = function () {
  this.className += " strike";
  document.getElementById("font-stack").style.fontFamily = "monospace";
};

/* Monospace */
document.getElementById("stack-mono").onclick = function () {
  this.className += " strike";
  document.getElementById("font-stack").style.fontFamily = "fantasy";
};

/* Decorative */
document.getElementById("stack-deco").onclick = function () {
  this.innerText = "serif";
  document.getElementById("font-stack").style.fontFamily = "serif";
};

/* Show CSS rules */
var importFace = 0;
document.getElementById("import-face").onclick = function () {
  this.children[importFace++].style.visibility = "visible";
};
