import requests

# === CONFIGURACIÓN ===
API_TOKEN = "tu_api_key"  
API_BASE = "https://api.cloudflare.com/client/v4"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# === OBTENER TODAS LAS ZONAS ===
def get_zones():
    zones = []
    page = 1
    per_page = 50
    while True:
        response = requests.get(
            f"{API_BASE}/zones",
            headers=HEADERS,
            params={"page": page, "per_page": per_page}
        )
        data = response.json()
        if not data.get("success"):
            raise Exception(f"Error al obtener zonas: {data.get('errors')}")
        
        zones += data["result"]

        # Corrección: manejar paginación con total_pages
        total_pages = data.get("result_info", {}).get("total_pages", 1)
        if page >= total_pages:
            break
        page += 1
    return zones

# === ACTIVAR HSTS POR ZONA ===
def enable_hsts(zone_id):
    payload = {
        "value": {
            "enabled": True,
            "max_age": 31536000,            # 1 año
            "include_subdomains": True,
            "preload": True,
            "nosniff": True
        }
    }
    response = requests.patch(
        f"{API_BASE}/zones/{zone_id}/settings/security_header",
        headers=HEADERS,
        json=payload
    )
    return response.json()

# === EJECUCIÓN PRINCIPAL ===
if __name__ == "__main__":
    try:
        zones = get_zones()
        for zone in zones:
            print(f"Activando HSTS en {zone['name']}...")
            result = enable_hsts(zone["id"])
            if result.get("success"):
                print(f"HSTS activado correctamente en {zone['name']}")
            else:
                print(f"Error en {zone['name']}: {result.get('errors')}")
    except Exception as e:
        print(f"Error fatal: {e}")
