$(document).ready(function() {

   $.getScript("/static/js/cita/jquery.cookie.js", function(){

   });

   function ver_cita(dialogContent,id){
      var data = JSON.parse(ajax_get_cita(id));

      var paciente = data[0].fields.paciente;
      var tipoterapia = data[0].fields.tipo_terapia;
      var terapista = data[0].fields.terapista;
      var estado = data[0].fields.estado;
      var indicaciones = data[0].fields.indicaciones;

      dialogContent.find("select[name='paciente']").val(paciente);
      dialogContent.find("select[name='tipoterapia']").val(tipoterapia);
      dialogContent.find("select[name='terapista']").val(terapista);
      dialogContent.find("select[name='estados']").val(estado);
      dialogContent.find("textarea[name='indicaciones']").val(indicaciones);

   }

   function ajax_get_citas(){

      var resp;

      $.ajax({
          async: false,
          type: 'get',
          url: '/get_citas/',
          success : function(response){
            resp = response;
          },
          dataType: 'json'
      });

      return resp;
   }

   function ajax_get_cita(id){

      var resp;

      $.ajax({
          async: false,
          type: 'get',
          url: '/get_cita/',
          data: {'id_cita':id},
          success : function(response){
            resp = response;
          },
          dataType: 'json'
      });

      return resp;
   }

   function ajax_save_cita(date_holder,start,end,paciente,tipoterapia,terapista,estado,indicaciones){
      var cookie = Cookies.get('csrftoken');

      $.ajax({
          type: 'POST',
          url: '/save_cita/',
          data:{
            'date_holder':date_holder,
            'start':start,
            'end':end,
            'paciente':paciente,
            'tipoterapia':tipoterapia,
            'terapista':terapista,
            'estado':estado,
            'indicaciones':indicaciones,
            'csrfmiddlewaretoken' : cookie
          },
          success : function(response){
            console.log(response);
          },
          dataType: 'json'
      });
   }

   function ajax_update_cita(date_holder,start,end,paciente,tipoterapia,terapista,estado,indicaciones,id){
      var cookie = Cookies.get('csrftoken');

      $.ajax({
          type: 'POST',
          url: '/update_cita/',
          data:{
            'cita_id':id,
            'date_holder':date_holder,
            'start':start,
            'end':end,
            'paciente':paciente,
            'tipoterapia':tipoterapia,
            'terapista':terapista,
            'estado':estado,
            'indicaciones':indicaciones,
            'csrfmiddlewaretoken' : cookie
          },
          success : function(response){
            console.log(response);
          },
          dataType: 'json'
      });
   }

   function not_null(list){
      for(i in list){
         if(list[i]==null || list[i]=="")
            return false;
      }
      return true;
   }

   function ajax_edit_cita(){

   }

   function ajax_delete_cita(id){
      var cookie = Cookies.get('csrftoken');

      $.ajax({
          type: 'POST',
          url: '/delete_cita/',
          data:{
            'cita_id':id,
            'csrfmiddlewaretoken' : cookie
          },
          success : function(response){
            console.log(response);
          },
          dataType: 'json'
      });
   }


   var $calendar = $('#calendar');
   var id = 10;

   $calendar.weekCalendar({
      timeslotsPerHour : 4,
      allowCalEventOverlap : true,
      overlapEventsSeparate: true,
      firstDayOfWeek : 1,
      businessHours :{start: 8, end: 18, limitDisplay: true },
      daysToShow : 7,
      height : function($calendar) {
         return $(window).height() - $("h1").outerHeight() - 1;
      },
      eventRender : function(calEvent, $event) {
         if (calEvent.end.getTime() < new Date().getTime()) {
            $event.css("backgroundColor", "#aaa");
            $event.find(".wc-time").css({
               "backgroundColor" : "#999",
               "border" : "1px solid #888"
            });
         }
      },
      draggable : function(calEvent, $event) {
         return calEvent.readOnly != true;
      },
      resizable : function(calEvent, $event) {
         return calEvent.readOnly != true;
      },
      eventNew : function(calEvent, $event) {
         var $dialogContent = $("#event_edit_container");
         resetForm($dialogContent);
         var date = $dialogContent.find("input[name='date_holder']");
         var startField = $dialogContent.find("select[name='start']").val(calEvent.start);
         var endField = $dialogContent.find("select[name='end']").val(calEvent.end);
         var paciente = $dialogContent.find("select[name='paciente']");
         var tipoterapia = $dialogContent.find("select[name='tipoterapia']");
         var terapista = $dialogContent.find("select[name='terapista']");
         var estado = $dialogContent.find("select[name='estados']");
         var indicaciones = $dialogContent.find("textarea[name='indicaciones']");
         

         $dialogContent.dialog({
            modal: true,
            title: "Nueva cita",
            close: function() {
               $dialogContent.dialog("destroy");
               $dialogContent.hide();
               $('#calendar').weekCalendar("removeUnsavedEvents");
            },
            buttons: {
               Reservar : function() {
                  var fecha_cita = date.val();
                  var inicio = startField.val();
                  var fin = endField.val();
                  var paciente_id = paciente.val();
                  var tipoterapia_id = tipoterapia.val();
                  var terapista_id = terapista.val();
                  var es = estado.val();
                  var txt = indicaciones.val();
                  
                  if(not_null([fecha_cita,inicio,fin,paciente_id,tipoterapia_id,terapista_id,es])){
                     ajax_save_cita(fecha_cita,inicio,fin,paciente_id,tipoterapia_id,terapista_id,es,txt);
                  }

                  resetForm($dialogContent);
                  $dialogContent.dialog("close");
                  location.reload(true);
               },
               Cancelar : function() {
                  $dialogContent.dialog("close");
               }        
            }
         }).show();

         /*$dialogContent.find(".date_holder").text($calendar.weekCalendar("formatDate", calEvent.start));*/
         $dialogContent.find("input[name='date_holder']").val($calendar.weekCalendar("formatDate", calEvent.start));
         setupStartAndEndTimeFields(startField, endField, calEvent, $calendar.weekCalendar("getTimeslotTimes", calEvent.start));

      },
      eventDrop : function(calEvent, $event) {
      },
      eventResize : function(calEvent, $event) {
      },
      eventClick : function(calEvent, $event) {

         if (calEvent.readOnly) {
            return;
         }

         var $dialogContent = $("#event_edit_container");
         resetForm($dialogContent);
         var date = $dialogContent.find("input[name='date_holder']");
         var startField = $dialogContent.find("select[name='start']").val(calEvent.start);
         var endField = $dialogContent.find("select[name='end']").val(calEvent.end);
         var paciente = $dialogContent.find("select[name='paciente']");
         var tipoterapia = $dialogContent.find("select[name='tipoterapia']");
         var terapista = $dialogContent.find("select[name='terapista']");
         var estado = $dialogContent.find("select[name='estados']");
         var indicaciones = $dialogContent.find("textarea[name='indicaciones']");

         $dialogContent.dialog({
            modal: true,
            title: "Editar Cita ",
            close: function() {
               $dialogContent.dialog("destroy");
               $dialogContent.hide();
               $('#calendar').weekCalendar("removeUnsavedEvents");
            },
            buttons: {
               Editar : function() {
                  var fecha_cita = date.val();
                  var inicio = startField.val();
                  var fin = endField.val();
                  var paciente_id = paciente.val();
                  var tipoterapia_id = tipoterapia.val();
                  var terapista_id = terapista.val();
                  var es = estado.val();
                  var txt = indicaciones.val();

                  if(not_null([fecha_cita,inicio,fin,paciente_id,tipoterapia_id,terapista_id,es])){
                     ajax_update_cita(fecha_cita,inicio,fin,paciente_id,tipoterapia_id,terapista_id,es,txt,calEvent.id);
                  }

                  resetForm($dialogContent);
                  $dialogContent.dialog("close");
                  location.reload(true);
               },
               Eliminar : function() {
                  $calendar.weekCalendar("removeEvent", calEvent.id);
                  ajax_delete_cita(calEvent.id);
                  $dialogContent.dialog("close");
               },
               Cancelar : function() {
                  $dialogContent.dialog("close");
               }
            }
         }).show();

         var startField = $dialogContent.find("select[name='start']").val(calEvent.start);
         var endField = $dialogContent.find("select[name='end']").val(calEvent.end);
         

         $dialogContent.find("input[name='date_holder']").val($calendar.weekCalendar("formatDate", calEvent.start));
         setupStartAndEndTimeFields(startField, endField, calEvent, $calendar.weekCalendar("getTimeslotTimes", calEvent.start));
         ver_cita($dialogContent,calEvent.id);
         $(window).resize().resize(); //fixes a bug in modal overlay size ??

      },
      eventMouseover : function(calEvent, $event) {
      },
      eventMouseout : function(calEvent, $event) {
      },
      noEvents : function() {

      },
      data : function(start, end, callback) {
         callback(getEventData());
      }
   });

   function resetForm($dialogContent) {
      $dialogContent.find("input").val("");
      $dialogContent.find("select").val("");
      $dialogContent.find("textarea").val("");
   }

   function getEventData() {
      var year = new Date().getFullYear();
      var month = new Date().getMonth();
      var day = new Date().getDate();
      var ev = JSON.parse(ajax_get_citas());
      var citas = [];

      for(var i in ev){
         var fecha_cita = ev[i].fields.fecha_cita;
         var hora_inicio = ev[i].fields.hora_inicio;
         var hora_fin = ev[i].fields.hora_fin;

         var start = new Date(fecha_cita + " " + hora_inicio)
         var end = new Date(fecha_cita + " " + hora_fin)
         var title = ev[i].fields.paciente.fullname + " " + ev[i].fields.tipo_terapia + " " + ev[i].fields.terapista.fullname
         var aux = {"id":ev[i].pk,"start": new Date(fecha_cita + " " + hora_inicio),"end":new Date(fecha_cita + " " + hora_fin),"title":title};
         citas.push(aux);
      }

      return {
         events : citas
      };
   }


   /*
    * Sets up the start and end time fields in the calendar event
    * form for editing based on the calendar event being edited
    */
   function setupStartAndEndTimeFields($startTimeField, $endTimeField, calEvent, timeslotTimes) {

      for (var i = 0; i < timeslotTimes.length; i++) {
         var startTime = timeslotTimes[i].start;
         var endTime = timeslotTimes[i].end;
         var startSelected = "";
         if (startTime.getTime() === calEvent.start.getTime()) {
            startSelected = "selected=\"selected\"";
         }
         var endSelected = "";
         if (endTime.getTime() === calEvent.end.getTime()) {
            endSelected = "selected=\"selected\"";
         }
         $startTimeField.append("<option value=\"" + startTime + "\" " + startSelected + ">" + timeslotTimes[i].startFormatted + "</option>");
         $endTimeField.append("<option value=\"" + endTime + "\" " + endSelected + ">" + timeslotTimes[i].endFormatted + "</option>");

      }
      $endTimeOptions = $endTimeField.find("option");
      $startTimeField.trigger("change");
   }

   var $endTimeField = $("select[name='end']");
   var $endTimeOptions = $endTimeField.find("option");

   //reduces the end time options to be only after the start time options.
   $("select[name='start']").change(function() {
      var startTime = $(this).find(":selected").val();
      var currentEndTime = $endTimeField.find("option:selected").val();
      $endTimeField.html(
            $endTimeOptions.filter(function() {
               return startTime < $(this).val();
            })
            );

      var endTimeSelected = false;
      $endTimeField.find("option").each(function() {
         if ($(this).val() === currentEndTime) {
            $(this).attr("selected", "selected");
            endTimeSelected = true;
            return false;
         }
      });

      if (!endTimeSelected) {
         //automatically select an end date 2 slots away.
         $endTimeField.find("option:eq(1)").attr("selected", "selected");
      }

   });


   var $about = $("#about");

   $("#about_button").click(function() {
      $about.dialog({
         title: "About this calendar demo",
         width: 600,
         close: function() {
            $about.dialog("destroy");
            $about.hide();
         },
         buttons: {
            close : function() {
               $about.dialog("close");
            }
         }
      }).show();
   });


});