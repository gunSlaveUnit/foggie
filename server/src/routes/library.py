from typing import List, Type

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server.src.models.library import Library
from server.src.models.user import User
from server.src.schemas.library import LibraryDBSchema
from server.src.settings import LIBRARY_ROUTER_PREFIX, Tags
from server.src.utils.auth import get_current_user
from server.src.utils.db import get_db

router = APIRouter(prefix=LIBRARY_ROUTER_PREFIX, tags=[Tags.LIBRARY])


@router.get('/', response_model=List[LibraryDBSchema])
async def every(user_id: int | None = None,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)) -> list[Type[Library]]:
    """
    List of all library records according to the given filters.
    Returns a list of LibraryDBSchema with library record data.
    """

    records_query = db.query(Library)
    if user_id:
        records_query = records_query.filter(Library.player_id == user_id)

    return records_query.all()