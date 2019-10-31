<!--
.. title: Reseña de Offcloud y Rclone
-->


Hace unos meses, cuando mi disco externo de ~640 GB (~598 GiB) dejó de funcionar, decidí comprar  almacenamiento en la nube. Después de investigar por varios días, decidí comprar el servicio premium de [Onedrive] (1TiB por 69€/año). Tras hacer esto, pronto me di cuenta de que un disco externo me venía mejor por mi velocidad de Internet (tengo ~3Mb de bajada y ~1Mb de subida). Pero ya que mi disco externo dejó de funcionar porque se me cayó alsuelo, no quería comprarme otro. Entonces, ¿qué opciones tenía? ¿Había un servicio para descargarme cosas  directamente a la nube?
[Onedrive]: https://onedrive.live.com

## Offcloud

[Offcloud] es un servicio que permite hacer tres cosas:
[Offcloud]: https://offcloud.com
* Descargar cosas usándolo como proxy (*"Instant downloading"*);
* Guardar cosas temporalmente en la nube de Offcloud (*"Cloud backup"*);
* Descargar cosas a uno de tus servicios de nubes de almacenamiento (Dropbox, Onedrive, Google Drive...) o a través de ftp o WebDAV (*"Remote upload"*).

Pero seamos más específicos sobre estas "cosas". Pueden ser:

* Enlaces directos y páginas web (estas últimas pueden ser descargadas como html o pdf)
* Vídeos y archivos de varios servicios de almacenamiento (gratis y de pago) ([lista de sitios soportados])
* Archivos torrent y enlaces magnet
* Archivos .nzb
[lista de sitios soportados]: https://offcloud.com/#/sites
El sistema es bastante sencillo. Pegas un link o subes un archivo torrent o .nzb, eliges tu método de descarga y esperas a que termine. Luego, puedes borrar la entrada de la lista de descargas (o el archivo, si está en la nube de Offcloud), o descargarlo en agún otro lugar. Puedes descargar tres enlaces al mes gratuitamente. Si eso no es suficiente, puedes comprar enlaces ilimitados para un mes o para un año, o comprar solo algunos enlaces. Tiene una API que te permite añadir enlaces desde otras aplicaciones, tiene plugins para gestores de descarga y navegadores, y funciona con [IFTTT] y [Zapier]. Y por supuesto, las descargas a la nube de Offcloud o alguno de tus servicios de almacenamiento funcionan incluso si apagas tu equipo.
[IFTTT]: https://ifttt.com
[Zapier]: https://zapier.com
[Regístrate en Offcloud](https://offcloud.com/?=9ee9276b) ([Enlace sin afiliación](https://offcloud.com))

Bueno, esto es genial. Puedo subir archivos a mi nube, a una velocidad mucho mayor que la de mi conexión de casa. Pero el espacio de mi ordenador está bastante limitado (tengo un disco SSD de ~103GiB), así que no puedo descargar muchos archivos a mi equipo si quiero pasarlos a, por ejempo, un lápiz de memoria USB. Por suerte, hay un programa para solucionar esto.

## Rclone

[Rclone] te permite gestionar tus servicios en la nube sin necesidad de sincronizarlos ni abrir un navegador. Esto incluye:

* Transferir archivos y carpetas entre nubes, o entre carpetas de la misma nube;
* Transferir archivos y carpetas entre tu equipo (y los dispositivos conectados a él) y la nube;
* Renombrar y borrar archivos de la nube sin descargar nada; y
* Acceder una nube por http, WebDAV o Fuse.

Te permite aplicar filtros para gestionar archivos y carpetas, así que no te hace falta recordar nombres de carpetas y archivos largos (yo los uso solamente para esto) , o para filtrar basándote en otros criterios. Se usa por línea de órdenes, y está disponible para Windows, Linux y Mac. Y es libre y de código abierto.

[Rclone]: https://rclone.org/

## Conclusión

Este es el procedimiento que uso ahora: descargo uno o más archivos utilizando [Offcloud] a [Onedrive], y luego lo copio a un lápiz de memmoria USB (que, estaréis de acuerdo conmigo, es menos propenso a caídas) usando [Rclone]. Y mientras tanto, ahorro espacio en disco y ancho de banda.
