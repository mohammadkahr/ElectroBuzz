// Get the modal
var modal = document.getElementById("loginModal");
var modal_log = document.getElementById("RegModal");
var modal_otp = document.getElementById("otpModal");
var modal_passChange = document.getElementById("passChangeModal");
var modal_back_login = document.getElementById("background-focuse");



// Get the button that opens the modal
var btn = document.getElementById("loginBtn");
var btn_log = document.getElementById("RegBtn");
var btn_otp = document.getElementById("OTPBtn");
var btn_passch = document.getElementById("passChangeBtn");
var btn_backtol = document.getElementById("Back_to_Login");




// Get the <span> element that closes the modal
var closeBtnSpan = document.getElementsByClassName("close");

function disableScroll() {
  document.body.style.overflowY = "hidden";
}

function enableScroll() {
  document.body.style.overflowY = "auto";
}

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal_back_login.style.display = "block";
  modal.style.display = "block";
  disableScroll();
}
btn_log.onclick = function() {
  modal.style.display = "none";
  modal_back_login.style.display = "block";
  modal_log.style.display = "block";
  disableScroll();
}
btn_otp.onclick = function() {
  modal.style.display = "none";
  modal_log.style.display = "none";
  modal_back_login.style.display = "block";
  modal_otp.style.display = "block";
  disableScroll();
}
btn_passch.onclick = function() {
  modal.style.display = "none";
  modal_log.style.display = "none";
  modal_back_login.style.display = "block";
  modal_otp.style.display = "none";
  modal_passChange.style.display = "block";
  disableScroll();
}
btn_backtol.onclick = function() {
  modal_log.style.display = "none";
  modal_otp.style.display = "none";
  modal_back_login.style.display = "block";
  modal_passChange.style.display = "none";
  modal.style.display = "block";
  disableScroll();
}



// When the user clicks on <span> (x), close the modal
for (let i = 0; i < closeBtnSpan.length; i++) {
  closeBtnSpan[i].onclick = function() {
    // console.log("1");
    modal.style.display = "none";
    // console.log("2");
    RegModal.style.display = "none";
    // console.log("3");
    otpModal.style.display = "none";
    // console.log("4");
    modal_back_login.style.display = "none";
    enableScroll();
  }
}
