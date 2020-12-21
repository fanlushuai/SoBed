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


@app.get("/vol_up")
def vol_up():
    pc.vol_up()
    return "ok"


@app.get("/vol_down")
def vol_down():
    pc.vol_down()
    return "ok"


@app.get("/music_next")
def music_next():
    pc.music_next()
    return "ok"


@app.get("/music_last")
def music_last():
    pc.music_last()
    return "ok"


@app.get("/music_play_pause")
def music_play_pause():
    pc.music_play_pause()
    return "ok"


@app.get("/screen_off")
def screen_off(sec: int = 1):
    pc.screen_off(sec)
    return "ok"


@app.get("/screen_on")
def screen_on():
    pc.screen_on()
    return "ok"


@app.get("/pc_sleep")
def pc_sleep(sec: int = 5):
    pc.pc_sleep(sec)
    return "目前只写了windows，自己补充mac"


@app.get("/pc_shutdown")
def pc_shutdown(sec: int = 5):
    pc.pc_shutdown(sec)
    return "目前只写了windows，自己补充mac"


if __name__ == '__main__':
    uvicorn.run('api:app', host='0.0.0.0', port=80, log_level="info")
