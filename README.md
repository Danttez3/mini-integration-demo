# mini-integration-demo
Este es el resulta de mis primeros pasos en el Mundo de la Programación
## ¿Qué hace el Script?
Aunque Git es un control de versiones como todos lo sabemos🫠, he indagado un poco en el ámbito de Python para crear un Script sencillo, el cuál imprimirá una pequeña definición de los comandos más comunes utilizados en el control de versiones, este se realizará a partir de una lista de opciones que serán entregadas al usuario final de la "App"🎯. Ofreciendo una lista pequeña de opciones en diferentes parámetros basados en las respuestas proporcionadas por el usuario final🧪.
## ¿Cómo construir la imagen de Docker?📄
  1. 🟢 FROM: En esta versión usaré una etiqueta "python:alpine"
  2. 🟢 WORKDIR: Cómo base común se usará "/app" para gestionar el directorio
  3. 🟢 COPY: Se agregaran a al directorio el script/programa de python llamado "Definiciones.py", así como el fichero "Requirements.txt"
  4. 🟡 Ejecutaremos los comandos básicos en la imagen utilizando la instrucción RUN🏃‍♂️
  5. 🟢 CMD: Definiremos los comandos que se utilizaran al iniciar el contenedor ["Python", "Definiciones.py]
## ¿Cómo ejecutar el contenedor?🖥️
Principalmente, la idea será que se ejecute de manera local descargando la imagen y ejecutando el contenedor contenedor en una terminal. Sin embargo, esto normalmente es posible para usuarios que tienen Docker en sus equipos, pero como quiero empezar a ahondar un poco más también me gustaría crear un ejecutable de mi aplicación que pueda compartir con amigos y familia. De igual manera la comunidad de GitHub también puede acceder a este y sugerir cambios o demás. ☘️
# Mi primer programa en Python
Durante el transcurso de los módulos vistos, siempre se mencionaba un tal "Python". Al indagar un poco más descubrí que no es más que uno de los Lenguajes de Programación💻 más utilizados a nivel mundial.
Aunque ahondaré mucho más en él cuando llegue el momento, era importante conocer lo más básico de Python junto con algunas definiciones que me ayudarán a crear mi script. Estas son: 
  1.  Variables (Qué son, Cómo se usan, Para qué sirven) 💬
  2.  Funciones ("If", "Else", "Print") 👀
