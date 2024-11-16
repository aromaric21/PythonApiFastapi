from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


articles = {
    1: {"nom": "Unité cental", "prix":750},
    2: {"nom": "Ecran", "prix": 350}
}

class Article(BaseModel):
    nom:str
    prix:int


@app.get("/articles/{article_id}", response_model=Article)
async def get_article(article_id:int):
    if article_id in articles:
        return  articles[article_id]
    raise HTTPException(status_code=404, detail="Article non trouvé")


@app.post("/articles/", response_model=Article)
async def create_article(artticle:Article):
    new_id = max(articles.keys()) + 1
    articles[new_id] = artticle.model_dump()
    return artticle