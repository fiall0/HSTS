# HTTP Strict Transport Security (HSTS)
Este script en Python permite habilitar automáticamente la politica de seguridad **HSTS (HTTP Strict Transport Security)** en todas las zonas configuradas en una cuenta de Cloudflare mediante su API.

**¿Que hace el script?**

1. **Autenticacion:** Se conecta a la API de Cloudflare usando un token de acceso (`API_TOKEN`).
2. **Listado de Zonas:** Recupera todas las zonas (dominios) asociadas a la cuenta, manejando la paginacion correctamente.
3. **Configuracion de HSTS:** Por cada zona, activa la cabecera `Strict-Transport-Security` con los siguientes parametros:

   * `enabled`: `true` (activa HSTS)
   * `max_age`: `31536000` segundos (1 año)
   * `include_subdomains`: `true` (se aplica a subdominios)
   * `preload`: `true` (opcional para la lista de preload de navegadores)
   * `nosniff`: `true` (previene la deteccion de tipo MIME)

**¿Para que sirve?**
Aplicar HSTS mejora la seguridad de tus sitios forzando el uso de HTTPS y evitando ataques de tipo downgrade o MITM (Man-in-the-Middle).

**Requisitos:**

* Python 3.x
* Biblioteca `requests`
* Un token de API valido de Cloudflare con permisos de lectura y edicion de zonas.
