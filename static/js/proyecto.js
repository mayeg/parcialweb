$(document).ready(function(){
    $("#cliente").on('change', function(){
        $.get("/get_cliente/" + $(this).val(), function(data){
            var cliente = data;
            $("#nombresCliente").html(cliente.nombres);
            $("#apellidosCliente").html(cliente.apellidos);
            $("#direccionCliente").html(cliente.direccion);
            $("#telefonoCliente").html(cliente.telefono);
            $("#facturaTotal").show();
        });
    });
});