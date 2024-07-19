from fastapi import FastAPI, Depends
from fastapi_users import fastapi_users, FastAPIUsers
from starlette.middleware.cors import CORSMiddleware

from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from auth.database import User
from auth.manager import get_user_manager
from feedbacks.router import router as router_feedback

app = FastAPI(
    title="eLectrone"
)

#CORS
#region
origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=[],
)
#endregion


@app.get("/")
def hello():
    print("helolo")
    return "hello"

#work with feedbacks
app.include_router(router_feedback)

#auth_routes
#region
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

#endregion


#current_users
#region
current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.name}"

@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"

#endregion
