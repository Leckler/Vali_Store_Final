$(document).ready(function(){
    document.getElementById("MostrarH").addEventListener("click", MostrarH);
    function MostrarH(){
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function(){
            if(this.readyState == 4 && this.status == 200){
                cargarXML(this);
            }
        };
        xhr.open("GET","../(XML)/Historial.xml",true);
        xhr.send();

    }
    function cargarXML(xml){
        var docXML = xml.responseXML;
        var tabla = "<tr><th>ID</th><th>Domicilio</th><th>Estado</th><th>FechaCompra</th><th>FechaEntrega</th></tr>";
        var cds = docXML.getElementsByTagName("CD");
        for (var i = 0; i<cds.length; i++){
            tabla += "<tr><td>";
            tabla += cds[i].getElementsByTagName("ID")[0].textContent;
            tabla += "</td><td>";
            tabla += cds[i].getElementsByTagName("Domicilio")[0].textContent;
            tabla += "</td><td>";
            tabla += cds[i].getElementsByTagName("Estado")[0].textContent;
            tabla += "</td><td>";
            tabla += cds[i].getElementsByTagName("FechaCompra")[0].textContent;
            tabla += "</td><td>";
            tabla += cds[i].getElementsByTagName("FechaEntrega")[0].textContent;
            tabla += "</td></tr>";

        }


        document.getElementById("crear").innerHTML = table;
    }
});
