var sm,sd,sy,sUrl;
var url_months = new Array('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');

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
    $('div.year').removeClass('selected');
    $('#year-'+y).addClass('selected');    
    $('#year').html(y);
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
    $('#days').show();
    var monthNum = url_months.indexOf(monthName);
    var monthAbbr = url_months[monthNum];
    $('#month').html(monthAbbr);
    
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

    // Scroll them to the calendar picker
    $("html, body").animate({ scrollTop: $(document).height() }, 1000);
}

function setDay(d){
    $('#day').html(_z(d.trim(),2));
    // Redirect
    window.location = '/'+(url_months.indexOf($('#month').html())+1)+'/'+$('#day').html()+'/'+$('#year').html();
}


function _z(num,count){
    var numZeropad = num + '';
    while(numZeropad.length < count) {
        numZeropad = "0" + numZeropad;
    }
    return numZeropad;
}