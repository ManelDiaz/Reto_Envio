# Reto_Envio

 Miembros del equipo:
 
  - Manel Díaz

  - Ruben Alsasua

  - Eneko Saez

 Enlace a github: https://github.com/ManelDiaz/Reto_Envio

 Descripción del proyecto:

    El proyecto se basa en montar un broker MQtt utilizando 3 contenedores, para el publicador, para el suscriptor y 
    para el broker utilizando una autentificación basada en certificados de cliente servidor. 

    Para la realización del proyecto se han utilizado las siguientes tecnologías:
    
      - Docker-compose para levantar los contenedores
      
      - Dashboard de Django para poder ver de forma mas visual el envio y recepción de mensajes
      
      - OpenSSL para crear una Autoridad Certificadora (CA)

      - Mosquitto MQtt como broker

      - Python (Paho-MQtt) para producir y compartir datos de forma segura 

  Pasos seguidos:

    Para la realización del proyecto se han seguido los siguientes pasos:

      - Para empezar se crearon los contenedores utilizando docker compose y se realizaron las configuraciones iniciales el 
        el archivo docker-compose.yml. Además, se configuraron los mensajes sin credenciales para poder probar las configuraciones
        añadidas. 

      - Para continuar, se desarrolló el cliente MQtt en Python, para ello se utilizó la librería paho-mqtt, debido a que ofrecia una manera segura y 
        sencilla de conectar aplicaciones de Python con un broker MQtt. 
      
      - A continuación, se creo la aplicación de Django con la cual se pueden enviar y recibir los mensajes. Al enviar los mensajes 
        se alamacenan en una base de datos db_sqlite y se visualizan en una interfaz web. 

      - Al comprobar que los mensajes sin certificados funcionaban correctamente, se empezó a desarrollar la conexión segura con los certificados. 


  Instrucciones de uso:

    Para poder ejecutar el proyecto correctamente, es necesario realizar los siguientes pasos:

      1. Clonar el repositorio, utilizando el siguiente comando: git clone https://github.com/ManelDiaz/Reto_Envio.git

      2. Levantar los contenedores mediante el comando 'docker-compose up -d' en la terminal de WSL. 

      3. Después de levantar los contendores se puede buscar en el navegador 'http://localhost:8000' para ver la interfaz del publicador y 
         http://localhost:8001' para la del suscriptor. 

      4. Para poder producir y consumir los mensajes desde la terminal es necesario utilizar los siguientes comandos: 
      
      
  Posibles vías de mejora:

    Para poder mejorar el proyecto realizado se podrían haber implementado las siguientes vías de mejora:
    
      - Crear una interfaz web mas amigable.
      
      - Mejorar la gestión de errores y logs para facilitar la depuración, sin necesidad de realizar prints en la consola.

  Problemas/ Retos encontrados:
  
    Durante la realizaón del proyecto se encontraron diferentes problemas, entre los que destancan:
    
       - Problemas con los permisos de los archivos de los certificados. Al no tener los permisos necesarios el sistema sacaba errores
         al intentar acceder a los certificados. Finalmente, pudo ser solucionado con el siguiente comando: sudo chmod -R 777 el_archivo.

       - Incompatibilidad entre claves y certificados. Se detectó que los valores MD5 de los certificados y las claves del publicador 
         y suscriptor no coincidían, lo que impedía una correcta autenticación. Para solucionarlo, fue necesario regenerar tanto los 
         certificados como las claves correspondientes.
    

  Alternativas posibles:

    Las siguientes podrían ser al ternativas posibles a implemnetar en el proyecto:
    
      - Utilizar PostgreSQL como base de datos en vez de SQLite. Tiene un mejor rendimiento en grandes volúmenes de datos, en comparación a 
        SQLite que es más limitado.

      - Utilizar EMQX como broker. En comparación a Mosquitto, EMQX tiene un soporte para el clustering, lo que quiere decir que si un nodo
        falla sigue funcionando sin interrupciones. Además, permite manejar mas de 100 millones de conexiones simultáneas. 
        https://www.emqx.com/en/blog/emqx-vs-mosquitto-2023-mqtt-broker-comparison
      
  
   
