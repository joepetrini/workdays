var sm,sd,sy,sUrl;
var months = new Array('January','February','March','April','May','June','July','August','September','October','November','December');
var url_months = new Array('jan','feb','mar','apr','may','jun','jul','jul','aug','sep','oct','nov','dec');

function setTimezone(){
    alert($('#timezone').val());
}

function checkDone(){
    // Check if all month,day,year are all selected, if so redir
    if (sm != undefined && sy != undefined && sd != undefined){
        sUrl = url_months[d.getMonth()]+'/'+_z(d.getDate(),2)+'/'+sy
        window.location = '/'+sUrl
    }
}

function setYear(y){
    $('#year').val(y);
}

function setMonth(m){
    m = months.indexOf(m);
    m = url_months[m];
    $('#month').val(m);
}

function setDay(d){
    $('#day').val(_z(d.trim(),2));
}


function _z(num,count){
    var numZeropad = num + '';
    while(numZeropad.length < count) {
        numZeropad = "0" + numZeropad;
    }
    return numZeropad;
}