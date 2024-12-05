import logging
from mangum import Mangum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.main import api_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Configure CORS
origins = [
    "*",       
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],                 
    allow_headers=["*"],                 
)

# Include your router here
app.include_router(api_router)

# Define your root endpoint
@app.get("/")
def root():
    logging.info("Root endpoint hit")
    return {"message": "Api 1.0"}

# Create the Mangum handler after all routes are defined
handler = Mangum(app)
