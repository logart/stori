from fastapi import FastAPI
import random
from typing import Dict, List
from random import choice
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

images = [
    "https://images.prom.ua/3633715315_w640_h640_shtora-velyur-temno-seraya.jpg",
    "https://podushka.com.ua/upload/catalogue/shtora_s_podkhvatom_provans_bella_rozy_s_kruzhevom_1570405512.jpg",
    "https://images.prom.ua/1075328978_shtora-blekaut-green.jpg"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

number = random.randint(0, 100)

@app.get("/guess")
async def make_guess(zinna: int)->str:

    if zinna < number:
        return 'higher'
    elif zinna > number:
        return'lower'
    else:
        return str(zinna)
    
@app.get("/")
async def string_returning(code: str)->str:
    return "redeploy works as a charm"

@app.get("/code")
async def string_returning(code: str)->str:
    return code

async def generate_jsons() -> List[Dict[str, str]]:
    jsons = []
    for i in range(10):
        title = "Щтора " + str(choice(range(i+1)))
        description = "Гардина " + str(i+1)
        image = choice(images)
        jsons.append({"title": title, "description": description, "image": image})
    return jsons
