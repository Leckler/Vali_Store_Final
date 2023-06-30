$(document).ready(function(){
    $("#btnEnviar").click(function(){
        var nombre = $("#pnombre").val();
        var apellido = $("#apaterno").val();
        var edades = $("#edad").val();
        var correos = $("#correo").val();
        var fono = $("#telefono").val();
        var genero = $("#optGenero").val();
        var clave = $("#pass").val();
        var clave2 = $("#pass2").val();
        var sobrenombre = $("#nombreU").val();
        var team = $("#optEquipo").val();
        var restrictora = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+/;
        var acceso = true;
        
       
        if(nombre == ""){
            $("#Verify1").fadeIn();
            return false;
        }else{
            $("#Verify1").fadeOut();
            if(apellido == ""){
                $("#Verify2").fadeIn();
                return false;
            }else{
                $("#Verify2").fadeOut();
                if(edades < 18){
                    $("#Verify3").fadeIn();
                    return false;
                }else{
                    $("#Verify3").fadeOut();
                    if(correos == "" || !restrictora.test(correos)){
                        $("#Verify4").fadeIn();
                        return false;
                    }else{
                        $("#Verify4").fadeOut();
                        if(fono <111111111 || fono >999999999){
                            $("#Verify5").fadeIn();
                            return false;
                        }else{
                            $("#Verify5").fadeOut();
                            if(genero == "0"){
                                $("#Verify6").fadeIn();
                                return false;

                            }else{
                                $("#Verify6").fadeOut();
                                if(clave == ""){
                                    $("#Verify7").fadeIn();
                                    return false;
                                }else{
                                    $("#Verify7").fadeOut();
                                    if(clave2 != clave){
                                        $("#Verify8").fadeIn();
                                        return false;
                                    }else{
                                        $("#Verify8").fadeOut();
                                        if(acceso = true){
                                            window.location.href = "Home.HTML";
                                        }

                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        
    })

    $("#empresa").click(function(){ 
        $("#empresa").hide();
        
        
    });

    $("#Verify1").hide();
    $("#Verify2").hide();
    $("#Verify3").hide();
    $("#Verify4").hide();
    $("#Verify5").hide();
    $("#Verify6").hide();
    $("#Verify7").hide();
    $("#Verify8").hide();
    $("#Verify9").hide();
    $("#Verify10").hide();

    $("#telefono").on('input', function () { 
        this.value = this.value.replace(/[^0-9]/g,'');
    });

    

});