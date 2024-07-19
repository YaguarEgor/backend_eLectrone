from fastapi import APIRouter, Depends

from auth.database import get_async_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from feedbacks.models import feedbacks

router = APIRouter(
    prefix="/feedbacks",
    tags=["Feedback"]
)

@router.get("/")
async def get_feedbacks(session: AsyncSession = Depends(get_async_session)):
    statement = select(feedbacks)
    result = await session.execute(statement)
    return result.mappings().all()