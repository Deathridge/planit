var thisScreenWidth = 0, thisScreenHeight = 0;
function viewScreenSize() {
    if (typeof (window.innerWidth) === 'number') {
        //Non-IE
        thisScreenWidth = window.innerWidth;
        thisScreenHeight = window.innerHeight;
    } else if (document.documentElement && (document.documentElement.clientWidth || document.documentElement.clientHeight)) {
        //IE 6+ in 'standards compliant mode'
        thisScreenWidth = document.documentElement.clientWidth;
        thisScreenHeight = document.documentElement.clientHeight;
    } else if (document.body && (document.body.clientWidth || document.body.clientHeight)) {
        //IE 4 compatible
        thisScreenWidth = document.body.clientWidth;
        thisScreenHeight = document.body.clientHeight;
        screenWidth = thisScreenWidth;
    }
    // screenSize = div in page footer  
    $("#screenSize").html(thisScreenWidth + "x" + thisScreenHeight);
}