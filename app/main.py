from fastapi import FastAPI

from app.api.journals import router as journal_router

app = FastAPI(title="Stumi", version="0.1.0")
app.include_router(journal_router)


@app.get("/")
def root():
    return {"message": "Welcome to Stumi"}


@app.get("/health")
def health():
    return {"status": "healthy"}
