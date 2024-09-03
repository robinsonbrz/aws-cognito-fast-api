from functools import wraps
from typing import List

from fastapi import HTTPException
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED

import os
from dotenv import load_dotenv

from jwt_bearer import CognitoAuthenticator

load_dotenv()

POOL_REGION = os.getenv('POOL_REGION')
POOL_ID = os.getenv('POOL_ID')
CLIENT_ID = os.getenv('CLIENT_ID')

auth = CognitoAuthenticator(
    pool_region=POOL_REGION,
    pool_id=POOL_ID,
    client_id=CLIENT_ID,
)

def auth_required():
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request,*args, **kwargs):
            credentials = request.headers.get("Authorization", None) # Bearer token
            if credentials:
                try:
                    claims = auth.verify_token(credentials.split(' ')[1])
                    print(claims)
                except Exception as e:
                    print(e)
                    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
            else:
                raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)

            return func(request,*args, **kwargs)

        return wrapper

    return decorator
