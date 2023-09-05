from pandas import DataFrame
from requests import Response, get, post
from requests.exceptions import JSONDecodeError

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


def nlpPreprocess(data: dict) -> str:
    resp: Response = post(
        url=f"{URL}/api/inference/nlp/preprocess",
        json=data,
        headers=HEADERS,
    )
    return resp.json()["message"]


def nlpPrognosis(message: str, username: str) -> None:
    data: dict = {"message": message, "username": username}
    resp: Response = post(
        url=f"{URL}/api/inference/nlp/prognosis",
        json=data,
        headers=HEADERS,
    )

    jsonData: dict = resp.json()
    resp: Response = post(
        url=f"{URL}/api/generate/report",
        json=jsonData,
        headers=HEADERS,
    )


def getReports(username: str) -> list:
    dfList: list = []
    resp: Response = get(url=f"{URL}/api/storage/report?username={username}")

    try:
        largeDF: DataFrame = DataFrame(data=resp.json())
    except JSONDecodeError:
        return dfList

    try:
        smallDFs: list = [largeDF.iloc[[i]] for i in range(len(largeDF))]

        df: DataFrame
        for df in smallDFs:
            time: float = df["Report Time"].values[0]
            symptoms: str = df["Symptoms"].values[0]
            prognosis1: str = df["Prognosis 1"].values[0]
            prognosis2: str = df["Prognosis 2"].values[0]
            prognosis3: str = df["Prognosis 3"].values[0]
            prognosis4: str = df["Prognosis 4"].values[0]
            prognosis5: str = df["Prognosis 5"].values[0]
            probability1: str = df["Probability 1"].values[0]
            probability2: str = df["Probability 2"].values[0]
            probability3: str = df["Probability 3"].values[0]
            probability4: str = df["Probability 4"].values[0]
            probability5: str = df["Probability 5"].values[0]

            dfDict: dict = {
                "Prognosis": [
                    prognosis1,
                    prognosis2,
                    prognosis3,
                    prognosis4,
                    prognosis5,
                ],
                "Probability": [
                    probability1,
                    probability2,
                    probability3,
                    probability4,
                    probability5,
                ],
            }
            data: dict = {
                "time": time,
                "symptoms": symptoms,
                "df": DataFrame(data=dfDict),
            }
            dfList.append(data)

    except KeyError:
        pass

    return dfList
