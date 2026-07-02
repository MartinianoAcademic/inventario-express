from fastapi import FastAPI

app = FastAPI(title="Inventario Express")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Sistema de inventario activo"
    }

@app.get("/products")
def get_products():
    return [
        {
            "id": 1,
            "name": "Arroz",
            "stock": 25,
            "fue_editado": False
        },
        {
            "id": 2,
            "name": "Aceite",
            "stock": 10,
            "fue_editado": False
        }
    ]