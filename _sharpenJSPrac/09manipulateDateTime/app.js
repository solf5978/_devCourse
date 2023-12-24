
const determineAgeFunction = function(day, month, year) {
  // Month is zero indexed
  let date = new Date(year, month - 1, day);
  if (date < 0) {
    var seconds = (Date.parse(new Date()) + Math.abs(Date.parse(date))) / 1000;
  } else {
    var seconds = (Date.now() - Date.parse(date)) / 1000;
  }
  let minutes = (seconds / 60).toFixed(2);
  let hours = (minutes /  60).toFixed(2);
  let days = Math.floor((hours / 24) % 365.24);
  let years = Math.floor((hours / 24) / 365.24);

  console.log(`You are ${years} years and ${days} days old. Which is ${hours} hours OR ${minutes} minutes OR ${seconds} seconds.`);
};



// Testing determineAgeFunction...

determineAgeFunction(25,5,1965);
determineAgeFunction(1,1,1970);
determineAgeFunction(03,09,2001);
determineAgeFunction(27,04,2023);

