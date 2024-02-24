<?php

    $archivo = "datos/prueba.json";
    $datos = [
        'archivo' => $_GET['archivo'],
        'elemento' => $_GET['patron'],
        'datos' => json_decode($_GET['datos'])
    ];
 
    $datosExistentes = file_get_contents($archivo);
    $datosExistentesjson = json_decode($datosExistentes);

    array_push($datosExistentesjson,$datos);

    $json = json_encode($datosExistentesjson,JSON_PRETTY_PRINT);

    file_put_contents($archivo,$json);

?>