import requests

def trigger():
    url = "http://localhost:5000/eliminar_grupo"
    params = {
        "nombre": "Amoxi",
        "dosis": "1 pastilla"
    }
    print(f"Requesting DELETE for {params}...")
    try:
        response = requests.get(url, params=params)
        print(f"Status: {response.status_code}")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    trigger()
