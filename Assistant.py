from fastapi import FastAPI,Query
from pydantic import BaseModel
from Openapi_client import generate_response

app = FastAPI()
class UserQuery(BaseModel):
    query: str
    usecase: str
    tone: str
    style: str
    language: str
@app.post("/generate-response/")
def Assistant(query: str,
    usecase: str = Query(..., description="The use case for the query", enum=["Report", "Application", "Letter", "Essay"]),
    tone: str = Query(..., description="The tone of the response", enum=["Empathetic", "Encouraging", "Professional", "Casual"]),
    style: str = Query(..., description="The style of the response", enum=["Technical", "Creative", "Concise", "Detailed"]),
    language: str = Query(..., description="The language of the response", enum=["English", "Spanish"])):
    try:
        prompt = f"Usecase: {usecase}\nTone: {tone}\nStyle: {style}\nLanguage: {language}\n\nQuery: {query}\n\nResponse:"
        bot_response = generate_response(prompt)
        response = {"response": bot_response}
    except Exception as e:
        print(f"Unexpected error in assistant function: {e}")
        response = {"response": "An unexpected error occurred. Please try again later."}

    return response

