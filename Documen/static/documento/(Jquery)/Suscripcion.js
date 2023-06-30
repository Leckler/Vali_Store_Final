$(document).ready(function(){
    $("#Pago").click(function(){
        var monto = $("#Donativo").val();
        var metodo = $("#optMetodoP").val();

        if(monto == 0){
            $("#Vmonto").fadeIn();
            return false;
        }else{
            $("#Vmonto").fadeOut();
        }

        if(metodo == "0"){
            $("#Vmetodo").fadeIn();
            return false;

        }else{
            $("#Vmetodo").fadeOut();
        }

        


        
    })

    $("#Vmetodo").hide();
    $("#Vmonto").hide();


})

