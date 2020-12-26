import socket
import sys
import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND

from pccheetsheet import PcControlBaseSheet

app = FastAPI()

pc = PcControlBaseSheet()


@app.get("/")
def index():
    return RedirectResponse(url="/docs", status_code=HTTP_302_FOUND)


@app.get("/media/vol_up")
def vol_up():
    pc.vol_up()
    return "ok"


@app.get("/media/vol_down")
def vol_down():
    pc.vol_down()
    return "ok"


@app.get("/media/next")
def music_next():
    pc.music_next()
    return "ok"


@app.get("/media/last")
def music_last():
    pc.music_last()
    return "ok"


@app.get("/media/play_pause")
def music_play_pause():
    pc.music_play_pause()
    return "ok"


@app.get("/screen/off")
def screen_off(sec: int = 1):
    pc.screen_off(sec)
    return "ok"


@app.get("/screen/on")
def screen_on():
    pc.screen_on()
    return "ok"


@app.get("/pc/sleep")
def pc_sleep(sec: int = 5):
    pc.pc_sleep(sec)
    return "目前只写了windows，自己补充mac"


@app.get("/pc/shutdown")
def pc_shutdown(sec: int = 5):
    pc.pc_shutdown(sec)
    return "目前只写了windows，自己补充mac"
