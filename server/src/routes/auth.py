import uuid

from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse

from server.src.models.user import User
from server.src.schemas.user import SignInSchema, UserDBSchema
from server.src.settings import Tags, SESSION_TTL
from server.src.utils.db import get_db, get_session_storage
from server.src.utils.auth import authenticate_user, get_current_user

router = APIRouter(prefix='/auth', tags=[Tags.AUTH])


@router.post("/sign-up/")
async def sign_up():
    """
    Registration (creation of a new user).
    Login immediately.
    """
    pass


@router.post("/sign-in/")
async def sign_in(login_data: SignInSchema,
                  db: Session = Depends(get_db),
                  session_storage=Depends(get_session_storage)):
    """
    Sets the session id in the request cookie
    if the user is successfully authenticated.
    """
    user: User | None = await authenticate_user(login_data.account_name, login_data.password, db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"detail": "Incorrect account name or password"}
        )

    session_id = str(uuid.uuid4())
    session_storage.set(session_id, user.id)
    session_storage.expire(session_id, SESSION_TTL)

    response = JSONResponse({"detail": "Logged in successfully"})
    response.set_cookie("session_id", session_id, max_age=SESSION_TTL)
    return response


@router.post("/sign-out/")
async def sign_out(authorization: str = Header(None),
                   _=Depends(get_current_user),
                   session_storage=Depends(get_session_storage)):
    """
    Deletes a user session.
    """
    session_storage.delete(authorization)
    response = JSONResponse({"detail": f"Session {authorization} was removed"})
    return response


@router.get("/me/", response_model=UserDBSchema)
async def me(current_user: User = Depends(get_current_user)):
    """
    Returns current user data as a UserDBScheme
    """
    return current_user
