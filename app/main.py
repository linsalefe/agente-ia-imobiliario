from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="Agente WhatsApp Imobiliário",
    description="Bot de qualificação de leads imobiliários",
    version="1.0.0"
)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "environment": settings.ENVIRONMENT,
        "version": "1.0.0"
    }


@app.get("/")
async def root():
    return {
        "message": "Agente WhatsApp Imobiliário API",
        "docs": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)