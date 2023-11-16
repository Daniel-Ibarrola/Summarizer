from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary

from typing import Optional


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary"
    )
    await summary.save()
    return summary.id


async def get(id_: int) -> Optional[dict]:
    summary = await TextSummary.filter(id=id_).first().values()
    if summary:
        return summary
    return None


async def get_all() -> list:
    return await TextSummary.all().values()
