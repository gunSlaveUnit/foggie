import uuid
from pathlib import Path
from typing import List

from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session, joinedload

from server.src.models.build import Build
from server.src.models.game import Game
from server.src.models.platform import Platform
from server.src.models.user import User
from server.src.schemas.build import BuildDBSchema, BuildCreateSchema
from server.src.settings import BUILDS_ROUTER_PREFIX, GAMES_ASSETS_PATH, GAMES_ASSETS_BUILDS_DIR
from server.src.utils.auth import get_current_user
from server.src.utils.db import get_db
from server.src.utils.file_system_storage import store

router = APIRouter(prefix=BUILDS_ROUTER_PREFIX)


@router.get('/', response_model=List[BuildDBSchema])
async def every(game_id: int,
                include_platforms: bool = False,
                db: Session = Depends(get_db)):

    items_query = db.query(Build).filter(Build.game_id == game_id)

    if include_platforms:
        items_query = items_query.join(Platform)
        items_query = items_query.options(joinedload(Build.platform))

    return items_query.all()


@router.post('/', response_model=BuildDBSchema)
async def create(game_id: int,
                 build_create_data: BuildCreateSchema,
                 db: Session = Depends(get_db),
                 current_user: User = Depends(get_current_user)) -> BuildDBSchema:
    """
    Creating a new build for specified game.
    Return a BuildDBSchema with created entity data.
    """

    build = Build(**vars(build_create_data))

    build.game_id = game_id

    related_game_directory = db.query(Game).filter(Game.id == game_id).one().directory

    build_directory = Path(GAMES_ASSETS_PATH)
    new_directory_uuid = str(uuid.uuid4())
    build_directory = build_directory.joinpath(related_game_directory, GAMES_ASSETS_BUILDS_DIR, new_directory_uuid)
    build_directory.mkdir(parents=True)
    build.directory = new_directory_uuid

    db.add(build)
    db.commit()
    db.refresh(build)

    return build


@router.put('/{build_id}/')
async def update(build_id: int):
    pass


@router.delete('/{build_id}/')
async def delete(build_id: int):
    pass


@router.get('/{build_id}/')
async def build_info(filename: str | None = None):
    """
    Returns the names of the build files.
    If "filename" query param was provided, returns a file.
    """
    pass


@router.post('/{build_id}/')
async def upload_build(game_id: int,
                       build_id: int,
                       files: List[UploadFile],
                       db: Session = Depends(get_db)):
    """
    Uploads project build files to the server.
    If something of them exists, won't be overwritten.
    """
    game = db.query(Game).filter(Game.id == game_id).one()
    build = db.query(Build).filter(Build.id == build_id).one()

    store_files_directory = Path(GAMES_ASSETS_PATH).joinpath(game.directory, GAMES_ASSETS_BUILDS_DIR, build.directory)

    return await store(store_files_directory, files)


@router.put('/{build_id}/')
async def update_build(file: UploadFile):
    """
    Uploads a build file to the server to update existing file.
    If not exists, won't be created.
    If the file is updated, the associated game will become unpublished.
    """
    pass


@router.delete('/{build_id}/')
async def delete_build(filename: str | None = None):
    """
    Deletes an existing build file
    or removes all if "filename" query param not provided.
    """
    pass
