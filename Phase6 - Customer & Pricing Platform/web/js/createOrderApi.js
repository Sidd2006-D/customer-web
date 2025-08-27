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
      id: 0,
      name: "",
      rate: parseInt("0"),
      taxRate: parseInt("0"),
    };
  }
};
createOrderApi.basePriceSetter = function (selectElm) {
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
  $("#loader").addClass("loading");
  $("#loader_msg").html("Loading Master Data...");
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
      `<option value = "${map.id}" data-name="${map.name}"  data-rate="${map.rate}" data-tax_rate="${map.taxRate}">${map.name}</option>`
    );
    createOrderApi.basePriceNameIdMap[map.name] = map.id;
  });
  $("#product").html(htmlArray.join(""));
  htmlArray = [];
  result = null;
  $("#loader").removeClass("loading");
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
  //TODO render in table.
};
