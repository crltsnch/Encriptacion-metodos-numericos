# Encriptacion-metodos-numericos

## Introducción 
Este repositorio se ha desarrollado para encriptar y desencriptar mensajes, empleando métodos numéricos. A través de una ecuación no lineal, calculamos sus raíces usando el método de Newton-Raphson, obteniendo así un mensaje codificado. Para decodificar un mensaje se sigue el proceso inverso. 

## Cómo descargar el código
Para descargar este código a tu ordenador, pulsa el botón verde llamado `<> Code`. Se desplegará un menú y selecciona la opción `Download ZIP`. Se descargará un archivo ZIP a tu ordenador y para poder abrir la carpeta, simplemente debes descomprimir el archivo ZIP. Una vez hecho esto, ya podrás acceder a la carpeta con los archivos de código.

## Cómo ejecutar el código
Para que el código se ejecute correctamente, debe ejecutar el código del archivo `run.py`.

## Archivos
Todos los archivos están guardados en la carpeta `Criptografia`.
- `run.py`. En este archivo se encuentra una línea de código que hace que el código se ejecute.
- `config.py`. Aquí encontramos todas las funciones que modifican la terminal a nuestro gusto (estética).
- `menu.py`. Este archivo configura el menú que aparece en la terminal.
- `proceso.py`. Aquí tenemos todo el código que nos permite realizar la codificación y decodificación de mensajes. Definimos la función no lineal, la función de punto fijo de Newton-Raphson, el método iterativo de resolución de ecuaciones no lineales, la encriptación y desencriptación de mensajes.

Por otro lado, la carpeta `Imágenes` contiene todas las fotos que usamos más adelante.

## Limitaciones
El código tiene ciertas limitaciones que nos gustaría que se tuviesen en cuenta:
- Para modificar la clave (ecuación no lineal) y su correspondiente función de Newton-Raphson (gn(x)) hay que hacerlo a mano, directamente modificando el código. Esto se puede hacer en el archivo `proceso.py` en las líneas 6 y 9 de código respectivamente.
- Hay que tener en cuenta que existen caracteres en el alfabeto español que no tienen ningún valor ASCII asignado.
- Al introducir el mensaje encriptado en el código, incluir los separadores '|'.

## Paso a paso
En este apartado explicamos cómo funciona el código.

### Menú
![Menú del código](https://raw.githubusercontent.com/crltsnch/Encriptacion-metodos-numericos/master/Imágenes/metodos_paso1.png)

### Encriptar
Cuando seleccionamos opción 1, en la terminar aparece el siguiente mensaje.

![Solicita mensaje a encriptar](https://raw.githubusercontent.com/crltsnch/Encriptacion-metodos-numericos/master/Imágenes/1-mensaje.png)

Introducimos el mensaje y la pantalla se actualiza.

![Mensaje encriptado](https://raw.githubusercontent.com/crltsnch/Encriptacion-metodos-numericos/master/Imágenes/1-encriptado.png)

Nos pide si queremos desencriptar ese mismo mensaje.

- Si respondemos que sí (Y).

![Mensaje desencriptado](https://raw.githubusercontent.com/crltsnch/Encriptacion-metodos-numericos/master/Imágenes/1-desencriptar_Y.png)

- Si respondemos que no (N).

![Fin parte 1](https://raw.githubusercontent.com/crltsnch/Encriptacion-metodos-numericos/master/Imágenes/1-desencriptar_N.png)

Finalmente, nos pregunta si queremos volver al menú (Y) o si queremos cerrar el programa (N). 

### Desencriptar
Cuando seleccionamos opción 2, en la terminar aparece el siguiente mensaje.

![Solicita mensaje a desencriptar](https://raw.githubusercontent.com/crltsnch/Encriptacion-metodos-numericos/master/Imágenes/2-mensaje.png)

Introducimos el mensaje y la pantalla se actualiza.

![Mensaje desencriptado](https://raw.githubusercontent.com/crltsnch/Encriptacion-metodos-numericos/master/Imágenes/2-desencriptado.png)

Finalmente, nos pregunta si queremos volver al menú (Y) o si queremos cerrar el programa (N). 

### Salir
Al seleccionar la tercera opción, el programa se cierra.

![Saliendo..](https://raw.githubusercontent.com/crltsnch/Encriptacion-metodos-numericos/master/Imágenes/3.png)
