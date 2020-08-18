# 0x10. Python - Network #0

## Resources:books:
Read or watch:
* [HTTP (HyperText Transfer Protocol)](https://intranet.hbtn.io/rltoken/UGtqGaRv-IUx4V7_d4HyRQ)
* [HTTP Cookies](https://intranet.hbtn.io/rltoken/ubO0VPV2T3D77jyfc0c1Xw)

---
## Learning Objectives:bulb:
What you should learn from this project:

* What a URL is
* What HTTP is
* How to read a URL
* The scheme for a HTTP URL
* What a domain name is
* What a sub-domain is
* How to define a port number in a URL
* What a query string is
* What an HTTP request is
* What an HTTP response is
* What HTTP headers are
* What the HTTP message body is
* What an HTTP request method is
* What an HTTP response status code is
* What an HTTP Cookie is
* How to make a request with cURL
* What happens when you type google.com in your browser (Application level)

---

### [0. cURL body size](./0-body_size.sh)
* Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response


### [1. cURL to the end](./1-body.sh)
* Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response


### [2. cURL Method](./2-delete.sh)
* Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response


### [3. cURL only methods](./3-methods.sh)
* Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.


### [4. cURL headers](./4-header.sh)
* Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response


### [5. cURL POST parameters](./5-post_params.sh)
* Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response


### [6. Find a peak](./6-peak.py)
* Technical interview preparation: 


### [7. Only status code](./100-status_code.sh)
* Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.


### [8. cURL a JSON file](./101-post_json.sh)
* Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.


### [9. Catch me if you can!](./102-catch_me.sh)
* Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.




#### Algunas palabras / vocabulario
Primero, realmente te animo a leer la publicación de Bilal sobre los encabezados HTTP aquí

URL : “Localizador uniforme de recursos”, define la dirección web de un recurso específico. Una URL se compone de 4 partes:
protocolo : http://o https://o ftp://… => define también en qué puerto se solicitará el servidor
host : www.example.como intranet.hbtn.io… => será resuelto por el DNS = nombre de host a la dirección IP
ruta : /index.htmlo /states/1/cities… => ruta desde la raíz del sitio web o servicio web en este host
cadena de consulta : ?name=Jono ?q=dress&color=FF0000… => siempre comienza con el símbolo ? y seguido de una lista de parámetros (clave = valor) separados por el símbolo &
solicitud : acción del cliente para enviar "datos" a una URL específica y devolver una respuesta
respuesta : resultado de una solicitud de devolución del servidor al cliente
Método HTTP : o llamado "verbo" para una RestAPI. Es solo parte del protocolo HTTP (solicitud http y https):
GET: método más común para recuperar información del servidor (lectura). Cuando navega en Google u otro sitio web, su navegador web realiza solicitudes GET a cada sitio web para recuperar HTML / CSS / JS, etc. para representar correctamente el sitio web. El cliente puede enviar información al servidor mediante una cadena de consulta.
POST: se usa para enviar datos al servidor (escribir) contener en el cuerpo de la solicitud (ver más abajo)
HEAD: igual que GET pero con una respuesta vacía. Se utiliza principalmente para comprobar si un recurso está disponible pero sin obtenerlo.
PUT/ PATCH: para actualizar un recurso con datos contenidos en el cuerpo de la solicitud
DELETE: para eliminar un recurso en el servidor (utilizado principalmente para una RestAPI)
otros ...
Encabezado : un encabezado es un hash de información de valor-clave. Puede tener un encabezado de solicitud (información del cliente al servidor), pero también un encabezado de respuesta (servidor a cliente). Los encabezados son realmente útiles y algunos "valores-claves" están estandarizados:
User-Agent: del cliente al servidor para describir al cliente. Ejemplo: Chrome utilizado como User-Agent: "Mozilla / 5.0 (Macintosh; Intel Mac OS X 10 11 6) AppleWebKit / 537.36 (KHTML, como Gecko) Chrome / 51.0.2704.103 Safari / 537.36"
Origin: del cliente al servidor para dar información de dónde viene la solicitud al servidor
Content-Type: define cómo se puede leer el cuerpo. Por ejemplo: "http://swapi.co/api/planets/1/" => "Content-Type: application / json" porque el cuerpo de la respuesta es un JSON
Content-Length: tamaño en Bytes del cuerpo de la solicitud / respuesta
otros
Cuerpo : un cuerpo son Bytes transmitidos en HTTP. Puede tener un cuerpo de solicitud (parámetros del cliente al servidor) y un cuerpo de respuesta (devolver el resultado del servidor al cliente)
Codificación de URL : acción para transcodificar una cadena normal en una cadena de consulta. También se utiliza para el cuerpo de la solicitud en caso deContent-Type: application/x-www-form-urlencoded
Algunas opciones interesantes:

Modo detallado
-vvv imprimirá todos los encabezados y transferirá el estado de una solicitud / respuesta

#### Dirección de salida
-o redirigir el cuerpo de respuesta de una solicitud a un archivo:
```
i-love-curl $ curl "http://www.google.com" -o google_homepage.html
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 11279    0 11279    0     0   145k      0 --:--:-- --:--:-- --:--:--  146k
i-love-curl $ ls
google_homepage.html
i-love-curl $
o a nada:

i-love-curl $ curl "http://www.google.com" -o /dev/null
i-love-curl $ 
```

#### Método HTTP
-X definir qué HTTP:

-X GET: para hacer una solicitud GET (por defecto)
-X POST: para hacer una solicitud POST
-X PUT: para hacer una solicitud PUT
-X DELETE: para hacer una solicitud DELETE
Cuerpo / parámetros
Todos los parámetros de la cadena de consulta se pueden agregar directamente a la URL. Pero para otro método HTTP, debe usar el atributo -d. Puede usar solo uno y debe estar codificado en URL (separado por el símbolo &) o múltiples. Por defecto, elContent-Type: application/x-www-form-urlencoded

Agregue un nuevo estado a una RestAPI:

```
i-love-curl $ curl "http://localhost:5555/states" -X POST -d "name=California&code=CA"
{ "id": 12, "name": "California", "code": "CA" }
i-love-curl $ 
o para actualizar un estado a RestAPI:

i-love-curl $ curl "http://localhost:5555/states/12" -X PUT -d "name=California Forever" -d "code=CAF"
{ "id": 12, "name": "California Forever", "code": "CAF" }
i-love-curl $ 
y si codifica el cuerpo de la solicitud como JSON (estableciendo un tipo de contenido correcto en el encabezado) y su servidor lo entiende:

i-love-curl $ curl "http://localhost:5555/states" -X POST -H "Content-Type: application/json" -d "{ \"name\": \"California\", \"code\": \"CA\" }"
{ "id": 13, "name": "California", "code": "CA" }
i-love-curl $
```

Valores de encabezado
-H establecerá su parámetro en la parte Encabezado.

Por ejemplo, para enviar un encabezado personalizado (por convención, comenzará por X-):
```
i-love-curl $ curl "http://localhost:5555/states" -X GET -H "X-Application-id: 14"
[{ "id": 12, "name": "California Forever", "code": "CAF" }, { "id": 13, "name": "California", "code": "CA" }]
i-love-curl $ 
o sobrescribir un encabezado estándar (aquí Content-Type y User-Agent):

i-love-curl $ curl "http://localhost:5555/states" -X GET -H "X-Application-id: 14" -H "Content-Type: text/xml" -H "User-Agent: MyCustomClient"
<xml>
  <states>
    <state id="12" code="CAF">
      <name>California Forever</name>
    </state>
    <state id="13" code="CA">
      <name>California</name>
    </state>
  </states>
</xml>
i-love-curl $ 
```


---

## Author
* **Deiwin Ignacio Monsalve Altamar** - [Deiwin-Ignacio-Monsalve-Altamar](https://github.com/Deiwin-Ignacio-Monsalve-Altamar)