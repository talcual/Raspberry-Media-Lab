

RaspiMedia

Proyecto realizando para fines de aprendizaje..

para el proyecto se utilizo Luvit y CherryPy con un toque de Bootstrap.


==============================================================================

Antes que todo porque escogi Luvit y CherryPy. una respuesta simple. porque son livianos y el laboratorio lo hice utilizando
mi raspberry pi 1.


lo primero que hacemos es clonar el repo. debemos preparar el entorno.

Para instalar Luvit 

Primer dejemos claro que es luvit... luvit es a lua, lo que nodejs es a javascript. con esa oracion creo
que dejo claro. jejej

para hacer la instalacion debemos verificar que tenemos primero Lua instalado, este viene por defecto en algunos 
sistemas linux, pero por si no esta instalado lo instalamos jeje 

apt install lua 
dnf install lua
yum install lua 

el que te sirva, pero ahora toca instalar el sistema de instalacion de paquetes de Lua, el cual es LuaRocks, es como un npm de node.
para hacerlo te recomiendo seguir este enlace => https://github.com/luarocks/luarocks/wiki/Download despues de esto instalamos Luvit
pueden entrar a la web oficial y conocer un poco mas https://luvit.io/install.html lista esta parte... tenemos el servidor de archivos listo.


Instalando CherryPy.

Bueno aqui decidi utilizar CherryPy porque me parece un buen framework para python, para hacer la respectiva instalacion te recomeindo
vallas a su documentacion oficial... http://docs.cherrypy.org/en/latest/ es lo mejor. 


instalado CherryPy y Luvit solo falta poner a correr ambos.

utilizando un nohup corremos files.lua y el servidor cherry.



sudo nohup luvit files.lua &
sudo nohup python server.py &


en la carpeta files, se deben colocar los archivos, para que puedan ser entregados por files.lua, en una proxima version intentare colocar esos archivos en una usb,
para que se automonte y hacer mas dinamico nuestro sistema de medio simple.

recuerda seguirmeeeee jejeje. 

http://www.luistoscano.com