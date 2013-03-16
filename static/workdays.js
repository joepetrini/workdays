var sm,sd,sy,sUrl;
var months = new Array('January','February','March','April','May','June','July','August','September','October','November','December');
var url_months = new Array('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec');

function setTimezone(){
    var timezone =  String($('#timezone option:selected').val());
    timezone = timezone.replace('/','-');
    $.get('/set-tz/'+timezone, function(data) {
        // If m/d/y page, refresh
    });
}

function init(m){
    $('#month').val(url_months[m-1]);
}

function checkDone(){
    // Check if all month,day,year are all selected, if so redir
    if (sm !== undefined && sy !== undefined && sd !== undefined){
        sUrl = url_months[d.getMonth()]+'/'+_z(d.getDate(),2)+'/'+sy;
        window.location = '/'+sUrl;
    }
}

function setYear(y){
    $('#year').val(y);
}

function daysInMonth(year,month){
    month = (month==12) ? 0 : month + 1;
    var lastDayOfMonth = new Date(year,month,0);
    return lastDayOfMonth.getDate();
}

/*
 * Called when user selects month.  Need to fill in text box and rebuild days in month table
*/
function setMonth(monthName){
    var monthNum = months.indexOf(monthName);
    var monthAbbr = url_months[monthNum];
    $('#month').val(monthAbbr);
    
    // TODO: Rebuild month table
    var yearSelected = $('#year').val();
    var firstDayOfMonth = new Date(yearSelected,monthNum,1);
    firstDayOfMonth = firstDayOfMonth.getDay();
    var tableContent = '<tr>';

    // Pad weekdays before start of month
    for (i=0;i<firstDayOfMonth;i++) {tableContent += '<td></td>';}

    // Fill in month days
    var totalDays = daysInMonth(yearSelected,monthNum);
    for (i=1;i<=totalDays;i++){
        if (i>1 && (i-1+firstDayOfMonth)%7===0) { tableContent+='<tr>'; }
        tableContent += '<td><div class="day picker">'+i+'</div></td>';
        if ((i-1+firstDayOfMonth)%7==6) { tableContent+='</tr>'; }
    }
    // Add closing tr tag if month doesn't end on sat
    if (!/tr>$/.test(tableContent)){tableContent+='</tr>';}

    // Replace table and reattach click event to days
    $('#cal tbody').html(tableContent);
    $('div.day').click(function() { 
        setDay($(this).html());}
    );

    // Set selected css to month
    $('div.month').removeClass('selected');
    $('#month-'+monthName).addClass('selected');
}

function setDay(d){
    $('#day').val(_z(d.trim(),2));
    // Redirect
    window.location = '/'+(url_months.indexOf($('#month').val())+1)+'/'+$('#day').val()+'/'+$('#year').val();
}


function _z(num,count){
    var numZeropad = num + '';
    while(numZeropad.length < count) {
        numZeropad = "0" + numZeropad;
    }
    return numZeropad;
}