from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import uuid
import asyncio
from database import JOBS
from tasks import process_circuit

app = FastAPI()

class QuantumJob(BaseModel):
    circuit: dict
    shots: int

@app.post("/submit")
async def submit_job(job: QuantumJob):
    job_id = str(uuid.uuid4())
    JOBS[job_id] = {"status": "pending", "result": None}

    # Process circuit in the background
    asyncio.create_task(process_circuit(job_id, job.circuit, job.shots))
    
    return {"job_id": job_id}

@app.get("/result/{job_id}")
async def get_result(job_id: str):
    if job_id not in JOBS:
        return {"error": "Job not found"}
    
    return JOBS[job_id]