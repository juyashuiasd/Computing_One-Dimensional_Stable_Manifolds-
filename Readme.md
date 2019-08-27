# Computing One-Dimensional Stable Manifolds and Stable Sets of Planar Maps without the Inverse
## Requisitos Previos
Para el uso de este programa, es necesario disponer de la librería matplotlib, que se puede instalar fácilmente con el siguiente comando:
```
pip install matplotlib
```
## Introducción
El código presente se compone de 5 archivos diferentes necesarios para la ejecución completa del código:

- mc.py: se ocupa de la ejecución del código.
- mclib.py: todas las funciones utilizadas se encuentran en este archivo que sirve como librería.
- point.py: se define la clase Point
- vector.py: se define la clase Vector
- plot.py: realiza la imagen tras la ejecución del algoritmo

## Instrucciones de uso

Para usar el código, abrimos una terminal y nos posicionamos en la carpeta donde se cuenta el archivo mc.py para posteriormente lanzar el siguiente comando:
```
python3 mc.py
```
Al ejecutar el código se le hará diferentes preguntas:

- ¿Quieres cambiar los parámetros?: si escribe "Y" pasará a modificar uno a uno los parámetros y si escribe "N" se usarán los parámetros por defecto.
- ¿Qué función utilizar?: deberá escribir un número del 1-4 donde decidirá sobre qué función calcularemos las variedades. El modo "input" se explicará posteriormente.
- ¿Cambiar el parámetro delta_k? después de elegir la función se le preguntará si quiere modificar delta_k. Pasará a modificarlo si escribe "Y", o usará su valor por defecto en el caso de escribir "N".
- ¿Qué variedad estable quiere calcular?(En la medida de lo posible): Se pueden elegir tres modos:
  - "S": variedad estable.
  - "U": variedad inestable.
  - "B": ambas.

Después de realizar todas las preguntas, se pasará a la función correspondiente para ejecutar el algoritmo. Estas funciones se llaman henonCalc, ikedaCalc, miraCalc e inputCalc. Esta última, está vacía por defecto, mientras que las tres primeras, cuentan con una serie de parámetros importantes en la ejecución, y que pueden modificar el comportamiento del algoritmo. Cómo modificar estos parámetros se explicará en detalle en el próximo apartado.

Al realizar el algoritmo se devolverá la rama calculada, y se devolverá en un formato de imagen que tendra el siguiente formato: nombre_funcion | fecha. Tras esto, se dará por finalizada la ejecución del algoritmo.

## Modificación de parámetros

Para modificar la ejecución del algoritmo contamos con ciertos parámetros. Todos estos parámetros se encuentran en las funciones nombre_funcionCalc(mode).

- A: arclength. Modificando este paŕametro la rama crecerá más o menos.
- PO: es el punto de silla
- P1: este punto es muy importante. Debe encontrarse a una distancia delta_k del punto P0 y además, debe estar desplazado en cierto ángulo. Como este punto se construye de la forma: p0 + movimiento(delta_k,angulo).
- Modificación de delta_k: después de calcular p1, siempre se modifica delta_k con ciertos valores. Esto se debe a que el punto p2 debe encontrarse a una distancia p1 calculada con la medida de contracción lineal dada por el autovalor. Así, la distancia de p1 a p2 sería:
  - distancia = (1/autovalor - 1). Además, se debe probar en un intervalo de la forma (distancia - 1/2*distancia, distancia + 1/2*distancia)
  - Por ejemplo: delta_k = delta_k*5.6*0.5, donde 45.6 es la contracción lineal calculada y 0.5 sería la distancia.

Todos estos parámetros se pueden modificar, pudiendo causar un comportamiento distinto del algoritmo en cada uno de los casos.

## Añadir un input

En el caso de que el usuario quisiera probar con funciones introducidas por él mismo, hemos creado el modo input.

Este modo se encuentra configurado para que solo funciones e inputCalc sean modificadas.

- funciones: se trata de una función que contiene a todas las funciones. Debajo de mode == "Input", el usuario tiene dispuesto un x y un y para que pueda meter su propia función.
- inputCalc: setrata de la función que contiene a todos los parámetros para el cálculo de la variedad. Es aconsejable que se siga el esquema seguido por todas las funciones del tipo nombre_funcionCalc:
 - Hacer una copia de delta_k.
 - Escribir p0 y p1.
 - Hacer la modificación correspondiente de delta_k.
 - Añadir la longitud a calcular deseada.
 - Ejecutar el algoritmo.
 - Restablecer el valor de delta_k.
 - Devolver el conjunto de puntos calculado.
