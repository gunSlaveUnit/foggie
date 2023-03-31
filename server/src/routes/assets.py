from fastapi import APIRouter, UploadFile

from settings import ASSETS_ROUTER_PREFIX, Tags

router = APIRouter(prefix=ASSETS_ROUTER_PREFIX, tags=[Tags.GAMES])


@router.get('/header/')
async def download_header():
    """
    Returns an image for the header section of the game.
    """
    pass


@router.post('/header/')
async def upload_header(file: UploadFile):
    """
    Uploads a header game section file to the server.
    If exists, won't be created.
    """
    pass


@router.put('/header/')
async def update_header(file: UploadFile):
    """
    Uploads a header game section file to the server to update existing file.
    If not exists, won't be created.
    """
    pass


@router.get('/capsule/')
async def download_capsule():
    """
    Returns an image for the capsule section of the game.
    """
    pass


@router.get('/screenshots/')
async def screenshots_info(filename: str | None = None):
    """
    Returns the names of the screenshot files.
    If "filename" query param was provided, returns a file.
    """
    pass


@router.get('/trailers/')
async def trailers_info(filename: str | None = None):
    """
    Returns the names of the trailers files.
    If "filename" query param was provided, returns a file.
    """
    pass


@router.get('/build/')
async def build_info(filename: str | None = None):
    """
    Returns the names of the build files.
    If "filename" query param was provided, returns a file.
    """
    pass