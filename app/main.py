from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.chat import router as chat_router


app = FastAPI(

    title="SHL AI Assessment Recommender",

    description="""
    Conversational recommender for SHL assessments.
    Supports:
    - Clarification
    - Recommendation
    - Refinement
    - Comparison
    """,

    version="1.0"

)


# Health endpoint

app.include_router(

    health_router

)


# Chat endpoint

app.include_router(

    chat_router

)



@app.get("/")

def root():

    return {

        "message":

        "SHL AI Recommender Running",


        "docs":

        "/docs",


        "health":

        "/health",


        "chat":

        "/chat"

    }