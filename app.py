#fast api  endpint to receive requests and process them in the background and display index.html at root
from fastapi import FastAPI

from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def read_index():
    return FileResponse("index.html")
