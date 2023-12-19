# Tarefa Nº2 - Posta en producción segura    
**Traballo OWASP - M3: Insecure Authentication/Authorization**  
***Yago Touriño Medrano***

# Índice
1. [Introducción](#introducción-y-análisis-de-la-vulnerabilidad)
2. [Escenarios de las Vulnerabilidades](#escenarios-de-las-vulnerabilidades)
3. [Escenario Práctico](#escenario-práctico)
4. [Bibliografía](#bibliografía)

# Introducción y análisis de la vulnerabilidad

La vulnerabilidad de esta tarea, la ***M3: Insecure Authentication/Authorization***  aborda deficiencias en los procesos de autenticación y autorización de una aplicación,dos elementos críticos para garantizar la protección de datos y sistemas.  
Consta, como el nombre indica, de dos puntos:  
- **Autenticación:**  
La autenticación insegura se refiere a la verificación de la identidad de los usuarios.
Los princiales puntos de ataque de esta vulnerabilidad, se deben a, por ejemplo:  
1. Almacenamiento inadecuado de las credenciales.
2. Contraseñas débiles.
3. Métodos de autenticación deficientes.
  
Para evitar estos problemas, un buen trabajo sería el **requerir contraseñas robustas**, o la **2FA** o **"Doble factor de autenticación"**, o laimplementación de **Seguridad biométrica**.


- **Autorización:**  
La autorización insegura se refiere a qué acciones puede realizar un usuario, o recursos a los que este tiene permitido acceder.  
Los princiales problemas a los que se expone nuestra aplicación frentea esta vulnerabilidad son:  
1. Accesos no autorizados a funciones de la aplicación.
2. Privilegios excesivos
  
Para evitar estos problemas, un buen trabajo sería el **gestionar correctamente la sesión de usuario**, o el **monitoreo de inicios de sesión**.

# Escenarios de las vulnerabilidades
### Escenario 1 - Contraseñas débiles
Nuestra aplicación, permite la creación de usuarios con credenciales deficientes en seguridad, por ejemplo, que se permita el uso de solo letras, y sin un requerimiento mínimo de caracteres.  
Los atacantes, podrían atacar muy facilmente nuestros usuarios utilizando aplicaciones de fuerza bruta en nuestra aplicación, utilizando diccionarios de contraseñas comunes disponibles en la red.  
### Escenario 2 - Falta de monitoreo de inicios de sesión
Nuestra aplicación, no tiene un control de sesiones de usuario cuando este se ha autenticado.  
Los atacantes, podrían interceptar sesiones para hacerse pasar por usuarios, y acceder a sus cuentas utilizando sus datos de sesión.

### Escenario 3 - Permisos inadecuados
Nuestra aplicación, da permisos con privilegios altos a los usuarios, permitiendoles a estos funciones a las que no deberían tener acceso.
Los atacantes, utilizando por ejemplo una de las dos vulnerabilidades anteriores, podría así acceder a más funciones de nuestra aplicación, como la modificación de usuarios, de las cuales un usuario "básico" no debería poder acceder.

# Escenario Práctico
[Enlace al video de youtube]()
# Bibliografía
[Web OWASP](https://owasp.org/www-project-mobile-top-10/2023-risks/m3-insecure-authentication-authorization)
[Tkinter Wiki](https://wiki.python.org/moin/TkInter)
[XML Elementtree](https://www.datacamp.com/tutorial/python-xml-elementtree)