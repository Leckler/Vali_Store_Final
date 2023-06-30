


$(document).ready(function () {
    $.ajax({
        url: "https://apis.digital.gob.cl/dpa/regiones",
        type: "GET",
        crossDomain: true,
        dataType: "jsonp",
        success: function (data) {
          $.each(data, function (i, item) {
            $("#optRegion").append(
              "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
            );
          });
        },
        error: function (xhr, status, error) {
          console.log("Error al obtener las regiones: " + error);
        }
    });

    $.ajax({
      url: "https://apis.digital.gob.cl/dpa/comunas",
      type: "GET",
      crossDomain: true,
      dataType: "jsonp",
      success: function (data) {
        $.each(data, function (i, item) {
          $("#optComuna").append(
            "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
          );
        });
      },
      error: function (xhr, status, error) {
        console.log("Error al obtener las regiones: " + error);
      }
  });

  $("#telefono").on('input', function () { 
    this.value = this.value.replace(/[^0-9]/g,'');
  });

  $("#EnviarP").click(function(){
    var nombre = $("#pnombre").val();
    var apellido = $("#apaterno").val();
    var correos = $("#correo").val();
    var fono = $("#telefono").val();
    var region = $("#optRegion").val();
    var comuna = $("#optComuna").val();
    var direccion = $("#direccion").val();
    var restrictora = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+/;

    if(nombre == ""){
      $("#VerifyN").fadeIn();
      return false;
    }else{
      $("#VerifyN").fadeOut();
      if(apellido == ""){
        $("#VerifyA").fadeIn();
        return false;
      }else{
        $("#VerifyA").fadeOut();
        if(correos == "" || !restrictora.test(correos)){
          $("#VerifyE").fadeIn();
          return false;
        }else{
          $("#VerifyE").fadeOut();
          if(fono <111111111 || fono >999999999){
            $("#VerifyT").fadeIn();
            return false;
          }else{
            $("#VerifyT").fadeOut();
            if(direccion == ""){
              $("#VerifyD").fadeIn();
              return false;
            }else{
              $("#VerifyD").fadeOut();
              if(region == ""){
                $("#VerifyR").fadeIn();
                return false;
              }else{
                $("#VerifyR").fadeOut();
                if(comuna == ""){
                  $("#VerifyC").fadeIn();
                  return false;
                }else{
                  $("#VerifyC").fadeOut();
                }
              }
            }
          }
        }
      }
    }
  });
  $("#VerifyN").hide();
  $("#VerifyA").hide();
  $("#VerifyE").hide();
  $("#VerifyT").hide();
  $("#VerifyD").hide();
  $("#VerifyR").hide();
  $("#VerifyC").hide();
  

});     
                  


