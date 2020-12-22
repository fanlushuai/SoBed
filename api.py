import socket

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


if __name__ == '__main__':
    hostname = socket.gethostname()
    local_area_network_ip = socket.gethostbyname(hostname)
    # 若只想本机使用的服务，不允许同局域网的设备访问，使用：127.0.0.1或localhost （前提是已经做了host映射）；
    # 若想本局域网的主机都可访问但外网不可访问，监听本主机的IP地址，例如：192.168.1.2；
    # 若想本局域网的主机和外网都可访问，监听0.0.0.0就可以
    uvicorn.run('api:app', host=local_area_network_ip, port=80, log_level="info")
