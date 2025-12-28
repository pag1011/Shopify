from fastapi import FastAPI
from pydantic import BaseModel
from agent import ShopifyAgent

app = FastAPI()
agent = ShopifyAgent()

class QueryRequest(BaseModel):
    question: str
    store_id: str

@app.get("/")
def root():
    return {"status": "Python AI Service is running"}

@app.post("/predict")
async def predict(request: QueryRequest):
    query = agent.generate_shopify_ql(request.question)
    mock_data = {"product": "X", "stock": 5}
    answer = agent.explain_data(mock_data)

    return {
        "answer": answer,
        "confidence": "high"
    }
