# HTTP Strict Transport Security (HSTS)
Este script en Python permite habilitar automáticamente la política de seguridad **HSTS (HTTP Strict Transport Security)** en todas las zonas configuradas en una cuenta de Cloudflare mediante su API.

**¿Qué hace el script?**

1. **Autenticación:** Se conecta a la API de Cloudflare usando un token de acceso (`API_TOKEN`).
2. **Listado de Zonas:** Recupera todas las zonas (dominios) asociadas a la cuenta, manejando la paginación correctamente.
3. **Configuración de HSTS:** Por cada zona, activa la cabecera `Strict-Transport-Security` con los siguientes parámetros:

   * `enabled`: `true` (activa HSTS)
   * `max_age`: `31536000` segundos (1 año)
   * `include_subdomains`: `true` (se aplica a subdominios)
   * `preload`: `true` (opcional para la lista de preload de navegadores)
   * `nosniff`: `true` (previene la detección de tipo MIME)

**¿Para qué sirve?**
Aplicar HSTS mejora la seguridad de tus sitios forzando el uso de HTTPS y evitando ataques de tipo downgrade o MITM (Man-in-the-Middle).

**Requisitos:**

* Python 3.x
* Biblioteca `requests`
* Un token de API válido de Cloudflare con permisos de lectura y edición de zonas.
