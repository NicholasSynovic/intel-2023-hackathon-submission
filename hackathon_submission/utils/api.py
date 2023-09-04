from requests import get, post, Response
from requests.exceptions import ConnectionError

URL: str = "http://localhost:8000"

def check() ->  bool:
    try:
        resp: Response = get(url=URL)
        return True
    except ConnectionError:
        return False

def login(username: str, password: str = "test")    ->  bool:
    resp: Response = post(url=f"{URL}/api/account/login?username={username}&password={password}")
    print(resp.content)

login(username="user", password="password1")
