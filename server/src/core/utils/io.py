import gzip
import os
import shutil
from pathlib import Path
from typing import List, BinaryIO

import aiofiles as aiofiles
from fastapi import UploadFile

CHUNK_SIZE = 1024 * 1024
MEDIA_TYPE = "application/gzip"


async def save(directory: Path, files: List[UploadFile]):
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)

    for file in files:
        async with aiofiles.open(directory.joinpath(file.filename), 'wb') as f:
            while chunk := await file.read(CHUNK_SIZE):
                await f.write(chunk)


async def clear(directory: Path):
    for path in directory.glob("**/*"):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)


async def remove(directory: str, files: List[str]):
    for file in files:
        os.remove(Path(directory).joinpath(file))


def _read_chunks(file_object: BinaryIO, chunk_size: int = CHUNK_SIZE) -> bytes:
    while chunk := file_object.read(chunk_size):
        yield chunk


def read_uncompressed_chunks(file_path: str, chunk_size: int = CHUNK_SIZE) -> bytes:
    with open(file_path, "rb") as file:
        for chunk in _read_chunks(file, chunk_size):
            yield chunk


def read_compressed_chunks(file_path: str, chunk_size: int = CHUNK_SIZE) -> bytes:
    with open(file_path, "rb") as file:
        for chunk in _read_chunks(file, chunk_size):
            yield gzip.compress(chunk)
