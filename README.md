# Reto_Envio

 Miembros del equipo:
 
  - Manel Díaz

  - Ruben Alsasua

  - Eneko Saez

 Enlace a github: https://github.com/ManelDiaz/Reto_Envio

 Descripción del proyecto:

    El proyecto se basa en montar un broker MQtt utilizando 2 contenedores, para el publicador y para el suscriptor
    utilizando una autentificación basada en certificados de cliente servidor. 

    Para la realización del proyecto se han utilizado las siguientes tecnologías:
    
      - Docker-compose para levantar los contenedores
      
      - Dashboard de Django para poder ver de forma mas visual el envio y recepción de mensajes
      
      - OpenSSL para crear una Autoridad Certificadora (CA)

      - Mosquitto MQtt como broker

      - Python (Paho-MQtt) para producir y compartir datos de forma segura 

  Pasos seguidos:

    Para la realización del proyecto se han seguido los siguientes pasos:

      - Para empezar se crearon los contenedores utilizando docker compose y se realizaron las configuraciones iniciales el 
        el archivo docker-compose.yml. Además, se configuraron los mensajes sin credenciales para poder povar las configuraciones
        añadidas. 

      - Para continuar, se desarrolló el cliente MQtt en Python, para ello se utilizó la librería paho-mqtt, debido a que ofrecia una manera segura y 
        sencilla de conectar aplicaciones de Python con un broker MQtt. 
      
      - A continuacion se creo la aplicación de Django con el cual se pueden enviar y recibir los mensajes. Al enviar los mensajes 
        se alamacenan en una base de datos db_sqlite y se visualizan en un interfaz web. 

      - Al comprobar que los mensajes sin certificados funcionaban correctamente, se empezó a desarrollar la conexión segura con los certificados. 


  Instrucciones de uso:

    Para poder ejecutar ek proyecto correctamente, es necesario realizar los siguientes pasos:

      1. Clonar el repositorio, utilizando el siguiente comando: git clone https://github.com/ManelDiaz/Reto_Envio.git

      2. Levantar los contenedores mediante el comando 'docker-compose up -d' en la terminal de WSL. 

      3. Después de levantar los contendores se puede buscar en el navegador 'http://localhost:8000' para ver la interfaz del publicador y 
         http://localhost:8001' para la del suscriptor. 

      4. Para poder producir y consumir los mensajes desde la terminal es necesario utilizar los siguientes comandos. 
      
      
  Posibles vías de mejora:


  Problemas/ Retos encontrados:


  Alternativas posibles:
    
    
