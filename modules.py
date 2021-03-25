import asyncio
import functools
import json
import threading
import typing
from types import FunctionType

_F = typing.TypeVar("_F", typing.Callable, FunctionType)

thread_lock = threading.Lock()

class JSONDict(dict):
    def get(self, k):
        return super().get(str(k))
    def __getitem__(self, k):
        return super().__getitem__(str(k))
    def __setitem__(self, k, v) -> None:
        return super().__setitem__(str(k), v)
    def __contains__(self, o: object) -> bool:
        return super().__contains__(str(o))


with open("bank.json", "r") as f:
    users = JSONDict(json.load(f))


def threaded():
    def predicate(func: _F):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> typing.Coroutine:
            loop = asyncio.get_event_loop()
            with thread_lock:
                result = await loop.run_in_executor(None, func, *args, **kwargs)
            return result

        return wrapped

    return predicate


@threaded()
def save_bank():
    with open("bank.json", "w") as f:
        json.dump(users, f)


async def open_account(user):
    if str(user.id) in users:
        return False

    else:
        user_data = {
            "wallet": 0,
            "bank": 0,
            "commisions": 0,
            "negative": 0,
            "about": 0,
            "about": "None",
            "portofolio": "None",
            "timezone": "None",
        }
        users[str(user.id)] = user_data

        await save_bank()

    return True


async def update_bank(user, change=0, mode="wallet"):
    users[str(user.id)][mode] += change

    await save_bank()

    bal = [
        users[str(user.id)]["wallet"],
        users[str(user.id)]["bank"],
        users[str(user.id)]["commisions"],
    ]
    return bal