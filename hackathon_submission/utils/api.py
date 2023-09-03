from requests import get, post, Response
from requests.exceptions import ConnectionError

URL: str = "http://localhost:8000"

def check() ->  bool:
    try:
        resp: Response = get(url=URL)
        return True
    except ConnectionError:
        return False
