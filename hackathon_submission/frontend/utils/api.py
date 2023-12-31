from pandas import DataFrame
from requests import Response, delete, get, post
from requests.exceptions import JSONDecodeError

# URL: str = "http://localhost:8000"
# URL: str = "http://172.22.0.3:8000"
URL: str = "http://http://172.17.0.1:8000"  # Docker Bridge IP

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

    jsonData["image"] = bytes().decode()

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
            image: str = df["Image"].values[0]

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
                "Image": [
                    image,
                    0,
                    0,
                    0,
                    0,
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


def deleteReport(uuid: str) -> None:
    delete(url=f"{URL}/api/storage/deleteReports?uuid={uuid}")


def deleteAccount(username: str) -> None:
    delete(url=f"{URL}/api/account/delete?username={username}")


def uploadImage(username: str, image: bytes) -> None:
    files: dict = {"file": ("image.jpeg", image)}
    post(
        url=f"{URL}/api/storage/upload?username={username}",
        files=files,
    )


def changeUsername(username: str, newUsername: str) -> None:
    get(
        url=f"{URL}/api/account/changeUsername?username={username}&newUsername={newUsername}"
    )


def downloadReports(username: str) -> None:
    resp: Response = get(url=f"{URL}/api/storage/download/reports?username={username}")
    from json import dump

    with open(f"{username}_reports.json", "w") as jsonFile:
        dump(obj=resp.json(), fp=jsonFile, indent=4)
        jsonFile.close()
