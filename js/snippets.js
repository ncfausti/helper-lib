var printProgress = function(percentComplete) {var total = 100; for(i = 0; i < total;i++){ if(i <= percentComplete*total) {document.write("+");} else { document.write("="); } }}
