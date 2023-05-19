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

## Limitaciones
El código tiene ciertas limitaciones que nos gustaría que se tuviesen en cuenta:
- Para modificar la clave (ecuación no lineal) y su correspondiente función de Newton-Raphson (gn(x)) hay que hacerlo a mano, directamente modificando el código. Esto se puede hacer en el archivo `proceso.py` en las líneas 6 y 9 de código respectivamente.
- Hay que tener en cuenta que existen caracteres en el alfabeto español que no tienen ningún valor ASCII asignado.
- Al introducir el mensaje encriptado en el código, incluir los separadores '|'.

## Paso a paso
