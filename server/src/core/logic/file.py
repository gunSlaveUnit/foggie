import shutil
from pathlib import Path
from typing import List

from fastapi import UploadFile
from starlette.responses import FileResponse, StreamingResponse

from server.src.core.utils.io import read_compressed_chunks, CHUNK_SIZE, read_uncompressed_chunks


class FileLogic:
    @staticmethod
    async def file(directory: Path, filename: str, media_type: str):
        return FileResponse(
            directory.joinpath(filename),
            headers={"Content-Disposition": f"filename={filename}"},
            media_type=media_type
        )

    @staticmethod
    async def stream(directory: Path, filename: str, media_type: str, compress=False):
        filepath = directory.joinpath(filename)

        handler = read_compressed_chunks(filepath, CHUNK_SIZE) if compress else read_uncompressed_chunks(filepath,
                                                                                                         CHUNK_SIZE)

        return StreamingResponse(
            handler,
            headers={"Content-Disposition": f"filename={filename}"},
            media_type=media_type
        )

    @staticmethod
    async def save(directory: Path, files: List[UploadFile]):
        for file in files:
            with open(directory.joinpath(file.filename), 'wb') as document:
                data = await file.read()
                document.write(data)

    @staticmethod
    async def clear(directory: Path):
        for path in directory.glob("**/*"):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                shutil.rmtree(path)
