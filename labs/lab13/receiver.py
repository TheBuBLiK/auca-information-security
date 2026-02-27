from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LogPayload(BaseModel):
    content: str

@app.post('/collect')
def collect(payload: LogPayload):
    with open('received_logs.txt', 'a', encoding='utf-8') as f:
        f.write(payload.content + "\n---\n")
    return {'status': 'saved', 'chars': len(payload.content)}
