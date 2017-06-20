window.onload = function() {
    $('.menu .item').tab()

    $('.bed-image-block').dimmer({on: 'hover'});

    $('.login-button, .register-button').click(function() {
        $('.ui.modal').modal('show');
    })    

    // Search dates
    $('#rangestart').calendar({
        type: 'date',
        multiMonth: 1,
        endCalendar: $('#rangeen')
    });
    $('#rangeend').calendar({
        type: 'date',
        multiMonth: 1,
        startCalendar: $('#rangestart')
    });

    // Add date
    $('#startdate').calendar({
        type: 'date',
        multiMonth: 1,
        endCalendar: $('#startdate')
    });
}

function showSingleBed(id) {
    $('#' + id).modal('show');
}

function scrollToContent() {
    document.getElementById('page_content').scrollIntoView();
}


function getBeds() {
    var check_in = formatDate(document.querySelector('#check_in_renter').value)
    var check_out = formatDate(document.querySelector('#check_out_renter').value)
    var url = "/get_beds" + '/' + check_in + '/' + check_out
    $.ajax({url: url, success: function(result){
        $("#beds-container").html(result);
        $('.bed-image-block').dimmer({
            on: 'hover'
        });
    }});
};


function formatDate(date) {
    var months = {
        January:'01'    ,
        February:'02'   ,
        Merch:'03'  ,
        April:'04'  ,
        May:'05'    ,
        June:'06'   ,
        July:'07'   ,
        August:'08' ,
        September:'09'  ,
        October:'10'    ,
        Novenber:'11'   ,
        December:'12'
    };
    var dateArray = date.replace(',', '').split(' ')
    var month = months[dateArray[0]]
    var day = dateArray[1].length < 2 ? '0' + dateArray[1] : dateArray[1];
    var year = dateArray[2]
    return day + '-' + month + '-' + year;
}


function getAvailability() {
    var check_in = formatDate(document.querySelector('#check_in_owner').value)
    var url = "/add_availabilities" + '/' + check_in
    $.ajax({
        url: url,
        success: function(result){
            $("#availabilities_status").show();
            $("#availabilities_status").html('מיטתך הוצאה להשכרה בתאריך: ' + check_in);
        },
        error: function(result) {
            $("#availabilities_status").show();
            $("#availabilities_status").html('אין אפשרות להשכיר את המיטה');
        }
    });
};


function rentRoom(id, bed_id) {
    var has_rented = 'rented'
    var selector = '#AA' + id
    id = id.replace('_', '-')
    id = id.replace('_', '-')
    var check_in = document.querySelector(selector).value
    var url = "/rent_room/" + bed_id + '/' + id
    $.ajax({url: url, success: function(result){
        $(selector).addClass('rented');
    }});
};