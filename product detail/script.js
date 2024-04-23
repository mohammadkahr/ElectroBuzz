var navItems = document.querySelectorAll('.product-descriptions-nav-text');
var active_frames = document.querySelectorAll('.detail-frame-active');
var color_frames = document.querySelectorAll('.color_frames');
var shopBtn = document.getElementById('shop-btn-h');



function setDefaultState() {
  if (navItems.length > 0) {
    var firstNavItem = navItems[0];
    firstNavItem.style.color = '#1C4E8E'; 
    firstNavItem.style.textDecoration = 'underline'; 
    firstNavItem.style.fontWeight = 'bold';
  }
}

setDefaultState();


function resetNavItems() {
  navItems.forEach(function(navItem) {
    navItem.style.color = ''; 
    navItem.style.textDecoration = ''; 
    navItem.style.fontWeight = '';
  });
}

function openTab(tabName){
  for (var i = 0; i < active_frames.length; i++) {
    active_frames[i].style.display = "none";
  }
  document.getElementById(tabName).style.display = "block";
}

navItems.forEach(function(navItem) {
  navItem.addEventListener('click', function() {
    resetNavItems();
    navItem.style.color = '#1C4E8E'; 
    navItem.style.textDecoration = 'underline'; 
    navItem.style.fontWeight = 'bold';
    if(navItem[0]){
      openTab(active_frames[0]);
      // console.log("1");
    }
    else if(navItem[1]){
      openTab(active_frames[1]);
      // console.log("2");
    }
    else if(navItem[2]){
      openTab(active_frames[2]);
      // console.log("3");
    }
  });
});

function changeButton(btnid , text) {
  var button = document.getElementById(btnid);
  var displayText = document.getElementById("product-detail-text-price");

  for (var i = 0; i < color_frames.length; i++) {
    color_frames[i].style.borderColor = "none";
    color_frames[i].style.border = "none";
  }

  button.style.borderColor = "#4CAF50";
  button.style.border = "1px solid";
  displayText.textContent = text ; 
}


function changeInputValue(inputId, incrementBtnId, decrementBtnId) {
  const input = document.getElementById(inputId);
  const incrementBtn = document.getElementById(incrementBtnId);
  const decrementBtn = document.getElementById(decrementBtnId);

  incrementBtn.addEventListener('click', function() {
    const currentValue = parseFloat(input.value);
    input.value = currentValue + 1;
  });

  decrementBtn.addEventListener('click', function() {
    const currentValue = parseFloat(input.value);
    if(currentValue > 0){
      input.value = currentValue - 1;
    }
  });
}

changeInputValue('product-detail-text-addcart-val',
'product-detail-text-addcart-plus-button',
'product-detail-text-addcart-minus-button');


function increase_cart(){
  const input = document.getElementById('product-detail-text-addcart-val');
  const cart_number = document.getElementById('cart_number_value');
  cart_number.innerHTML=parseInt(cart_number.innerHTML)+parseInt(input.value);
 
} 

function numItems(){
  var cardsin = document.querySelectorAll('.cards-frame');
  var items = cardsin.length;
  var numbers = document.getElementById('modal-shop-itm-spn');
  numbers.innerHTML = items + " items";
}
numItems();

// var cardsin = document.getElementsByClassName('cards-price-tot1');

function totalPrice(){
  var cardsin = document.querySelectorAll('.cards-price-tot');
  var sum = 0;
  for (var index = 0; index < cardsin.length; index++) {
    console.log(cardsin[index].innerHTML);
    var temp = parseFloat(cardsin[index].innerHTML);
    sum = sum + temp;
    console.log(sum);
  }
  var sumation = document.getElementById('sub-frame-txt-p');
  sumation.innerHTML = "$" + parseFloat(sum);
  
}

function print_on_console(value){
  console.log(value);
}

function disableScroll() {
  document.body.style.overflowY = "hidden";
}

function enableScroll() {
  document.body.style.overflowY = "auto";
}


var modal_addcard = document.getElementById("modal-shop");
var modal_back = document.getElementById("background-focuse");
var btn_addcars = document.getElementById("shop-btn-h");


btn_addcars.onclick = function() {
  modal_back.style.display = "block";
  modal_addcard.style.display = "block";
  disableScroll();
  totalPrice();
}


window.onclick = function(event) {
  if (event.target == modal_back) {
    modal_addcard.style.display = "none";
    modal_back.style.display = "none";
    enableScroll();
  }
}

function deleteCart(index) {
  var item = document.getElementsByClassName("cards-frame")[index];
  item.style.display = "none";
  totalPrice();
  numItems();

}