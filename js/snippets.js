var printProgress = function(percentComplete) {var total = 100; for(i = 0; i < total;i++){ if(i <= percentComplete*total) {document.write("+");} else { document.write("="); } }}

// String.format
// usage 
//'Your balance is {0} USD'.f(77.7) 
// 'Added {0} by {1} to your collection'.f(title, artist)
//
String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};