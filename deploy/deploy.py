from fastapi import FastAPI, Request
import models
import time


app = FastAPI(
    title='MLOps', debug=True,
)


@app.middleware("http")
async def measure_execution_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    execution_time = (end_time - start_time)
    print(f"Endpoint '{request.method} {request.url.path}' execution time: {execution_time}s")
    return response


@app.post("/question")
async def create_item(question:str):
    return {'quesion': question, "answer": models.getAnswer(question)}

@app.get('/version')
async def getVersion():
    global version
    return {'version': version}

@app.put('/metadata')
async def setMetadata(metadata:str):
    des = metadata['description']
    ver = metadata['version']
    global version
    version = ver
    global description
    description = des    
    return {'version': version, 'description': description}

