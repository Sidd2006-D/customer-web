
function prepareOrderTr(d) {
  return `<tr id="${d.id}" style="cursor: pointer;"  onclick="viewOrderDetails(this.id)">
  <td style="text-align: right;">${d.id}</td> 
  <td style="text-align: right;">${d.date}</td> 
  <td style="text-align: left;">${d.customer_name}</td> 
  <td style="text-align: left;">${d.base_price}</td> 
  <td style="text-align: right;">${d.product_count}</td> 
  <td style="text-align: right;">₹ ${d.sub_total}</td> 
  <td style="text-align: right;">₹ ${d.tax_amount}</td> 
  <td style="text-align: right;">₹   ${d.grand_total}</td> 
  </tr>`;
}
async function loadOrderGridAllrow() {
  let result = await eel.load_order_grid_all_rows()();
  console.log(result);
  let trArray = [];
  result.forEach(function (d) {
    trArray.push(prepareOrderTr(d));
  });
  $("#order_grid_report").html(trArray.join(""));
}

function viewOrderDetails(id) {
  window.open("/orderDeatails.html?id=" + id);

  // script.js
}
var orderDetails;
async function loadOrderDetails() {
  const urlParams = new URLSearchParams(window.location.search);
  const id = urlParams.get("id");
  orderDetails = await eel.get_order_details_by_id(parseInt(id))();
  console.log(orderDetails);

  let trArray = [];
  orderDetails.order_items.forEach(function (d) {
    trArray.push(prepareOrderDetailsTr(d, trArray.length));
  });
  $("#order_details_tbody").html(trArray.join(""));
  $('#customer_name').html(orderDetails.customer_name);
  $('#base_price').html(orderDetails.base_price);
  $('#sub_total').html('₹ ' + orderDetails.sub_total);
  $('#tax_amount').html( '₹ ' + orderDetails.tax_amount);
  $('#grand_total').html('₹ ' + orderDetails.grand_total);
  // "date": obj.date.strftime("%d-%m-%Y"),  
  // "created_on": obj.created_on.strftime("%d-%m-%Y %H:%M:%S"),  
  // "customer_name": obj.customer_name, 
  // "base_price": obj.base_price,
  // "product_count": obj.product_count,
  // "tax_amount": obj.tax_amount,
  // "sub_total": obj.sub_total,
  // "grand_total": obj.grand_total,
}
function prepareOrderDetailsTr(d, index) {
  return `<tr id="${d.id}" style="cursor: pointer;"  ">
          <td style="text-align: right;">${index + 1}</td> 
          <td style="text-align: left;">${d.product_name}</td> 
          <td style="text-align: right;">₹ ${parseFloat(d.rate).toFixed(2)}</td> 
          <td style="text-align: right;">${d.quantity}</td> 
          <td style="text-align: right;"> ${d.tax_rate}</td> 
          <td style="text-align: right;">₹ ${d.tax_amount}</td> 
          <td style="text-align: right;">₹ ${d.line_total}</td> 
        </tr>`;
}
var cssPrint = `
<style> 
* {
    -webkit-print-color-adjust: exact !important;   /* Chrome, Safari */
    color-adjust: exact !important;                 /*Firefox*/
}
@media print { body {margin: 0; margin-right: 2;} footer {page-break-after: always;} header { visibility: hidden } }');
@page { page-break-after: always; } .bold{font-size: 15px;color: rgb(0,0,0); font-weight: bold;}
tbody{ font-size: 11px; }
.t-r{ text-align: right; } .t-l{ text-align: left; } .t-c{ text-align: center; }');
table {
  width: 100%;
  border-collapse: collapse;           /* merge borders */
}
table, th, td {
  border: 1px solid #ccc;
}
th, td {
  padding: 8px 12px;
  text-align: left;
}
th {
  background: #f7f7f7;
}

</style>
`;
var jsPrint = `
<script type="text/javascript"> 
  var imgs = document.images, len = imgs.length, counter = 0; 
  if(len==0){
    window.print(); 
    window.close();
  } else {
  [].forEach.call( imgs, function( img ) { 
    img.addEventListener( "load", incrementCounter, false ); 
  });
   
  function incrementCounter() { 
    counter++; 
    if ( counter === len ) { 
      window.print(); 
      //window.close(); 
    }
  } 
  }
</script>
`;
function printOrder() {
  orderDetails


  var mywindow = window.open('', 'my div', 'height=842,width=595');
  mywindow.document.write(`<html><head><title>Order# ${orderDetails.id}</title>`);
  mywindow.document.write('<style>');
  mywindow.document.write(cssPrint);
  mywindow.document.write('</style>');
  mywindow.document.write('</head><body><div class="col-lg-12">');
  let trArray = [];
  orderDetails.order_items.forEach(function (d) {
    trArray.push(prepareOrderDetailsTr(d, trArray.length));
  });
  mywindow.document.write(`<table style="width: 100%;">
    <thead>
      <tr>
        <th>#</th>
        <th style="text-align: left;">Product Name</th>
        <th style="text-align: right;">Rate</th>
        <th style="text-align: right;">Qty</th>
        <th style="text-align: right;">Tax%</th>
        <th style="text-align: right;">Tax Amount</th>
        <th style="text-align: right;">Total</th>
      </tr>
    </thead>
    <tbody>
    ${trArray.join('')}
    </tbody>
    </table>`);
  mywindow.document.write('</div>');
  mywindow.document.write(jsPrint);
  mywindow.document.write('</body></html>');
  mywindow.document.close(); // necessary for IE >= 10
  mywindow.focus(); // necessary for IE >= 10
  mywindow.print();
  mywindow.close();
}