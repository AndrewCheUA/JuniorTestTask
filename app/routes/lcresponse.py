from fastapi import APIRouter, HTTPException

from app.schemas.lc_response import SummarizeRequest
from app.repository import repository_lcresponse

router = APIRouter(prefix='/summarize')


@router.post("/")
async def summarize_request(request: SummarizeRequest):
    try:
        # Use LangChain to generate the summary
        summary = await repository_lcresponse.create_summary(request.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))