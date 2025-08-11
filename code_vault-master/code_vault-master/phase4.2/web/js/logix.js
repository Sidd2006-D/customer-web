//JS DS
/*

string
int
float
array =[]
map =[]
new Set()// python set()

-------------------
[Done]Fresh Data rendering into HTML UI.
[]New Entry Render into HTML UI
[]Udate Entry Re-render into HTML UI

----------------------------

Read file(CSV/xlsx/xml) then prepare DS for handling data.
DS from file reading or JSON File.
Render data into table.

Class Object.
Object Orient Programing in JS

*/
var fanTRTDButtons =
  '<td><button type="button" onclick="editrow(this)" class="btn btn-warning" data-toggle="modal" data-target="#myModal">Edit</button></td><td><button onclick="deleteFan(this)" type="button" class="btn btn-danger"> Delete</button></td>';

async function loadFanMasterApi() {
  let data = await eel.get_all_fan_data()();
  console.log(data);

  // Clear existing table data
  $("#masterTable").html("");
  let options = ['<option value="">-Select-</option>'];
  let trPart = [];
  for (let index in data) {
    let fanMap = data[index];
    // let trPart = [];
    trPart.push(
      `<tr id="${fanMap.fan_id}" class="cursor" data-name="${fanMap.name}">`
    );
    trPart.push(`<td>${fanMap.fan_name}</td>`);
    trPart.push(`<td>${fanMap.fan_rate}</td>`);
    trPart.push(fanTRTDButtons);
    trPart.push("</tr>");
    // let tr = trPart.join('');
    // $("#masterTable").append(tr);
    // $("#masterTable").append(trPart.join(''));
    options.push(
      `<option value="${fanMap.fan_id}">${fanMap.fan_name}</option>`
    );
  }
  $("#masterTable").html(trPart.join(""));
  $("#selectedFan").html(options.join(""));
}

async function loadFanStockApi() {
  let data = await eel.get_all_fan_data()();
  console.log(data);

  // Clear existing table data
  $("#masterTable").html("");

  let options = ['<option value="">-Select-</option>'];

  for (let index in data) {
    let fanMap = data[index];
    let trPart = [];

    trPart.push(
      `<tr id="${fanMap.fan_id}" class="cursor" data-name="${fanMap.fan_name}">`
    );
    trPart.push(`<td>${fanMap.fan_name}</td>`);
    trPart.push(`<td>${fanMap.qty}</td>`);

    trPart.push(
      '<td><button onclick="deleteFanStock(this)" type="button" class="btn btn-danger">Delete</button></td>'
    );
    trPart.push(`</tr>`);
    $("#masterTable").append(trPart.join(""));

    options.push(
      `<option value="${fanMap.fan_id}">${fanMap.fan_name}</option>`
    );
  }

  $("#selectedFan").html(options.join(""));
}

async function insert_fans() {
  let Fanname = $("#fanName").val(),
    Fanrate = $("#fanRate").val(),
    Fanstock = $("fanstock").val();

  if (!Fanname) {
    alert("Fan Name cannot be empty");
    return;
  }

  if (!Fanrate) {
    alert("Fan Rate cannot be empty");
    return;
  }

  fan_dict = {
    name: Fanname,
    rate: Fanrate,
    qty: Fanstock,
  };
  await eel.inserting_data(fan_dict)();
  console.log(fan_dict);
  loadFanMasterApi();
  alert("Submitted Successfully");
}

async function add_fan_stock() {
  console.log(" ADD BUTTON CLICKED");
  let selectedFan = $("#selectedFan").val(),
    qty = $("#qty").val();
  if (!selectedFan) {
    return;
  }
  if (!qty) {
    return;
  }
  if (isNaN(selectedFan)) {
    return;
  }
  if (isNaN(qty)) {
    return;
  }
  let data = {
    fan_id: parseInt(selectedFan),
    qty: parseInt(qty),
  };
  let msg = await eel.update_fan_stock_add(data)();
  console.log(msg);
  loadFanStockApi();
  alert(msg);

  qty = $("#qty").val("");
}

async function reduce_fan_stock() {
  console.log(" REDUCE BUTTON CLICKED");
  let selectedFan = $("#selectedFan").val(),
    qty = $("#qty").val();
  if (!selectedFan) {
    return;
  }
  if (!qty) {
    return;
  }
  if (isNaN(selectedFan)) {
    return;
  }
  if (isNaN(qty)) {
    return;
  }
  let data = {
    fan_id: parseInt(selectedFan),
    qty: parseInt(qty),
  };
  let msg = await eel.update_fan_stock_reduce(data)();
  console.log(msg);
  loadFanStockApi();
  alert(msg);

  qty = $("#qty").val("");
}

/**
 * Edits a table row when the associated button is clicked.
 *

 *
 * The function uses:
 * - `row.attr('id')`: Retrieves the value of the 'id' attribute of the selected table row.
 * - `row.data('name')`: Retrieves the value of the data attribute 'data-name' from the selected table row.
 */
function editrow(buttonElement) {
  // Get the parent <tr> of the clicked button
  let row = $(buttonElement).closest("tr"); //closest() is a jQuery function that finds the nearest parent element that matches the selector.

  let fanId = row.attr("id");
  let fanName = row.data("name");
}

async function deleteFan(buttonElement) {
  let row = $(buttonElement).closest("tr");

  let fanId = row.attr("id");
  let fanName = row.data("name");
  let data = { fan_id: fanId, fan_name: fanName };

  let confirmed = confirm("Are you sure you want to delete this data?");
  if (confirmed) {
    let msg = await eel.delete_fan_stock(data)();
    alert(msg);
    loadFanMasterApi();
  }
}

async function deleteFanStock(buttonElement) {
  let row = $(buttonElement).closest("tr");

  let fanId = row.attr("id");
  let fanName = row.data("name");
  let data = { fan_id: fanId, fan_name: fanName };

  let confirmed = confirm("Are you sure you want to delete this data?");
  if (confirmed) {
    let msg = await eel.delete_fan_stock(data)();
    alert(msg);
    loadFanStockApi();
  }
}
