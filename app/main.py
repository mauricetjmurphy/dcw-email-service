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
    "http://localhost:5173",  # Frontend URL
    "http://127.0.0.1:5173", # Localhost resolution
]

origins = [
    "http://localhost:5173",  # Frontend dev server
    "http://127.0.0.1:5173", # Localhost resolution
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Explicitly allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],        # Allow all HTTP methods
    allow_headers=["*"],        # Allow all headers
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
