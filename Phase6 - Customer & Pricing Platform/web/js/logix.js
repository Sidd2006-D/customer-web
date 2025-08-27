async function addProduct() {
  //product.html
  let Pname = $("#Pname").val(),
    Prate = $("#Prate").val(),
    tax = $("#tax").val();
  if (!Pname) {
    alert("Product name should not be blank!");
    return;
  }
  if (!Prate) {
    alert("Rate should not be blank!");
    return;
  }
  if (!tax) {
    alert("Tax should not be blank!");
    return;
  }
  let data = {
    name: Pname,
    rate: Prate,
    tax: tax,
  };
  let result = await eel.saving_productInfo(data)();
  console.log(result);
  if (result.newRowId) {
    alert("Product Inserted Successfully😊👍");
  } else {
    alert("Failed To Add Product😓😭");
  }
  $("#Pname").val("");
  $("#Prate").val("");
  $("#tax").val("");
}

async function addBasePrice() {
  //product.html
  let v1 = document.getElementById("basePriceTitle");
  let basePriceTitle = $("#basePriceTitle").val().trim();
  if (!basePriceTitle) {
    alert("Please enter Title!");
    return;
  }
  let result = await eel.saving_base_price(basePriceTitle)();
  if (result.newRowId) {
    alert("DONE 😊👍");
  } else {
    alert("Duplicate entry not allowed!");
  }
}


async function addCustomer() {
  let name = $("#name").val().trim(),
    bp = $("#base_price").val();

  if (!name) {
    alert("Customer name cannot be blank!");
    return;
  }

  let data = { name: name, base_price: bp };

  let result = await eel.saving_customer_info(data)();

  if (result["newRowId"]) {
    console.log(result);
    alert("Saved successfully😊👍");
  } else {
    alert("Failed to save customer😓😭");
  }
}

async function addProductPriceListWise() {

  let rate = $("#rate").val();
  let price_list_id = $("#base_price").val();
  let product_id = $("#product").val();


  let data = {
    'rate': rate,
    'price_list_id': price_list_id,
    'product_id': product_id
  };

  result = await eel.saving_product_price_list_wise(data)()

  if (result['id']) {
    console.log(result)
    alert("Added To Price List Successfully😊👍")
  }
  else {
    alert("Failed To Add To Price List😓😭");
  }
}

function addOrder(){
  
}

async function loadBasepriceScreenData() {
  let result = await eel.load_baseprice_screen_data()();
  console.log(result);

  let basePriceOptions = ['<option value="">-Base Price-</option>'];

  let bp = result["bp_list"];
  bp.forEach((item) => {
    basePriceOptions.push(`<option value="${item.name}">${item.name}</option>`);
  });

  $("#base_price").html(basePriceOptions.join(""));
}
async function loadProductScreenData() {
  let result = await eel.load_product_screen_data()();
  console.log(result);

  let productOptions = ['<option value="">-Product-</option>'];


  result.forEach((item) => {
    productOptions.push(`<option value="${item.name}">${item.name}</option>`);
  });

  $("#product").html(productOptions.join(""));
}
async function loadCustomerScreenData(){
  let result = await eel.load_customer_screen_data()();

  let customerOptions = ['<option value = "">-Customer-</option>']
 
  result.forEach((item) => {
    customerOptions.push(`<option value = "${item.name}">${item.name}</option>`)
  });

  $("#customer").html(customerOptions.join(""))
  console.log(result)
}