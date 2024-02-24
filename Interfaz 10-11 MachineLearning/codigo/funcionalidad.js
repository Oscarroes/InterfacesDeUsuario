
        //DECLARACIÓN DE VARIABLESGLOBALES
        var supercontador = -1;
        var datosImagenes = []
        var temporizador = ""
        var datos;

        var imagen = new Image();
        var imagen2 = new Image();
        var contexto
        var contexto2
        var contexto3
        var contextoVertical
        var contextoHorizontal
        var contextoDiagonal1
        var contextoDiagonal2
        var contextoLinea30
        var contextoLinea_30
        var patrones = []
        var cuentapatrones = []

        // CARGAR IMAGEN DENTRO DE UN CANVAS PARA PODER MANIPULARLA:
        window.onload = function(){
            //CARGAMOS EL CONTEXTO DE LOS LIENZOS PARA QUE PODAMOS PINTAR EN LOS LIENZOS
            contexto = document.getElementById("lienzo").getContext("2d");
            contexto2 = document.getElementById("lienzo2").getContext("2d");
            contexto3 = document.getElementById("lienzo3").getContext("2d");

            //CONTEXTO DE LAS REFERENCIAS VERTICAL Y HORIZONTAL
            contextoVertical = document.getElementById("lienzoVertical").getContext("2d");
            contextoHorizontal = document.getElementById("lienzoHorizontal").getContext("2d");
            //CONTEXTO DE LAS DIAGONALES
            contextoDiagonal1 = document.getElementById("lienzoDiagonal1").getContext("2d");
            contextoDiagonal2 = document.getElementById("lienzoDiagonal2").getContext("2d");
            //CONTEXTO DE LAS LINEAS A +-30º
            contextoLinea30 = document.getElementById("lienzoLinea30").getContext("2d");
            contextoLinea_30 = document.getElementById("lienzoLinea_30").getContext("2d");

            //PATRONES
            patrones[0] = new Image();
            patrones[0].src = "img/vertical.png";
            patrones[1] = new Image();
            patrones[1].src = "img/horizontal.png";
            patrones[2] = new Image();
            patrones[2].src = "img/diagonal1.png";
            patrones[3] = new Image();
            patrones[3].src = "img/diagonal2.png";
            patrones[4] = new Image();
            patrones[4].src = "img/linea30.png";
            patrones[5] = new Image();
            patrones[5].src = "img/linea-30.png";
            
            cuentapatrones[0] = 0;
            cuentapatrones[1] = 0;
            cuentapatrones[2] = 0;
            cuentapatrones[3] = 0;
            cuentapatrones[4] = 0;
            cuentapatrones[5] = 0;

            procesaImagen("../../imagenes/002procesadas/")
            fetch("../imagenes/json/imagenes.json")
            .then(function(response){
                    return response.json()
                })
            .then(function(misdatos){
                console.log(datos)
                datos = misdatos
                temporizador = setTimeout("bucle()",5)
            })

        }
        function bucle(){
                supercontador++;
                // Limpia el lienzo3 antes de cargar la nueva imagen
                contexto3.clearRect(0, 0, 512, 512);
                procesaImagen("../../imagenes/002procesadas/" + datos[supercontador])
                clearTimeout(temporizador);
                temporizador = setTimeout(function(){
                    clearTimeout(temporizador);
                    temporizador = setTimeout("bucle()",5000);
                }, 1000);
            }
        //FUNCION PARA PROCESAR LA IMAGEN
        function procesaImagen(miimagen){
            //CARGO UNA IMAGEN DEL DISCO DURO 
            imagen.src = "img/" + miimagen;
            //ME ESPERO A QUE LA IMAGEN CARGUE Y ENTONCES EJECUTO ESTA FUNCION
            imagen.onload = function(){
                //PINTO LAS REFERENCIAS
                contextoVertical.drawImage(patrones[0],0,0)
                contextoHorizontal.drawImage(patrones[1],0,0)
                contextoDiagonal1.drawImage(patrones[2],0,0)
                contextoDiagonal2.drawImage(patrones[3],0,0)
                contextoLinea30.drawImage(patrones[4],0,0)
                contextoLinea_30.drawImage(patrones[5],0,0)
                //primero pinto la imagen original EN EL LIENZO ORIGINAL
                contexto.drawImage(imagen,0,0);

                //CARGAMOS LA IMAGEN 1 EN MEMORIA
                //ahora vamos a detectar los bordes/contorno en la imagen pixel a pixel
                let imagenlienzo1 = contexto.getImageData(0,0,512,512);
                //CARGAMOS LA IMAGEN 2 EN MEMORIA
                let imagenlienzo2 = contexto2.getImageData(0,0,512,512);
                

                //PARA CADA UNO DE LOS PIXELES DE LA IMAGEN, DE CERO HASTA LA LONGITUD FINAL 
                //DE LOS DATOS DE LA IMAGEN MIRO LA DIFERENCIA DEL CANAL ROJO EN HORIZONTAL
                //recorremos la imagen pixel a pixel por filas: i+=4 porque cada pixel está cada 4 valores RGBA
                for(let i = 0; i<imagenlienzo1.data.length; i+=4){
                    //MIRO LA DIFERENCIA DEL CANAL ROJO EN HORIZONTAL:
                    let diferencia = Math.abs(imagenlienzo1.data[i]-imagenlienzo1.data[i+4])
                    //MIRO LA DIFERENCIA DEL CANAL ROJO EN VERTICAL TAMBIÉN:
                    let diferencia2 = Math.abs(imagenlienzo1.data[i]-imagenlienzo1.data[i+512*4])
                    if(diferencia > 10 || diferencia2 > 10){
                        //SI DIFERENCIA < 10 PINTA PIXEL DE COLOR
                        imagenlienzo2.data[i] = 0;
                        imagenlienzo2.data[i+1] = 0;
                        imagenlienzo2.data[i+2] = 0;
                        imagenlienzo2.data[i+3] = 255;
                    }else{
                        //SI DIFERENCIA > 10 PINTA PIXEL BLANCO
                        imagenlienzo2.data[i] = 255;
                        imagenlienzo2.data[i+1] = 255;
                        imagenlienzo2.data[i+2] = 255;
                        imagenlienzo2.data[i+3] = 255;

                    }
                }
                //POR ÚLTIMO PONGO LA IMAGEN EN BLANCO Y NEGRO EN EL LIENZO2:
                contexto2.putImageData(imagenlienzo2,0,0);

                //FUNCION PARA RECORRER LA IMAGEN DEPENDIENDO DE LA DIRECCIÓN
                function lineas(contextoLinea,contexto2,contexto3,precision,cuentaP,indice,color){
                    let muestravertical = contextoLinea.getImageData(0,0,8,8)
                    for(let x = 0; x < 512; x++){
                        for(let y = 0; y < 512; y++){
                            //vamos a restar el trozo contra la direccion
                            let trozo = contexto2.getImageData(x,y,8,8)
                            let suma = 0;
                            for(let i = 0; i < trozo.data.length; i+=4){
                                suma += Math.abs(trozo.data[i] - muestravertical.data[i])
                            } //DETECTAMOS LOS PIXELES QUE COINCIDEN CON LA DIRECCION ELEGIDA
                            //A MAYOR NUMERO EN PRECISION MENOS PRECISA SERÁ LA COINCIDENCIA
                            if(suma < precision){
                            cuentaP[indice]++;
                            contexto3.fillStyle = color;
                            contexto3.fillRect(x,y,2,2);
                            }
                        
                        }
                    }

                }

                //RECORREMOS LA IMAGEN QUE HE PINTADO CON BORDES PARA VERTICAL
                lineas(contextoVertical,contexto2,contexto3,4000,cuentapatrones,0,"red");
                //RECORREMOS LA IMAGEN QUE HE PINTADO CON BORDES PARA HORIZONTAL
                lineas(contextoHorizontal,contexto2,contexto3,4000,cuentapatrones,1,"blue");
                //RECORREMOS LA IMAGEN QUE HE PINTADO CON BORDES PARA DIAGONAL1
                lineas(contextoDiagonal1,contexto2,contexto3,4000,cuentapatrones,2,"green");
                //RECORREMOS LA IMAGEN QUE HE PINTADO CON BORDES PARA DIAGONAL2
                lineas(contextoDiagonal2,contexto2,contexto3,4000,cuentapatrones,3,"orange");
                //RECORREMOS LA IMAGEN QUE HE PINTADO CON BORDES PARA LINEA 30º
                lineas(contextoLinea30,contexto2,contexto3,3000,cuentapatrones,4,"yellow");
                //RECORREMOS LA IMAGEN QUE HE PINTADO CON BORDES PARA LINEA -30º
                lineas(contextoLinea_30,contexto2,contexto3,3000,cuentapatrones,5,"cyan");

                //SACAMOS LOS RESULTADOS POR CONSOLA
                console.log(cuentapatrones)
                let total = 0;
                for(i=0; i<cuentapatrones.length; i++){
                    total += cuentapatrones[i]
                }
                for(i=0; i<cuentapatrones.length; i++){
                    cuentapatrones[i] /= total
                }
                console.log(cuentapatrones)
                //GUARDAR LA INFO EN UN JSON
                let guarda = JSON.stringify(cuentapatrones)
                let patron = miimagen.split("-")
                let rutacompleta = miimagen
                let soloimagen = rutacompleta.split("/")[rutacompleta.split("/").length - 1]
                let quitoExtension = soloimagen.split(".")[0]
                
                fetch("guardajson2.php?archivo=" + soloimagen + "&patron=" + quitoExtension + "&datos=" + guarda)
            }
            }