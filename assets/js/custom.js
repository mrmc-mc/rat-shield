//  Up Down Buttom for amount input
$("input[name='amount']").TouchSpin({
        min: 0.001,
        max: 1e9,
        boostat: 20,
        buttondown_class: "btn btn-primary",
        buttonup_class: "btn btn-primary",
});
