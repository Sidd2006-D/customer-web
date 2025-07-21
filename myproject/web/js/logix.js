const wsUrl =
  window.location.protocol === "https:"
    ? "wss://" + window.location.host
    : "ws://" + window.location.host;
const socket = new WebSocket(wsUrl);


// -----------------------------------------------------------------------------------------------------------

// SENDING DATA TO EEL

async function savecustomer() {
  let name = $("#name").val();
  let email = $("#email").val();
  let phone = $("#phone").val();
  let product = $("#product").val();
  let processor = $("#processor").val();

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
  alert("Submited Successfully")

  formData = {
    name: name,
    email: email,
    phone: phone,
    product: product,
    processor: processor,
  };
  console.log(formData);

  let result = await eel.savecustomer(formData)();
  console.log(result);
}

// -------------------------------------------------------------------------------------------------
// RETRIEVING DATA FROM EEL

var formData = {};
//#day 4th 16thJuly25
async function get_list_of_all_customer() {
  let result = await eel.get_list_of_all_customer()();
  //$("#result_span").html(JSON.stringify(result));
  // render js object(can be map of lsit of var/map) on html
  $("#customerGridTableTbody").html("");
  for (let index in result) {
    let data = result[index];
    let trHtml = genrateCustomerTableRowHtmlFromMap(data);
    $("#customerGridTableTbody").append(trHtml);
  }
}
async function get_student() {
  let result = await eel.get_stu_info()();
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

function genrateCustomerTableRowHtmlFromMap(data) {
  console.log(data.id);
  console.log(data["name"]);

  tr=[];
  tr.push(`<tr id="${data.id}" class="cursor" onclick ="editCustomerRow(this)" ><td>`);
  tr.push(data.created_on);
  tr.push('</td><td>');
  tr.push(data.name);
  tr.push('</td><td>');
  tr.push(data.email);
  tr.push('</td><td>');
  tr.push(data.phone);
  tr.push('</td><td>');
  tr.push(data.product);
  tr.push('</td><td>')
  tr.push(data.processor)
  tr.push('</td><td></tr>')
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
  console.log(data.id);
  console.log(data["name"]);
  return (
    '<tr id="' +
    data.id +
    '"><td>' +
    data.created_on +
    "</td><td>" +
    data.name +
    "</td><td>" +
    data.class +
    "</td><td>" +
    data.section +
    "</td><td>" +
    data.roll_no +
    "</td></tr>"
  );
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
  console.log(element);
  console.log(element.id);
  console.log(element.dataset);
  window.location.href = "/customerEntry.html?rowId=" + element.id;
}
 async function getCustomerByID(id) {
  
  $('#customerID').val(id);
  data = await eel.get_customer_by_id(id)();
  $("#name").val(data.name);
  console.log(`"hello ${data.id}"`)

}