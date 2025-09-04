// addOrder(){

// }

var createOrderApi = {};
createOrderApi.productWisePriceMasterList = [];
createOrderApi.basePriceNameIdMap = {};
createOrderApi.selectedCustomerRates = {};
createOrderApi.selectedProduct = null;
createOrderApi.selectedCustomerID = "";
createOrderApi.selectedBasePrice = "";
createOrderApi.prepareCustomerRate = function () {
  createOrderApi.selectedCustomerRates = {};
  let selectBasePriceId =
    createOrderApi.basePriceNameIdMap[createOrderApi.selectedBasePrice];
  createOrderApi.productWisePriceMasterList.forEach(function (map) {
    if (selectBasePriceId == map.basePriceId) {
      createOrderApi.selectedCustomerRates[map.productId] = map.rate;
    }
  });
  console.log("Rates", createOrderApi.selectedCustomerRates);
};
createOrderApi.customerSetter = function (selectElm) {
  $("#order_grid").html("");
  console.log(selectElm.selectedOptions[0].dataset);
  console.log(selectElm.selectedOptions[0].value);

  createOrderApi.selectedBasePrice =
    selectElm.selectedOptions[0].dataset.base_price;
  createOrderApi.selectedCustomerID = selectElm.selectedOptions[0].value;
  createOrderApi.selectedCustomerRates = {};
  $("#base_price").val(createOrderApi.selectedBasePrice);
  if (!createOrderApi.selectedCustomerID) return;
  if (!createOrderApi.selectedBasePrice) return;
  createOrderApi.prepareCustomerRate();
};
createOrderApi.productSetter = function (selectElm) {
  createOrderApi.selectedProduct = null;
  if (selectElm.selectedOptions[0].value) {
    let productId = selectElm.selectedOptions[0].value;
    console.log(selectElm.selectedOptions[0].dataset);
    createOrderApi.selectedProduct = {
      id: productId,
      name: selectElm.selectedOptions[0].dataset.name,
      taxRate: parseInt(selectElm.selectedOptions[0].dataset.tax_rate),
    };
  }
};
createOrderApi.basePriceSetter = function (selectElm) {
  $("#order_grid").html("");
  createOrderApi.selectedCustomerRates = {};
  if (!createOrderApi.selectedCustomerID) {
    createOrderApi.selectedBasePrice = "";
    $("#base_price").val("");
    return;
  }
  createOrderApi.selectedBasePrice = selectElm.selectedOptions[0].value;
  if (!createOrderApi.selectedBasePrice) return;
  createOrderApi.prepareCustomerRate();
};

createOrderApi.loadMasterForCreateNewOrder = async function () {
  $("#loadMasterDom").removeClass("loading");
  // $("#loader").addClass("loading");
  // $("#loader_msg").html("Loading Master Data...");
  createOrderApi.basePriceNameIdMap = {};
  createOrderApi.customerRates = {};
  let result = await eel.load_master_for_order_cretaion()();
  console.log(result);
  createOrderApi.productWisePriceMasterList = result.productWisePriceMasterList;
  let htmlArray = ['<option value ="" data-base_price="">-Select-</option>'];
  //map={"id": 1, "name": "", "basePrice":""}
  result.customerMasterList.forEach(function (map) {
    htmlArray.push(
      `<option value = "${map.id}" data-base_price="${map.basePrice}">${map.name}</option>`
    );
  });
  $("#customer").html(htmlArray.join(""));
  htmlArray = ['<option value ="">-Select-</option>'];
  result.basePriceMasterList.forEach(function (map) {
    htmlArray.push(
      `<option value = "${map.name}" data-id="${map.id}">${map.name}</option>`
    );
    createOrderApi.basePriceNameIdMap[map.name] = `${map.id}`;
  });
  $("#base_price").html(htmlArray.join(""));
  console.log(createOrderApi.basePriceNameIdMap);
  htmlArray = ['<option value ="">-Select-</option>'];
  result.productMasterList.forEach(function (map) {
    htmlArray.push(
      `<option value = "${map.id}" data-name="${map.name}" data-tax_rate="${map.taxRate}">${map.name}</option>`
    );
    createOrderApi.basePriceNameIdMap[map.name] = map.id;
  });
  $("#product").html(htmlArray.join(""));
  htmlArray = [];
  result = null;
  $("#loader").removeClass("loading");
};

createOrderApi.editQty = function (input) {
  console.log(input.valueAsNumber);
  let tdArray = input.parentNode.parentNode.children;
  if (input.valueAsNumber < 1) {
    tdArray[4].innerText = 0;
  } else {
    let subtotal = parseInt(tdArray[2].innerText) * input.valueAsNumber;
    let taxAmount = subtotal * (parseInt(tdArray[3].innerText) / 100);
    tdArray[4].innerText = (subtotal + taxAmount).toFixed(2);
  }
};
createOrderApi.addProduct = function () {
  if (!createOrderApi.selectedCustomerID) return;
  if (!createOrderApi.selectedProduct) return;
  if (
    createOrderApi.selectedProduct.id in createOrderApi.selectedCustomerRates
  ) {
    createOrderApi.selectedProduct.rate =
      createOrderApi.selectedCustomerRates[createOrderApi.selectedProduct.id];
  }
  // let productSelect = $("#product")[0];
  // let selectedOption = productSelect.selectedOptions[0];
  // if (!selectedOption || !selectedOption.value) return;
  let existingProductRow = $("#order_grid").find(
    `tr#${createOrderApi.selectedProduct.id}`
  );
  if (existingProductRow.length) {
    alert("Product already added!");
    return;
  }
  let quantity = parseInt($("#quantity").val()),
    dateTime = new Date().toLocaleString();
  let subtotal = createOrderApi.selectedProduct.rate * quantity;
  let tax = subtotal * (createOrderApi.selectedProduct.taxRate / 100);
  let total = (subtotal + tax).toFixed(2);
  // let total = (createOrderApi.selectedProduct.rate * quantity * (1 + createOrderApi.selectedProduct.taxRate / 100)).toFixed(2);

  let rowHtml = `
    <tr id="${createOrderApi.selectedProduct.id}"> 
      <td>${createOrderApi.selectedProduct.name}</td>
      <td><input type="number" value="${quantity}" onchange="createOrderApi.editQty(this)" min="0" style="width: 60px; height: 30px;"></td>
      <td>${createOrderApi.selectedProduct.rate}</td>
      <td>${createOrderApi.selectedProduct.taxRate}</td>
      <td>${total}</td>
      <td>${dateTime}</td>
    </tr>
  `;
  $("#order_grid").append(rowHtml);
};

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

createOrderApi.saveOrder = async function () {
  if (!createOrderApi.selectedCustomerID) {
    alert("Select Customer");
    return;
  }
  let itemList = [];
  $("#order_grid tr").each(function () {
    let trChildsTdElementArray = this.children;
    if (trChildsTdElementArray[1].children[0].valueAsNumber) {
      // trChildsTdElementArray[0].innerText;
      // trChildsTdElementArray[1].children[0].valueAsNumber;
      // trChildsTdElementArray[2].innerText;
      // trChildsTdElementArray[3].innerText;
      // trChildsTdElementArray[4].innerText;
      let lineItem = {
        id: parseInt(this.id), //$(this).attr("id"),
        name: trChildsTdElementArray[0].innerText,
        qty: parseInt(trChildsTdElementArray[1].children[0].valueAsNumber),
        rate: parseFloat(trChildsTdElementArray[2].innerText),
        tax_rate: parseFloat(trChildsTdElementArray[3].innerText),
        total: parseFloat(trChildsTdElementArray[4].innerText),
      };
      itemList.push(lineItem);
    }
  });
  if (!itemList.length) {
    alert("Add Product 1st");
    return;
  }
  if (
    !confirm(`Are you sure to create order with ${itemList.length} product?`)
  ) {
    return;
  }
  console.log("itemList", itemList);
  result = await eel.create_new_order({
    selectedBasePrice: createOrderApi.selectedBasePrice,
    item_list: itemList,
    customer_id: parseInt(createOrderApi.selectedCustomerID),
  })();
  console.log(result);
  if (result["newOrderid"]) {
    alert("Order Submitted successfully😊👍");
  } else {
    alert("Something went wrong!");
  }
  /*
  $("#order_grid tr").each(function () {

    if ($(this).find("th").length) return;

    let $tds = $(this).find("td");


    let row = {
      id: $(this).attr("id"),
      name: $tds.eq(0).text(),
      qty: parseInt($tds.eq(1).text()),
      rate: parseFloat($tds.eq(2).text()),
      tax_rate: parseFloat($tds.eq(3).text()),
      total: parseFloat($tds.eq(4).text()),
    };
    itemList.push(row);
  });
  */
};

var demoOrderItems = {
  101: [
    { id: 1, name: "Colgate", rate: 100, qty: 2, tax_rate: 13, total: 226 },
    { id: 2, name: "Cola", rate: 50, qty: 1, tax_rate: 10, total: 55 },
  ],
  102: [
    { id: 1, name: "Soap", rate: 40, qty: 3, tax_rate: 5, total: 126 },
    { id: 2, name: "Shampoo", rate: 80, qty: 1, tax_rate: 12, total: 89.6 },
  ],
};


function showOrderItems(orderId) {
  var items = demoOrderItems[orderId];
  var rows = [];
  if (items.length === 0) {
    rows.push(
      '<tr><td colspan="6" style="color:#aaa;">No items for this order.</td></tr>'
    );
  } else {
    $.each(items, function (i, item) {
      rows.push(
        `<tr>
          <td>${item.id}</td>
          <td>${item.name}</td>
          <td>${item.rate}</td>
          <td>${item.qty}</td>
          <td>${item.tax_rate}</td>
          <td>${item.total}</td>
        </tr>`
      );
    });
  }
  $("#order_items_tbody").html(rows.join(""));
  $("#order_grid_wrapper").hide();
  $("#order_items_wrapper").show();
}


function goBackToOrdersGrid() {
  $("#order_items_wrapper").hide();
  $("#order_grid_wrapper").show();
}


