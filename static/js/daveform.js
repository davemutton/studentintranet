//jQuery time
$("#firstnext").click(function(){
	var a1 = $('input[name="subject"]:checked').length > 0;
	var a2 = $('input[name="level"]:checked').length > 0;
	var a3 = $('input[name="pathway"]:checked').length > 0;
	var a4 = $('input[name="agebracket"]:checked').length > 0;
	if (a1 == true && a2 == true && a3 == true &&  a4 == true ){
	$("#firstsection").css({'visibility':'hidden','display':'none'}); 
	$("#secondsection").css({'visibility':'visible','display':'block'}); 
} 
});



$("#firstprevious").click(function(){

	$("#firstsection").css({'visibility':'visible','display':'block'}); 
	$("#secondsection").css({'visibility':'hidden','display':'none'}); 
});

$("#secondprevious").click(function(){

	$("#secondsection").css({'visibility':'visible','display':'block'}); 
	$("#thirdsection").css({'visibility':'hidden','display':'none'}); 
});

id_description

$("#secondnext").click(function(){
	var b1 = $(".as-selection-item").length > 0;
	var b2 = $('textarea[name="description"]').val().length > 10;
if (b1 == true && b2 == true ){
	$("#secondsection").css({'visibility':'hidden','display':'none'}); 
	$("#thirdsection").css({'visibility':'visible','display':'block'}); 
}
});