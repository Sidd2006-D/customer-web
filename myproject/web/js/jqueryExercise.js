function testCssWithJQ(){
  //$('.li3').css("color", "green");
  
  $('.li1, .li2, .li3').css({
    "color": "green",
    "font-size": "18px",
    "font-style": "italic",
  });

  $('.li3').html("<b>This is html change by jQ using:<br>Css in Jquery");  
}

function howLoopWillWorks(){

  // for(let i=1;i<=10;i++){
  //   console.log(i)
  // }

  let a = $('#orderListTest li');
  console.log(a);
  // $([]).forEach(element => {
    
  // });
  $('#orderListTest li').each(function(index, domElement){
    // console.log(index);
    domElement.className = "li3";
    console.log(domElement.className);
  }); 
  //let dataArray = [{"name": "Akash", "dob": "XXX"}];
  //generate csv file and download
  //generate csv file from data and download
  //datatable
}

function addNumber(){
  var a = $('#firstN').val(); // getting value by id of the input
  var b = $('#secondN').val();
  if(!a){
    return;
  }
  if(!b){
    return;
  }
  // a = parseInt(a); // convert string to integer val
  a = parseFloat(a); // to decimal/floating point
  b = parseFloat(b);
  var c = a+b;
  console.log(a,'+',b,'=',c,typeof(a), typeof(b));
   $('#resultN').val(c); // set value by id
   $('#firstN').val(''); // set value by id
   $('#secondN').val(''); // set value by id

}


function showD1hideD2(){
  $('#D1').show();  
  $('#D2').hide();  
}
function hideD1ShowD2(){
  $('#D1').hide(); 
  $('#D2').show();  
}
function toggleD1andD2(){
  $('#D1,#D2').toggle(); // can accept multi DOM id or class
  // if dom/eleemt is visible then it will hide, if its hidden then it will became visible 
}

function hideAll(){
  $('#D1,#D2,#D3').hide();
}
function showAll(){
  $('#D1,#D2,#D3').show();
}

function replaceD1Html(){
  const now = new Date(); //js
  //Jquery
  $('#D1').html(`<strong>Dom D1 Html was replace by this Content: ${now.toLocaleString()}</strong>`);
}

function replaceD2Html(){
  $('#D2').html('<h5>Hello! THIS is D2</h5>')
}
function appendD1Html(){
  $('#D1').append('<h5>HI! This is apended in D1</h5>')
}
function prependD1Html(){
  $('#D1').prepend('<h5>Hello! This is D1.How are you?</h5>')
}