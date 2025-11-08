from fastapi import FastAPI

app = FastAPI()

# Your route definitions below
@app.get("/")
async def root():
    return {"message": "Hello World"}
