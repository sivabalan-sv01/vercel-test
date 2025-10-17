from fastapi import FastAPI, BackgroundTasks, Request, Form
from fastapi.responses import FileResponse, HTMLResponse
import os

app = FastAPI()

@app.get("/")
async def read_index():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(base_dir, "index.html")
    return FileResponse(index_path)

# Example background task function
def background_process(data: str):
    # simulate processing task, e.g. saving data, heavy computation
    import time
    time.sleep(10)
    print(f"Processed data in background: {data}")

@app.post("/process")
async def process_request(background_tasks: BackgroundTasks, data: str = Form(...)):
    background_tasks.add_task(background_process, data)
    return {"message": "Request received, processing started in background"}
