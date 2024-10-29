# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.controller.visualize import router as visualize_router
from app.db.init_db import init_db

app = FastAPI()

# Define lifespan function
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run startup tasks
    init_db()
    yield  # Control goes to the app here
    # Run shutdown tasks if needed

# Initialize the app with the lifespan handler
app = FastAPI(lifespan=lifespan)

# Set up CORS (optional but recommended for web apps)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed for your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(visualize_router, prefix="/api/v1")