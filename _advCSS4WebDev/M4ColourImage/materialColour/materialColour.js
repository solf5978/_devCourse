var COLORS = document.getElementsByClassName("color-grid");
// console.log(COLORS);

var COLOR_BTNS = document.getElementById("color-categories").children;
// console.log(COLOR_BTNS);

for (var i = 0; i < COLOR_BTNS.length; i++) {
  COLOR_BTNS[i].addEventListener("click", changeColor);
}

function changeColor(e) {
  // alert( e.target.innerText.toLowerCase() );
  showColor(e.target.innerText.toLowerCase());
}

function showColor(name) {
  for (var i = 0; i < COLORS.length; i++) {
    COLORS[i].style.display = "none";

    if (COLORS[i].className === "color-grid " + name + "-colors") {
      COLORS[i].style.display = "grid";
    }
  }
}

/** RGBA Demo **/
window.onload = function () {
  var redValue, greenValue, blueValue, rgbAlphaValue;
  var redSlide = document.getElementById("redSlider");
  var greenSlide = document.getElementById("greenSlider");
  var blueSlide = document.getElementById("blueSlider");
  var rgbAlphaSlide = document.getElementById("rgbAlphaSlider");

  redSlide.oninput = function () {
    redValue = parseInt(redSlide.value);
    greenValue = parseInt(greenSlide.value);
    blueValue = parseInt(blueSlide.value);
    rgbAlphaValue = parseFloat(rgbAlphaSlide.value);

    showRGBOutcome();
  };

  greenSlide.oninput = function () {
    redValue = parseInt(redSlide.value);
    greenValue = parseInt(greenSlide.value);
    blueValue = parseInt(blueSlide.value);
    rgbAlphaValue = parseFloat(rgbAlphaSlide.value);

    showRGBOutcome();
  };

  blueSlide.oninput = function () {
    redValue = parseInt(redSlide.value);
    greenValue = parseInt(greenSlide.value);
    blueValue = parseInt(blueSlide.value);
    rgbAlphaValue = parseFloat(rgbAlphaSlide.value);

    showRGBOutcome();
  };

  rgbAlphaSlide.oninput = function () {
    redValue = parseInt(redSlide.value);
    greenValue = parseInt(greenSlide.value);
    blueValue = parseInt(blueSlide.value);
    rgbAlphaValue = parseFloat(rgbAlphaSlide.value);

    showRGBOutcome();
  };

  function showRGBOutcome() {
    document.getElementById("rgbOutcomebox").style.backgroundColor =
      "rgba(" +
      redValue +
      "," +
      greenValue +
      ", " +
      blueValue +
      "," +
      rgbAlphaValue +
      ")";
    document.getElementById(
      "rgbOutcomecode"
    ).innerHTML = document.getElementById(
      "rgbOutcomebox"
    ).style.backgroundColor;
  }

  /** HSLa Interaction **/
  var hueValue, satValue, lightValue, hslAlphaValue;
  var hueSlide = document.getElementById("hueSlider");
  var satSlide = document.getElementById("saturationSlider");
  var lightSlide = document.getElementById("lightSlider");
  var hslAlphaSlide = document.getElementById("hslAlphaSlider");

  hueSlide.oninput = function () {
    hueValue = parseInt(hueSlide.value);
    satValue = parseInt(satSlide.value);
    lightValue = parseInt(lightSlide.value);
    hslAlphaValue = parseFloat(hslAlphaSlide.value);

    document.getElementById("hueValue").value = hueValue;
    var sineTheta = Math.sin(Math.PI / 2 - (hueValue * Math.PI) / 180);
    var cosineTheta = Math.cos(Math.PI / 2 - (hueValue * Math.PI) / 180);
    document.getElementById("hueCircle").style.transform =
      "translate(" + 66 * cosineTheta + "px," + -66 * sineTheta + "px)";

    document.getElementById("satBox").style.background =
      "linear-gradient(to right, hsl(" +
      hueValue +
      ",0%," +
      lightValue +
      "%), hsl(" +
      hueValue +
      ",100%," +
      lightValue +
      "%))";
    document.getElementById("lightBox").style.background =
      "linear-gradient(to right, hsl(" +
      hueValue +
      "," +
      satValue +
      "%, 0%), hsl(" +
      hueValue +
      ", " +
      satValue +
      "%, 50%), hsl(" +
      hueValue +
      ", " +
      satValue +
      "%, 100%))";
    showHSLOutcome();
  };

  satSlide.oninput = function () {
    hueValue = parseInt(hueSlide.value);
    satValue = parseInt(satSlide.value);
    lightValue = parseInt(lightSlide.value);
    hslAlphaValue = parseFloat(hslAlphaSlide.value);

    document.getElementById("satValue").value = satValue;
    document.getElementById("lightBox").style.background =
      "linear-gradient(to right, hsl(" +
      hueValue +
      "," +
      satValue +
      "%, 0%), hsl(" +
      hueValue +
      ", " +
      satValue +
      "%, 50%), hsl(" +
      hueValue +
      ", " +
      satValue +
      "%, 100%))";
    showHSLOutcome();
  };

  lightSlide.oninput = function () {
    hueValue = parseInt(hueSlide.value);
    satValue = parseInt(satSlide.value);
    lightValue = parseInt(lightSlide.value);
    hslAlphaValue = parseFloat(hslAlphaSlide.value);

    document.getElementById("lightValue").value = lightValue;
    document.getElementById("satBox").style.background =
      "linear-gradient(to right, hsl(" +
      hueValue +
      ",0%," +
      lightValue +
      "%), hsl(" +
      hueValue +
      ",100%," +
      lightValue +
      "%))";
    showHSLOutcome();
  };

  hslAlphaSlide.oninput = function () {
    hueValue = parseInt(hueSlide.value);
    satValue = parseInt(satSlide.value);
    lightValue = parseInt(lightSlide.value);
    hslAlphaValue = parseFloat(hslAlphaSlide.value);

    showHSLOutcome();
  };

  function showHSLOutcome() {
    document.getElementById("hslOutcomebox").style.backgroundColor =
      "hsla(" +
      hueValue +
      "," +
      satValue +
      "%, " +
      lightValue +
      "%," +
      hslAlphaValue +
      ")";
    document.getElementById("hslOutcomecode").innerHTML =
      "hsla(" +
      hueValue +
      ", " +
      satValue +
      "%, " +
      lightValue +
      ", " +
      hslAlphaValue +
      ")<br />" +
      document.getElementById("hslOutcomebox").style.backgroundColor;
  }
};
