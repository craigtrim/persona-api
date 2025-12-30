from fastapi import FastAPI

from persona_api.routers import personality_router

app = FastAPI(
    title="Persona API",
    description="Generate bot/agent personalities based on the Big Five personality model",
    version="0.1.0",
)

app.include_router(personality_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
