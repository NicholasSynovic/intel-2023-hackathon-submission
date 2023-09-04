from pandas import DataFrame
from requests import Response, get, post

URL: str = "http://localhost:8000"
HEADERS: dict = {"Content-type": "application/json"}


def str2bool(data: str) -> bool:
    if data == "true":
        return True
    elif data == "false":
        return False
    else:
        return data


def check() -> bool:
    try:
        resp: Response = get(url=URL)
        return True
    except ConnectionError:
        return False


def login(username: str, password: str = "test") -> bool:
    resp: Response = post(
        url=f"{URL}/api/account/login?username={username}&password={password}"
    )
    data: str = resp.content.decode()
    return str2bool(data=data)


def logout() -> bool:
    resp: Response = post(url=f"{URL}/api/account/logout")
    data: str = resp.content.decode()
    return str2bool(data=data)


def signup(username: str, password: str) -> bool:
    resp: Response = post(
        url=f"{URL}/api/account/signup?username={username}&password={password}"
    )
    data: str = resp.json()["username"]
    return str2bool(data=data)


def preprocess(data: dict) -> str:
    resp: Response = post(
        url=f"{URL}/api/inference/api/preprocess",
        json=data,
        headers=HEADERS,
    )
    return resp.json()["message"]


def prognosis(message: str, username: str) -> bool:
    data: dict = {"message": message, "username": username}
    resp: Response = post(
        url=f"{URL}/api/inference/nlp/prognosis",
        json=data,
        headers=HEADERS,
    )
    return str2bool(data=resp.content.decode())
