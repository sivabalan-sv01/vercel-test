from fastapi import FastAPI, BackgroundTasks, Request, Form
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

@app.get("/")
async def read_index():
    return FileResponse("index.html")

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
