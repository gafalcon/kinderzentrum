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
    $('select[name=descripcion_paciente-descripcion_pregunta_2]').change(function() { 
    	if ($(this).val() == 'otros'){
    		$('#id_descripcion_paciente-descripcion_otros_2').parent().show();
    		$('#id_descripcion_paciente-descripcion_otros_2').val("Especifique");
    		//console.log('mostrar casilla de otros');
    	}else{
    		$('#id_descripcion_paciente-descripcion_otros_2').parent().hide();
    	}	
    });

    $('#id_descripcion_paciente-descripcion_pregunta_3').on('change', function() {
   		var valor_si_no = $('input[name=descripcion_paciente-descripcion_pregunta_3]:checked', '#id_descripcion_paciente-descripcion_pregunta_3').val(); 
		console.log(valor_si_no);
   		if (valor_si_no == 'True'){
   			$('#id_descripcion_paciente-descripcion_pregunta_4').parent().show();
   		}else{
   			$('#id_descripcion_paciente-descripcion_pregunta_4').parent().hide();
   		}
	});

    $('input[name=descripcion_paciente-descripcion_pregunta_5').on('click', function(e){
    	if(e.target.value == "rehabilitacion_fisica"){
    		if (e.target.checked)
    			$('#id_descripcion_paciente-descripcion_tiempo_rehab_fisica').parent().show();
    		else
    			$('#id_descripcion_paciente-descripcion_tiempo_rehab_fisica').parent().hide();
    	}else if(e.target.value == "estimulacion_temprana"){
    		if (e.target.checked)
    			$('#id_descripcion_paciente-descripcion_tiempo_estimu_temprana').parent().show();
    		else
    			$('#id_descripcion_paciente-descripcion_tiempo_estimu_temprana').parent().hide();
    	}
    });

    $('input[name=descripcion_paciente-descripcion_pregunta_6]').on('click',function(e) { 
    	if (e.target.value == 'otro'){
    		if (e.target.checked){
    			$('#id_descripcion_paciente-descripcion_otros_6').parent().show();
    			$('#id_descripcion_paciente-descripcion_otros_6').val("Especifique");
    		}else
    			$('#id_descripcion_paciente-descripcion_otros_6').parent().hide();
    		//console.log('mostrar casilla de otros');
    	}
    });

    $('select[name=descripcion_paciente-descripcion_pregunta_8]').change(function() { 
    	if ($(this).val() == 2){
    		$('#id_descripcion_paciente-descripcion_pregunta_8_1').parent().show();
    		$('#id_descripcion_paciente-descripcion_pregunta_8_2').parent().show();
    		$('#id_descripcion_paciente-descripcion_pregunta_8_3').parent().show();
    		$('#id_descripcion_paciente-descripcion_pregunta_8_4').parent().show();
    		//console.log('mostrar casilla de otros');
    	}else{
    		$('#id_descripcion_paciente-descripcion_pregunta_8_1').parent().hide();
    		$('#id_descripcion_paciente-descripcion_pregunta_8_2').parent().hide();
    		$('#id_descripcion_paciente-descripcion_pregunta_8_3').parent().hide();
    		$('#id_descripcion_paciente-descripcion_pregunta_8_4').parent().hide();
    	}	
    });

	$('input[type=text], [type=number]').addClass('form-control');
	function value_changed(bool_value,  element){
		if(bool_value)
			element.show();
		else
			element.hide();
	}

	var num_hermanos = $('input[name=familiares_otros-numero_hermanos]').val();
	value_changed(num_hermanos != "0" && num_hermanos != '',
				  $("#hermanos-formset"));
	value_changed(num_hermanos != "0" && num_hermanos != '',
				  $("#id_familiares_otros-transtorno_hermanos").parent());
	$('input[name=familiares_otros-numero_hermanos]').change(function(e){
		value_changed(e.target.value != "0" && e.target.value != '', $("#hermanos-formset"));
		value_changed(e.target.value != "0" && e.target.value != '', $("#id_familiares_otros-transtorno_hermanos").parent());
	});

	value_changed($('input:radio[name=alimentacion-suplementos]:checked').val() == "True", $("#suplementos-formset"));
	$('input[name=alimentacion-suplementos]').change(function(e){
		value_changed(e.target.value == "True", $("#suplementos-formset"));
	});

	value_changed($('input:radio[name=recien_nacido-hubo_apego_precoz]:checked').val() == "True", $("#id_recien_nacido-tiempo_apego_precoz").parent());
	$('input:radio[name=recien_nacido-hubo_apego_precoz]').change(function(e){
		value_changed(e.target.value == "True", $("#id_recien_nacido-tiempo_apego_precoz").parent());
	});
	value_changed($('input:radio[name=recien_nacido-permanecio_internado]:checked').val() == "True", $("#id_recien_nacido-tiempo_internado").parent());
	value_changed($('input:radio[name=recien_nacido-permanecio_internado]:checked').val() == "True", $("#id_recien_nacido-tipo_contacto").parent());
	$('input:radio[name=recien_nacido-permanecio_internado]').change(function(e){
		value_changed(e.target.value == "True", $("#id_recien_nacido-tiempo_internado").parent());
		value_changed(e.target.value == "True", $("#id_recien_nacido-tipo_contacto").parent());
	});
	value_changed($("#id_recien_nacido-complicaciones_nacimiento_5").is(":checked"), $("#otra-complicacion"));
	$('input[name=recien_nacido-complicaciones_nacimiento]').change(function(e){
		value_changed($("#id_recien_nacido-complicaciones_nacimiento_5").is(":checked"), $("#otra-complicacion"));
	});

	value_changed($("#id_primeros_dias-situaciones_despues_nacimiento_4").is(":checked"), $("#id_primeros_dias-otra_situacion").parent());
	$('input[name=primeros_dias-situaciones_despues_nacimiento]').change(function(e){
		value_changed($("#id_primeros_dias-situaciones_despues_nacimiento_4").is(":checked"), $("#id_primeros_dias-otra_situacion").parent());
	});

	value_changed($("#id_primeros_dias-examenes_2").is(":checked"), $("#id_primeros_dias-otro_examen").parent());
	$('input[name=primeros_dias-examenes]').change(function(e){
		value_changed($("#id_primeros_dias-examenes_2").is(":checked"), $("#id_primeros_dias-otro_examen").parent());
	});

	value_changed($('input:radio[name=primeros_dias-clinica]:checked').val() == "True", $("#id_primeros_dias-clinica_permanencia").parent());
	value_changed($('input:radio[name=primeros_dias-clinica]:checked').val() == "True", $("#id_primeros_dias-dias_permanencia").parent());
	$('input:radio[name=primeros_dias-clinica]').change(function(e){
		value_changed(e.target.value == "True", $("#id_primeros_dias-clinica_permanencia").parent());
		value_changed(e.target.value == "True", $("#id_primeros_dias-dias_permanencia").parent());
	});
	value_changed($('input:radio[name=primeros_dias-icteria]:checked').val() == "True", $("#id_primeros_dias-tratamiento_icteria").parent());
	$('input:radio[name=primeros_dias-icteria]').change(function(e){
		value_changed(e.target.value == "True", $("#id_primeros_dias-tratamiento_icteria").parent());
	});
	value_changed($('input:radio[name=primeros_dias-dormia_toda_noche]:checked').val() == "False", $("#id_primeros_dias-veces_despertar_noche").parent());
	$('input:radio[name=primeros_dias-dormia_toda_noche]').change(function(e){
		value_changed(e.target.value == "False", $("#id_primeros_dias-veces_despertar_noche").parent());
	});
	value_changed($('input:radio[name=alimentacion-lactancia]:checked').val() == "True", $("#id_alimentacion-tiempo_leche_materna").parent());
	value_changed($('input:radio[name=alimentacion-lactancia]:checked').val() == "True", $("#id_alimentacion-motivo_suspencion_lactancia").parent());
	value_changed($('input:radio[name=alimentacion-lactancia]:checked').val() == "True", $("#id_alimentacion-otro_motivo_suspencion_lactancia"));
	$('input:radio[name=alimentacion-lactancia]').change(function(e){
		value_changed(e.target.value == "True", $("#id_alimentacion-tiempo_leche_materna").parent());
		value_changed(e.target.value == "True", $("#id_alimentacion-motivo_suspencion_lactancia").parent());
		value_changed(e.target.value == "True", $("#id_alimentacion-otro_motivo_suspencion_lactancia"));
	});
	value_changed($('input:radio[name=alimentacion-difiere_alimentacion]:checked').val() == "True", $("#id_alimentacion-motivo_cambios_alimentacion").parent());
	$('input:radio[name=alimentacion-difiere_alimentacion]').change(function(e){
		value_changed(e.target.value == "True", $("#id_alimentacion-motivo_cambios_alimentacion").parent());
	});

	value_changed($("#id_alimentacion-motivo_suspencion_lactancia_5").is(":checked"), $("#id_alimentacion-otro_motivo_suspencion_lactancia").parent());
	$('input[name=alimentacion-motivo_suspencion_lactancia]').change(function(e){
		value_changed($("#id_alimentacion-motivo_suspencion_lactancia_5").is(":checked"), $("#id_alimentacion-otro_motivo_suspencion_lactancia").parent());
	});
	value_changed($("#id_alimentacion-afecciones_2").is(":checked"), $("#id_alimentacion-otra_afeccion").parent());
	$('input[name=alimentacion-afecciones]').change(function(e){
		value_changed($("#id_alimentacion-afecciones_2").is(":checked"), $("#id_alimentacion-otra_afeccion").parent());
	});
	value_changed($("#id_alimentacion-enfermedades_3").is(":checked"), $("#id_alimentacion-otra_enfermedad").parent());
	$('input[name=alimentacion-enfermedades]').change(function(e){
		value_changed($("#id_alimentacion-enfermedades_3").is(":checked"), $("#id_alimentacion-otra_enfermedad").parent());
	});
	value_changed($("#id_alimentacion-forma_alimento_7").is(":checked"), $("#id_alimentacion-otra_forma_alimento").parent());
	$('input[name=alimentacion-forma_alimento]').change(function(e){
		value_changed($("#id_alimentacion-forma_alimento_7").is(":checked"), $("#id_alimentacion-otra_forma_alimento").parent());
	});




	
	value_changed($('input:radio[name=familiares_otros-transtorno_hermanos]:checked').val() == "True", $("#id_familiares_otros-hermano_transtorno").parent());
	value_changed($('input:radio[name=familiares_otros-transtorno_hermanos]:checked').val() == "True", $("#id_familiares_otros-transtorno").parent());
	value_changed($('input:radio[name=familiares_otros-transtorno_hermanos]:checked').val() == "True", $("#id_familiares_otros-alteracion_desarrollo").parent());
	$('input:radio[name=familiares_otros-transtorno_hermanos]').change(function(e){
		value_changed(e.target.value == "True", $("#id_familiares_otros-hermano_transtorno").parent());
		value_changed(e.target.value == "True", $("#id_familiares_otros-transtorno").parent());
		value_changed(e.target.value == "True", $("#id_familiares_otros-alteracion_desarrollo").parent());
	});
});
