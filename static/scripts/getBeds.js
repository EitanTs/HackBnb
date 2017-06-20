$("find_beds").click(get_beds())

function get_beds() {
var check_in = document.querySelector('#check_in_renter').value
    var check_out = document.querySelector('#check_out_renter').value
    var url = "/get_beds" + '/' + check_in + '/' + check_out
    $.ajax({url: url, success: function(result){
        $("#beds-container").html(result);
    }});
};
