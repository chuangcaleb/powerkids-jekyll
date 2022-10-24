// SRC: https://www.geeksforgeeks.org/how-to-calculate-the-number-of-days-between-two-dates-in-javascript/

var one_day = 1000 * 60 * 60 * 24;

// Get current date
var today = new Date();

// Target date
var deadline = new Date(2022, 10, 15);

// To Calculate the result in milliseconds and then converting into days
var res = Math.round(deadline.getTime() - today.getTime()) / one_day;

// To remove the decimals from the (Result) resulting days value
var diff_days = res.toFixed(0);

// Update element
const daysLeft = document.querySelector("#daysLeft");
daysLeft.textContent = `${diff_days} days left!`;
