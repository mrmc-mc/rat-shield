function swap(selectList1,selectList2){
    var temp = document.getElementById('selectList1').value;
	var temp1 = document.getElementById('selectList2').value;
    document.getElementById('selectList1').value = temp1;
	document.getElementById('selectList2').value = temp;
}
	
function calculate(){
	var selectList1 = document.getElementById('selectList1');
	var selectList2 = document.getElementById('selectList2');
	
	if (selectList1.value === "irt" && selectList2.value === "irt") {
      rate = 1;
      label1 = 'تومان';
      label2= 'تومان';
    }
    if (selectList1.value === "irt" && selectList2.value === "psv") {
      rate = 0.88;
      label1 = 'تومان';
      label2 = 'پریمیوم ووچر';
    }
    if (selectList1.value === "psv" && selectList2.value === "psv") {
      rate = 1.;
    }
    if (selectList1.value === "psv" && selectList2.value === "irt") {
      rate = 0.69;
    }
    if (selectList1.value === "USD" && selectList2.value === "JPY") {
      rate = 108.96;
    }
    if (selectList1.value === "USD" && selectList2.value === "ALL") {
      rate = 109.7;
    }
    if (selectList1.value === "USD" && selectList2.value === "DZD") {
      rate = 118.6;
    }
	
	
	var amount = document.getElementById('amount').value;
	if(amount>0) { } else { amount=1 }
	var converted = parseFloat(amount) * parseFloat(rate);
	
	converted = converted.toFixed(2);
	document.getElementById('finalamount').innerHTML = amount + selectList1.value + ' * ' + rate + ' Exchange = ' + converted + selectList2.value;
	document.getElementById('finalamount2').innerHTML ='قیمت هر واحد ' + label2 + '  = ' +rate + ' ' + label1;
}