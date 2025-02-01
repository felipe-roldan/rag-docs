import uuid
import logging
import pdb

from fastapi import APIRouter, status, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse


from app.procesar_documento.models.process_document_request import (
  SearchVectorDataBaseRequest
)

router = APIRouter()

@router.post("/api/v1/cadena_qa", status_code=200)
async def query_qa_chain(
  request: SearchVectorDataBaseRequest
):
  ...