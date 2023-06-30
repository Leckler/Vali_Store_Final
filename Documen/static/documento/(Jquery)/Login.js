$(document).ready(function(){
    $("#boton2").click(function(){
        var usuario = $("#nombre").val();
        var entrada = $("#clave").val();

        var enlace = true;
        if(usuario.length == 0){
            $("#Lnombre").fadeIn();
            enlace = false;
        }else{
            $("#Lnombre").fadeOut();
            if(entrada.length < 4){
                $("#Lclave").fadeIn();
                enlace = false;
            }else{
                $("#Lclave").fadeOut();
            }
        }

        if (enlace){
            $("#alerta").attr("hidden", false)
            $("#alerta").attr("class", "alert alert-success col-md-3")
            $("#resultado").text("Enlace confirmado")

        }else{
            $("#alerta").attr("hidden", false)
            $("#alerta").attr("class", "alert alert-danger col-md-3")
            $("#resultado").text("Enlace no confirmado")

        }


    })
    $("#nombre").blur(function(){
        var usuario=$("#nombre").val();
        if(usuario.length==0){
            $("#nombre").css("border","3px solid red")
            alert("Este campo no puede estar vacio")
        }else{
            $("#nombre").css("border","1px solid lightgrey")
        }
    })

    $("#Lnombre").hide();
    $("#Lclave").hide();
})