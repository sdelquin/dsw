# Introducción a la programación web

Seguro que ya sabes exactamente qué es una **página web**, e incluso conozcas cuáles son los pasos que se suceden para que, cuando visitas una web poniendo su dirección en el navegador, la página se descargue a tu equipo y se pueda mostrar. Sin embargo, este procedimiento que puede parecer sencillo, a veces no lo es tanto. **Todo depende de cómo se haya hecho la página en cuestión**.

![Cliente-servidor](./images/client-server.jpg)

Cuando una **página web** se descarga al ordenador, su contenido define qué se debe mostrar en pantalla. **Este contenido está programado en un lenguaje de marcado**, formado por etiquetas, que habitualmente es **HTML**. Las etiquetas que componen la página indican el objetivo de cada una de las partes que la componen. Así, dentro de estos lenguajes hay etiquetas para indicar que un texto es un encabezado, que forma parte de una tabla, o que simplemente es un párrafo de texto.

Además, si la página está bien estructurada, la información que le indica al navegador el estilo con que se debe mostrar cada parte de la página estará almacenado en otro fichero, una **hoja de estilos** o **CSS** _(Abreviatura de "Hoja de estilos en cascada", del inglés Cascading Style Sheet - CSS)_. La hoja de estilos se encuentra indicada en la página web y el navegador la descarga junto a ésta. En ella nos podemos encontrar, por ejemplo, estilos que indican que el encabezado debe ir con tipo de letra Arial y en color rojo, o que los párrafos deben ir alineados a la izquierda.

![HTML&CSS](./images/html-and-css.png)

Estos dos ficheros se descargan a tu ordenador desde un servidor web como respuesta a una petición. El proceso es el que se indica a continuación:

1. **Tu ordenador solicita a un servidor web** una página con extensión `.html`
2. El servidor **busca esa página** en un almacén de páginas (cada una suele ser un fichero).
3. Si el servidor encuentra esa página, **la recupera**.
4. Y por último **se la envía al navegador** para que éste pueda mostrar su contenido (renderizado).

Este es un ejemplo típico de una comunicación **cliente-servidor**. El cliente es el que hace la **petición** e inicia la comunicación, y el servidor es el que recibe la petición y la atiende mediante una **respuesta**. En este contexto, **el navegador es el cliente web**.

![Request-Response](./images/request-response.jpg)

## Páginas web estáticas y dinámicas

Las páginas explicadas en el apartado anterior se llaman **páginas web estáticas**. Estas páginas se encuentran almacenadas en su forma definitiva, tal y como se crearon, y su contenido no varía. Son útiles para mostrar una información concreta, y mostrarán esa misma información cada vez que se carguen. La única forma en que pueden cambiar es si un programador la modifica y actualiza su contenido.

En contraposición a las páginas web estáticas existen las **páginas web dinámicas**. Estas páginas, como su propio nombre indica, se caracterizan porque su contenido cambia en función del escenario correspondiente (usuario identificado, acciones ejecutadas, configuración, etc.).

![Static vs Dynamic web](./images/static-vs-dynamic-web.jpg)

Dentro de las **páginas web dinámicas**, es muy importante distinguir **dos tipos**:

1. Aquellas que **incluyen código que ejecuta el navegador**. En estas páginas el código ejecutable, normalmente en lenguaje **JavaScript**, se incluye dentro del HTML y se descarga junto con la página. Cuando el navegador muestra la página en pantalla, ejecuta el código que la acompaña. Este código puede incorporar múltiples funcionalidades que pueden ir desde mostrar animaciones hasta cambiar totalmente la apariencia y el contenido de la página.

2. Sin embargo hay muchas páginas en Internet que no tienen extensión .html. Puede que tengan extensión .php o .asp o que incluso ni siquiera tengan extensión. En éstas, el contenido que se descarga al navegador es similar al de una página web estática. Lo que cambia es la forma en que se obtiene ese contenido. Al contrario de lo que vimos hasta ahora, esas páginas no están almacenadas en el servidor; más concretamente, el contenido que se almacena no es el mismo que después se envía al navegador. **El HTML de estas páginas se forma como resultado de la ejecución de un programa**, y esa ejecución tiene lugar en el servidor web.

El esquema de funcionamiento de una página web dinámica es el siguiente:

1. El **cliente web** (navegador) de tu ordenador **solicita** a un servidor web una **página web**.
2. El **servidor busca** esa página y la recupera.
3. En el caso de que se trate de una página web dinámica, es decir, que su contenido deba ejecutarse para obtener el HTML que se devolverá, **el servidor web contacta con el módulo responsable de ejecutar el código** y se lo envía.
4. Como parte del proceso de ejecución, puede ser necesario **obtener información de algún repositorio** _(cualquier almacén de información digital, normalmente una base de datos)_, como por ejemplo consultar registros almacenados en una base de datos.
5. El resultado de la ejecución será una página en **formato HTML**, similar a cualquier otra página web no dinámica.
6. El **servidor web envía el resultado** obtenido al navegador, que la procesa y muestra en pantalla.

Este procedimiento tiene lugar constantemente mientras consultamos páginas web. Por ejemplo, cuando consultas tu correo electrónico vía web, lo primero que tienes que hacer es introducir tu nombre de usuario y contraseña. A continuación, lo más habitual es que el servidor te muestre una pantalla con la bandeja de entrada, en la que aparecen los mensajes recibidos en tu cuenta. **Esta pantalla es un claro ejemplo de una página web dinámica**.

Obviamente, el navegador no envía esa misma página a todos los usuarios, sino que la **personaliza de forma dinámica** en función de quién sea el usuario que se conecte. Para generarla ejecuta un programa que obtiene los datos de tu usuario (tus contactos, la lista de mensajes recibidos) y con ellos compone la página web que recibes desde el servidor web.

### Ámbito de aplicación

Aunque la utilización de páginas web dinámicas parezca la mejor opción para construir un sitio web, no siempre lo es. Sin lugar a dudas, es la que más potencia y flexibilidad permite, pero **las páginas web estáticas tienen también algunas ventajas**:

1. No es necesario saber ~~programar~~ tanto para crear un sitio que utilice únicamente páginas web estáticas. **"Simplemente"** habría que manejar HTML y CSS, e incluso esto no sería indispensable: se podría utilizar algún programa de diseño web para generarlas.

2. La característica diferenciadora de las páginas web estáticas es que **su contenido nunca varía**, y esto en algunos casos también puede suponer una ventaja (mayor capacidad de cacheado, enlaces invariantes, motores de búsqueda, etc.).

Para que Google muestre un sitio web en sus resultados de búsqueda, previamente tiene que **indexar su contenido**. Es decir, un programa ("robot") recorre las páginas del sitio consultando su contenido y clasificándolo. Si las páginas se generan de forma dinámica, puede que su contenido, en parte o por completo, no sea visible para el buscador y por tanto no quede indexado. Esto nunca sucedería en un sitio que utilizase páginas web estáticas.

Para que un servidor web pueda procesar una página web dinámica, necesita
ejecutar un programa. Esta ejecución la realiza un módulo concreto, que puede estar integrado en el servidor o ser independiente. Además, puede ser necesario consultar una base de datos como parte de la ejecución del programa. Es decir, **la ejecución de una página web dinámica requiere una serie de recursos del lado del servidor**. Estos recursos deben instalarse y mantenerse.

**Las páginas web estáticas sólo necesitan un servidor web que se comunique con el navegador** para enviar dicha información. Y de hecho para ver una página estática almacenada en tu equipo no necesitas ni siquiera de un servidor web. Son archivos que pueden almacenarse en ficheros del disco duro y abrirse desde él directamente con un navegador web.

Pero si se decide hacer un sitio web utilizando páginas estáticas, ten en cuenta que tienen limitaciones. **La desventaja más importante** ya la comentamos anteriormente: la **actualización de su contenido** debe hacerse **de forma manual** editando la página que almacena el servidor web. Esto implica un mantenimiento que puede ser prohibitivo en sitios web con alta variabilidad de sus contenidos.

### Aplicaciones web

Las **aplicaciones web emplean páginas web dinámicas** para crear aplicaciones que se ejecuten en un servidor web y se muestren en un navegador. Se puede encontrar aplicaciones web para realizar múltiples tareas. Unas de las primeras en aparecer fueron las que se comentarion anteriormente, los clientes de correo.

Hoy en día existen aplicaciones web para multitud de tareas como procesadores de texto, gestión de tareas, o edición y almacenamiento de imágenes. Estas aplicaciones tienen ciertas ventajas e inconvenientes si las comparas con las aplicaciones tradicionales que se ejecutan sobre el sistema operativo de la propia máquina (aplicaciones nativas):

| Ventajas                                                                                                                                                                                                                                      | Inconvenientes                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **No es necesario instalarlas** en aquellos equipos en que se vayan a utilizar. Se instalan y se ejecutan solamente en un equipo, en el servidor, y esto es suficiente para que se puedan utilizar de forma simultánea desde muchos clientes. | **Dependemos de una conexión con el servidor** para poder utilizarlas. Si nos falla la conexión, no podremos acceder a la aplicación web.                                                                                                                                       |
| Como solo se encuentran instaladas en un equipo, **es muy sencillo gestionarlas** (hacer copias de seguridad de sus datos, corregir errores, actualizarlas).                                                                                  | Aún con conexión a internet, el "cuello de botella" de la velocidad de ejecución suele ser la **transmisión de datos** a través de la red. Esto puede ralentizar la aplicación web, sobre todo si la arquitectura no está bien diseñada para escalar con el número de usuarios. |
| **Se pueden utilizar en todos aquellos sistemas que dispongan de un navegador web**, independientemente de sus características (no es "tan" necesario un equipo potente) o de su sistema operativo.                                           |                                                                                                                                                                                                                                                                                 |

## Ejecución de código en el servidor y en el cliente

Cuando el navegador solicita a un servidor web una página, **es posible que antes de enviársela haya tenido que ejecutar, por sí mismo o por delegación, algún programa para obtenerla**. Ese programa es el que genera, en parte o en su totalidad, la página web que llega al cliente. En estos casos, **el código se ejecuta en el entorno del servidor web** y hablamos de **SERVER SIDE RENDERING (SSR)**:

![Server Side Rendering](./images/server-side-rendering.png)

Además, cuando una página web llega al navegador, es también posible que incluya algún programa o fragmentos de código que se deban ejecutar en el cliente. Ese código, normalmente en **lenguaje JavaScript, se ejecutará en el navegador** y, además de poder modificar el contenido de la página, también puede llevar a cabo acciones como la animación de textos u objetos de la página o la comprobación de los datos que introduces en un formulario.

**Estas dos tecnologías se complementan una con la otra**. Así, volviendo al ejemplo del correo web, el programa que se encarga de obtener tus mensajes y su contenido de una base de datos se ejecuta en el entorno del servidor, mientras que tu navegador ejecuta, por ejemplo, el código encargado de avisarte cuando quieres enviar un mensaje y te has olvidado de poner un texto en el asunto.

Esta división es así porque **el código que se ejecuta en el cliente** web (en el navegador) no tiene, o mejor dicho **tradicionalmente no tenía, acceso a los datos que se almacenan en el servidor**. Es decir, cuando en tu navegador querías leer un nuevo correo, el código Javascript que se ejecutaba en el mismo no podía obtener de la base de datos el contenido de ese mensaje. La solución era crear una nueva página en el servidor con la información que se pedía y enviarla de nuevo al navegador.

Sin embargo, es posible realizar programas en los que el código JavaScript que se ejecuta en el navegador pueda comunicarse con un servidor de Internet para obtener información con la que, por ejemplo, modificar la página web actual.

En nuestro ejemplo, cuando pulsas con el ratón encima de un correo que quieres leer, la página puede contener código Javascript que detecte la acción y, en ese instante, consultar a través de Internet el texto que contiene ese mismo correo y mostrarlo en la misma página, modificando su estructura en caso de que sea necesario. Es decir, sin salir de una página poder modificar su contenido en base a la información que se almacena en un servidor de Internet. En este escenario podemos hablar de **SPA (Single Page Applications)** o aplicaciones de una única página, algo muy relacionado con el llamado **CLIENT SIDE RENDERING (CSR)**:

![Client Side Rendering](./images/client-side-rendering.png)

En este módulo vas a aprender a crear aplicaciones web que se ejecuten en el lado del servidor o lo que se conoce en la industria como **desarrollo backend**. Otro módulo de este mismo ciclo, Desarrollo Web en Entorno Cliente, enseña las características de la programación de código que se ejecuta en el navegador web o lo que se conoce como **desarrollo frontend**.

![Frontend vs backend](./images/front-vs-back.jpg)

**Muchas de las aplicaciones web actuales utilizan estas dos tecnologías**: la ejecución de código en el servidor y en el cliente. Así, el código que se ejecuta en el servidor genera páginas web que ya incluyen código destinado a su ejecución en el navegador. Aquellas personas que se dedican al desarrollo de una aplicación en toda su extensión ("frontend" + "backend") se dice que trabajan en **desarrollo fullstack**.

# Tecnologías para programación web del lado del servidor

Cuando se programa una **aplicación** se hace utilizando un **lenguaje de programación**. Por ejemplo, utilizas el lenguaje Python para crear aplicaciones que se ejecuten en distintos sistemas operativos. Al programar cada aplicación utilizas ciertas herramientas como un entorno de desarrollo o librerías de código. Además, una vez acabado su desarrollo, esa aplicación necesitará ciertos componentes para su ejecución, como por ejemplo un intérprete dentro de un entorno virtual.

En este bloque veremos **distintas tecnologías** que se pueden utilizar para **programar aplicaciones** que se ejecuten en un **servidor web**, y cómo se relacionan unas con otras. Analizaremos las ventajas e inconvenientes de utilizar cada una, y qué lenguajes de programación se deben aprender para utilizarlas.

Los **componentes principales** con los que se debe contar para ejecutar aplicaciones web en un servidor son los siguientes:

1. Un **servidor web** para recibir las peticiones de los clientes web (normalmente navegadores) y enviarles la página que solicitan (una vez generada puesto que hablamos de páginas web dinámicas). El servidor web debe conocer el procedimiento a seguir para generar la página web: qué módulo se encargará de la ejecución del código y cómo se debe comunicar con él.

2. El **módulo encargado de ejecutar el código** o programa y generar la página web resultante. Este módulo debe integrarse de alguna forma con el servidor web, y dependerá del lenguaje y tecnología que utilicemos para programar la aplicación web.

3. Un **sistema gestor de base de datos**. Este módulo no es estrictamente necesario pero en la práctica se utiliza en todas las aplicaciones web que manejan ciertas cantidades de datos o información.

4. El **lenguaje de programación** que utilizarás para desarrollar las aplicaciones.

Además de los componentes a utilizar, también es importante decidir cómo vas a **organizar el código** de la aplicación. Muchas de las arquitecturas que se usan en la programación de aplicaciones web te ayudan a estructurar el código de las aplicaciones en **capas o niveles**.

El motivo de dividir en capas el diseño de una aplicación es que se puedan **separar las funciones lógicas** de la misma, favoreciendo la reutilización y el desacoplamiento de los componentes.

En una aplicación se puede distinguir, de forma general, funciones de **presentación** (se encarga de dar formato a los datos para presentárselo al usuario final), **lógica de negocio** (utiliza los datos para ejecutar un proceso y obtener un resultado) y **persistencia** (que mantiene los datos almacenados de forma organizada).

![Capas desarrollo web](./images/webdev-layers.png)

## Arquitecturas y plataformas

La primera elección antes de comenzar a programar una aplicación web es **elegir la arquitectura** a utilizar.

Podríamos diferenciar tres tipos de aspectos en relación con la arquitectura de una aplicación web:

1. Aspectos software.
2. Aspectos hardware.
3. Aspectos empresariales.

### Aspectos software

1. ¿Qué lenguaje de programación se utilizará?
2. ¿Necesito un framework web? ¿Cuál se adapta mejor al proyecto?
3. ¿Qué modelo de ejecución es el más adecuado? ¿SSR o CSR?
4. ¿Necesito persistencia? ¿Qué base de datos se utilizará?
5. ¿Base de datos relacional vs clave-valor? ¿Puedo usar ambas?
6. ¿Sobre qué servidor web se va a desplegar la aplicación?
7. ¿Qué servidor de aplicación se requiere?
8. ¿Qué tipo de licencia voy a establecer para la aplicación que desarrolle?

### Aspectos hardware

1. ¿Qué tipo de infraestructura hay disponible?
2. ¿Necesito infraestructura "on-premise" o "cloud"?
3. ¿Qué coste/beneficio me proporciona cada solución?
4. ¿Qué requerimientos debe tener la(s) máquina(s) del proyecto?
5. ¿Cómo se gestiona la escalabilidad de la aplicación?

### Aspectos empresariales

1. ¿Qué tamaño tiene el proyecto?
2. ¿Qué lenguajes de programación conozco? ¿Vale la pena el esfuerzo de aprender uno nuevo?
3. ¿Voy a usar herramientas de código abierto o herramientas propietarias? ¿Cuál es el coste de utilizar soluciones comerciales?
4. ¿Voy a programar la aplicación yo solo o formaré parte de un equipo de desarrollo?

Estudiando las respuestas a estas y otras preguntas, se podrá ver qué arquitecturas se adaptan mejor a la aplicación y cuáles no son viables.

# Lenguajes

La elección del lenguaje de programación es importante pero no decisiva. Hay que tener en cuenta otros factores como se ha comentado en la sección anterior.

En cualquier caso, cuando hablamos de programación del lado del servidor, los lenguajes de programación tienen características que los diferencian tanto en tiempo de desarrollo, compilación y ejecución.

Si nos centramos en **desarrollo web para entorno servidor** podemos citar algunas de las opciones disponibles:

| Lenguaje                                                                            | Framework                                                               |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [Java](https://www.java.com/es/) / [Kotlin](https://kotlinlang.org/)                | [Spring Boot](https://spring.io/projects/spring-boot)                   |
| [PHP](https://www.php.net/manual/es/intro-whatis.php)                               | [Laravel](https://laravel.com/)                                         |
| [JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript) / [Typescript]() | [Express](https://expressjs.com/es/) / [Node.js](https://nodejs.org/es) |
| [Ruby](https://www.ruby-lang.org/es/)                                               | [Ruby on Rails](https://rubyonrails.org/)                               |
| [C#](https://learn.microsoft.com/es-es/dotnet/csharp/)                              | [ASP.NET](https://dotnet.microsoft.com/es-es/apps/aspnet)               |
| [Go](https://go.dev/)                                                               | [Gin](https://gin-gonic.com/)                                           |
| [Python](https://www.python.org/)                                                   | [Django](https://www.djangoproject.com/)                                |

> 💡 Todos los lenguajes tienen ventajas e inconvenientes. El lenguaje de programación debe ser una herramienta para solucionar el problema, no un fin en sí mismo. Explora las distintas posibilidades y trata de encontrar aquella herramienta que mejor se adapte al proyecto.

## Framework web

Los llamados "framework web" constituyen un conjunto de módulos que **permiten el desarrollo ágil de aplicaciones web** mediante la aportación de librerías y/o funcionalidades ya creadas.

En su gran mayoría, los framework web se basan en una arquitectura "MVC" o "Modelo-Vista-Controlador":

![Modelo-Vista-Controlador](./images/mvc.jpg)

## Integración con lenguajes de marcas

La respuesta gráfica que se devuelve al usuario consiste en **integrar parte del código del programa en medio de las etiquetas HTML** de la página web, dando lugar a las **plantillas**. De esta forma, el contenido que no varía de la página se puede introducir directamente en HTML mientras que el lenguaje de programación se utilizará para todo aquello que pueda variar de forma dinámica.

Este mecanismo de "renderizado" de las plantillas se realiza mediante un **motor de plantillas**.

## Integración con el servidor web

La comunicación entre un cliente web o navegador y un servidor web se lleva a cabo gracias al **protocolo HTTP**. En el caso de las aplicaciones web, HTTP es el vínculo de unión entre el usuario y la aplicación en sí. Cualquier introducción de información que realice el usuario se transmite mediante una petición HTTP, y el resultado que obtiene le llega por medio de una respuesta HTTP.

En el lado del servidor, estas peticiones son procesadas por el servidor web. Es por tanto el servidor web el encargado de decidir cómo procesar las peticiones que recibe. Cada una de las arquitecturas que acabamos de ver tiene **una forma de integrarse con el servidor web** para ejecutar el código de la aplicación.

La integración de los módulos de procesamiento con el servidor web es un objetivo claro del módulo "Despliegue de aplicaciones web" de 2º curso de Desarrollo de Aplicaciones Web.
