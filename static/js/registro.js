var page=1, total_pages=11;

function showButton(id,btnClass){
	var obj = $("#"+id);
	obj.attr("class","show "+btnClass);
}

function hideButton(id,btnClass){
	var obj = $("#"+id);
	obj.attr("class","hide "+btnClass);
}

function showPanel(id){
	var obj = $("#"+id);
	obj.attr("class","show panel panel-default");
}

function hidePanel(id){
	var obj = $("#"+id);
	obj.attr("class","hide panel panel-default");
}

function nextPanel(){
	hidePanel("panel"+page);
	page++;
	showPanel("panel"+page);
	showButton("btn_previous","previous");
	setProgressBar(Math.round((page-1)*100/total_pages));
	if(page==total_pages){
		hideButton("btn_next","next");
	}	
}

function previousPanel(){
	hidePanel("panel"+page);
	page--;
	showPanel("panel"+page);
	showButton("btn_next","next");
	setProgressBar(Math.round((page-1)*100/total_pages));
	if(page==1){
		hideButton("btn_previous","previous");
		//setProgressBar();
		setProgressBar(0);
	}
}

function setPanelVisible(id){
	var i;	
	for(i=1; i<=total_pages; i++){
		if(i==id){
			var panel = $("#panel"+i);
			panel.attr("class","show panel panel-default");
		} else {
			var panel = $("#panel"+i);
			panel.attr("class","hide panel panel-default");
		}
	}
	for(i=1; i<=total_pages; i++){
		if(i==id){
			var nav_i = $("#nav"+i);
			nav_i.attr("class","current");
		} else {
			var nav_i = $("#nav"+i);
			nav_i.attr("class","");
		}
	}
}



$(function() {

  	/* Creamos un widget de calendario con jquery-ui */
    $( ".datepicker" ).datepicker({
		changeMonth: true,
		changeYear: true,
		yearRange: "1950:2012",
		// Podemos poner mas opciones
    });

    //ocultamos los campos que no son necesarios a menos que se realice una eleccion 
    $('[oculto=oculto]').parent().hide();
    //$('#id_descripcion_otros').parent().hide();
    //$('#id_descripcion_pregunta_4').parent().hide();

    /*	Si ha seleccionado la opcion de otros, entonces mostramos un casillero adicional
     que permite describir de forma especifica la opcion "otros" */
    $('select[name=descripcion_pregunta_2]').change(function() { 
    	if ($(this).val() == 'otros'){
    		$('#id_descripcion_otros_2').parent().show();
    		$('#id_descripcion_otros_2').val("Especifique")
    		//console.log('mostrar casilla de otros');
    	}else{
    		$('#id_descripcion_otros_2').parent().hide();
    	}	
    });

    $('#id_descripcion_pregunta_3').on('change', function() {
   		valor_si_no = $('input[name=descripcion_pregunta_3]:checked', '#id_descripcion_pregunta_3').val(); 
   		if (valor_si_no == 'si'){
   			$('#id_descripcion_pregunta_4').parent().show();
   		}else{
   			$('#id_descripcion_pregunta_4').parent().hide();
   		}
	});

    $('input[name=descripcion_pregunta_5').on('click', function(e){
    	if(e.target.value == "rehabilitacion_fisica"){
    		if (e.target.checked)
    			$('#id_descripcion_tiempo_rehab_fisica').parent().show();
    		else
    			$('#id_descripcion_tiempo_rehab_fisica').parent().hide();
    	}else if(e.target.value == "estimulacion_temprana"){
    		if (e.target.checked)
    			$('#id_descripcion_tiempo_estimu_temprana').parent().show();
    		else
    			$('#id_descripcion_tiempo_estimu_temprana').parent().hide();
    	}
    });

    $('input[name=descripcion_pregunta_6]').on('click',function(e) { 
    	if (e.target.value == 'otro'){
    		if (e.target.checked){
    			$('#id_descripcion_otros_6').parent().show();
    			$('#id_descripcion_otros_6').val("Especifique")
    		}else
    			$('#id_descripcion_otros_6').parent().hide();
    		//console.log('mostrar casilla de otros');
    	}
    });

    $('select[name=descripcion_pregunta_8]').change(function() { 
    	if ($(this).val() == 'si'){
    		$('#id_descripcion_pregunta_8_1').parent().show();
    		$('#id_descripcion_pregunta_8_2').parent().show();
    		$('#id_descripcion_pregunta_8_3').parent().show();
    		$('#id_descripcion_pregunta_8_4').parent().show();
    		//console.log('mostrar casilla de otros');
    	}else{
    		$('#id_descripcion_pregunta_8_1').parent().hide();
    		$('#id_descripcion_pregunta_8_2').parent().hide();
    		$('#id_descripcion_pregunta_8_3').parent().hide();
    		$('#id_descripcion_pregunta_8_4').parent().hide();
    	}	
    });

	$('input[type=text], [type=number]').addClass('form-control');
	$('input[name=numero_hermanos]').change(function(e){
		if(e.target.value != "0")
			$("#hermanos-formset").show();
		else
			$("#hermanos-formset").hide();
	});

	$('input[name=suplementos]').change(function(e){
		if(e.target.value == "si")
			$("#suplementos-formset").show();
		else
			$("#suplementos-formset").hide();
	});

});
