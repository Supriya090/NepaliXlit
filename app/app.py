from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from transliteration import XlitEngine
from time import time

app = FastAPI()
templates = Jinja2Templates(directory=".")

engine = XlitEngine("ne", beam_width=10)


class Query(BaseModel):
    text: str

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/transliterate")
def transliterate(query: Query):
    try:
        # Make predictions using the loaded model
        start_time = time()
        out = engine.translit_sentence(query.text)
        end_time = time()
        
        return {"original": query.text, "translit": out, "time_taken": end_time-start_time}
    except Exception as exp:
        raise HTTPException(status_code=500, detail=str(exp))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# uvicorn app:app --reload