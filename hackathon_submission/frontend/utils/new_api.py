from pandas import DataFrame
from requests import Response, delete, get, post

from hackathon_submission.frontend.utils import common


def checkOnline() -> bool:
    resp: Response = get(url=common.URL, headers=common.HEADERS)
    return resp.json()["status"]


def login(username: str, password: str) -> str:
    data: dict = {"username": username, "password": password}
    resp: Response = post(
        url=f"{common.URL}/api/account/login",
        headers=common.HEADERS,
        json=data,
    )
    return resp.json()["username"]


def logout(username: str, password: str) -> None:
    data: dict = {"username": username, "password": password}
    post(
        url=f"{common.URL}/api/account/logout",
        headers=common.HEADERS,
        json=data,
    )


def signup(username: str, password: str) -> str:
    data: dict = {"username": username, "password": password}
    resp: Response = post(
        url=f"{common.URL}/api/account/signup",
        headers=common.HEADERS,
        json=data,
    )
    return resp.json()["username"]


def deleteAccount(username: str, password: str) -> None:
    data: dict = {"username": username, "password": password}
    delete(
        url=f"{common.URL}/api/account/delete",
        headers=common.HEADERS,
        json=data,
    )


def nlpPreprocess(data: dict) -> dict:
    resp: Response = post(
        url=f"{common.URL}/api/nlp/preprocess",
        json=data,
        headers=common.HEADERS,
    )
    return resp.json()


def cvPreprocess(image: bytes) -> dict:
    files: dict = {"file": ("image.jpeg", image)}
    resp: Response = post(
        url=f"{common.URL}/api/cv/preprocess",
        files=files,
    )
    return resp.json()


def nlpInference(data: dict) -> dict:
    resp: Response = post(
        url=f"{common.URL}/api/nlp/inference",
        headers=common.HEADERS,
        data=data,
    )
    return resp.json()


def cvInference(data: dict) -> dict:
    resp: Response = post(
        url=f"{common.URL}/api/cv/inference",
        headers=common.HEADERS,
        data=data,
    )
    return resp.json()


def createReport(data: dict) -> None:
    post(
        url=f"{common.URL}/api/report/create",
        headers=common.HEADERS,
        data=data,
    )


def deleteAllReports(username: str, password: str) -> None:
    data: dict = {"username": username, "password": password}
    delete(
        url=f"{common.URL}/api/account/delete",
        headers=common.HEADERS,
        json=data,
    )


def downloadAllReports(username: str, password: str) -> str:
    data: dict = {"username": username, "password": password}
    resp: Response = post(
        url=f"{common.URL}/api/report/download",
        headers=common.HEADERS,
        json=data,
    )
    return resp.json()["username"]
