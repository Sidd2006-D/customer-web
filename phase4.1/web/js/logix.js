const wsUrl =
  window.location.protocol === "https:"
    ? "wss://" + window.location.host
    : "ws://" + window.location.host;
const socket = new WebSocket(wsUrl);


// -----------------------------------------------------------------------------------------------------------

// SENDING DATA TO EEL

function cancelCustomerEdit(){
  $('#customerEditDOM').hide();
  $('#customerRecordsDOM').show();
  $('#customerForm')[0].reset();
}

async function saveCustomer() {
  let name = $("#name").val();
  let email = $("#email").val();
  let phone = $("#phone").val();
  let product = $("#product").val();
  let processor = $("#processor").val();
  let customerID = $("#customerID").val();

  phone = parseInt(phone);

  if (!name) {
    alert("Name should not be Blank ");
    return;
  } 
  if (!email) {
    alert("Email should not be Blank ");
    return;
  }
  if (!phone) {
    alert("Phone Number should not be Blank ");
    return;
  }
  if (!product) {
    alert("Please select product! ");
    return;
  }
  if (!processor) {
    alert("Please select processor!  ");
    return;
  }

  formData = {
    "name": name,
    "email": email,
    "phone": phone,
    "product": product,
    "processor": processor,
    "customerID": customerID,
  };
  console.log(formData);
  if(customerID)//if customerID=true
    {
    let result = await eel.update_customer(formData)(); 
    $('#customerEditDOM').hide();
    $('#customerRecordsDOM').show();
    updateCustomerTableRowById(result.lastest_customer_data)
  }else{
    let result = await eel.insert_customer(formData)(); 
    console.log(result); 
  }
  $('#customerForm')[0].reset();
  alert("Submited Successfully");
}

function updateCustomerTableRowById(lastest_customer_data){
  let tdsHtml = genrateCustomerTDs(lastest_customer_data);
  console.log(tdsHtml);
  $('#'+lastest_customer_data.id).html(tdsHtml);
}

// -------------------------------------------------------------------------------------------------
// RETRIEVING DATA FROM EEL


async function get_student() {
  let result = await eel.get_all_students()();
  //$("#result_span").html(JSON.stringify(result));
  // render js object(can be map of lsit of var/map) on html
  $("#studentGridTableTbody").html("");
  for (let index in result) {
    let data = result[index];
    let trHtml = genratestudentTableRowHtmlFromMap(data);
    $("#studentGridTableTbody").append(trHtml);
  }
}



// --------------------------------------------------------------------------------------------------------
// SHOWING DATA ON WEBSITE
var formData = {};
//#day 4th 16thJuly25
async function get_list_of_all_customer() {
  let result = await eel.get_list_of_all_customer()();
  //$("#result_span").html(JSON.stringify(result));
  // render js object(can be map of lsit of var/map) on html
  $("#customerGridTableTbody").html(""); // render new html[elements] inside DOM and delete Existing
  for (let index in result) {
    let data = result[index];
    let trHtml = genrateCustomerTableRowHtmlFromMap(data);
    $("#customerGridTableTbody").append(trHtml); // add new one or more element inside DOM
  }
}

function genrateCustomerTDs(data) {
  let tr=[];
  tr.push('<td>');
  tr.push(data.created_on);
  tr.push('</td><td>');
  tr.push(data.name);
  tr.push('</td><td>');
  tr.push(data.email);
  tr.push('</td><td style="text-align:right;">');
  tr.push(data.phone);
  tr.push('</td><td>');
  tr.push(data.product);
  tr.push('</td><td>')
  tr.push(data.processor);
  tr.push('</td><td><button type="button" onclick ="editCustomerRow(this)">Edit</button>')
  tr.push('</td><td><button type="button" onclick ="deleteCustomerRow(this)">Delete</button>')
  tr.push('</td>')
  return tr.join('');
}

function genrateCustomerTableRowHtmlFromMap(data) {
  console.log(data.id);
  console.log(data["name"]); 
  let tr=[];
  tr.push(`<tr id="${data.id}" class="cursor" data-name="${data.name}">`);
  tr.push(genrateCustomerTDs(data))
  tr.push('</tr>')
  return tr.join('')
  

  // return (
  //   '<tr id="' +
  //   data.id +
  //   '"><td>' +
  //   data.created_on +
  //   "</td><td>" +
  //   data.name +
  //   "</td><td>" +
  //   data.email +
  //   "</td><td>" +
  //   data.phone +
  //   "</td><td>" +
  //   data.product +
  //   "</td><td>" +
  //   data.processor +
  //   "</td></tr>"
  // );
}




function genratestudentTableRowHtmlFromMap(data) {
  console.log(data);
  return (
    '<tr id="' +
    data.id +
    '"><td>' +
    data.created_on +
    "</td><td>" +
    data.name +
    "</td><td>" +
    data.dob +
    "</td><td>" +
    data.age +
    "</td><td>" +
    data.class_val +
    "</td><td>" +
    "<button class='btn btn-success' onclick=showEditStudent(this)>edit</button>" +
    "</td><td>" +
    "<button class='btn btn-danger' onclick=deleteStudent_data(this)>delete</button>" +
    "</td></tr>"
  );
}

function showEditStudent(row){
 
  $('#loaddata').hide();
  $('#update_studentForm').show();
  dbrowid=row.parentNode.parentNode.id;
  get_student_by_id(dbrowid);
}

async function get_student_by_id(dbrowid){
  data = await eel.get_stuData_by_id(dbrowid)();
  if (data.id){
    $('studentID').val(data.id)
    $('name').val(data.name)
    $('dob').val(data.dob)
    $('class').val(data.class)
    
  }
}

function deleteStudent_data(id){
   
}
// <tr id="1">
//   <td>23 july</td>
//   <td>siddharth</td>
//   <td>sidd@gmail.com</td>
//   <td>778974878</td>
//   <td>lenovo</td>
//   <td>Ryzen5</td>
// </tr>

// ---------------------------------------------------------------------------------------------
// EDITING CUSTOMERS GRID DATA
function editCustomerRow(element) {
  // here element is an button[edit]
  //element.parentNode is an TD
  //element.parentNode.parentNode is an TD's parentNode TR
  console.log(element.parentNode.parentNode.id);  
  $('#customerEditDOM').show();
  $('#customerRecordsDOM').hide();
  let dbRowId = element.parentNode.parentNode.id;
  getCustomerByID(dbRowId);
  // window.location.href = "/customerEntry.html?rowId=" + element.id;
}


 async function getCustomerByID(dbRowId) {
   
  data = await eel.get_customer_by_id(dbRowId)();
  console.log(data)
  if(data.id){
    $("#customerID").val(data.id);
    $("#name").val(data.name);
    $("#email").val(data.email);
    $("#phone").val(data.phone);
    $("#product").val(data.product);
    $("#processor").val(data.processor);
  }else{ 
    $('#customerEditDOM').hide();
    $('#customerRecordsDOM').show();
    alert("Customer Not Found, Please refresh your page!")
  }
  //if(var) false hoga whenver: "",0,false
 

}


async function deleteCustomerRow(elm){
  // here elm is an button[Delete]
  //elm.parentNode is an TD
  //elm.parentNode.parentNode is an TD's parentNode TR
  let dbRowIdToDelete = elm.parentNode.parentNode.id,
  customerName = elm.parentNode.parentNode.dataset.name; //JS
  console.log(elm.parentNode.parentNode.id); 
  console.log(elm.parentNode.parentNode.dataset); 
  if(!dbRowIdToDelete){
    return;
  }
  if(confirm(`Are you sure to delete ${customerName}?`)){
    console.log("Going for deletion");
    let result = await eel.delete_customer_by_id(dbRowIdToDelete)();
    console.log(result)
    if(result['isDeleted']){
      // $('#elemetID').remove();
      $(`#${dbRowIdToDelete}`).remove(); // Jquery delete element by id
      /*
      js delete element by id
      //step1 
      const elementToRemove = document.getElementById('myElement');
      if (elementToRemove) { //step2 start 
        elementToRemove.remove(); //step3
      }//step2 end
      */
      alert(`${customerName} deleted Successfully!`)
    }
  }else{
    console.log("You pressed cancel!") 
  }

}


async function createStudent(){
  let name = $('#name').val(),
  dob = $('#dob').val(),
  classVal =$('#class').val();

   if( !name){
      alert("enter name !")
      return;
   }

   if( !dob){
      alert("enter DOB! ")
      return;
   }

   if( !classVal){
      alert("Select class! ");
      return;
   }
   
   formData = {
    "name": name, 
    "dob": dob,
    "class": classVal,
    "studentID": '', 
  };
  console.log(formData);
   let result = await eel.insert_student(formData)();
   console.log(result);
}