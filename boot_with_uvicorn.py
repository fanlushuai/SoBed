import socket

import uvicorn
# 这个是必须的。如果在命令行运行，如果不指定这个。uvicorn找不到api这个模块。在idea是可以的执行的。
from api import app


if __name__ == '__main__':
    hostname = socket.gethostname()
    local_area_network_ip = socket.gethostbyname(hostname)
    # 若只想本机使用的服务，不允许同局域网的设备访问，使用：127.0.0.1或localhost （前提是已经做了host映射）；
    # 若想本局域网的主机都可访问但外网不可访问，监听本主机的IP地址，例如：192.168.1.2；
    # 若想本局域网的主机和外网都可访问，监听0.0.0.0就可以
    uvicorn.run('api:app', host=local_area_network_ip, port=80, log_level="info")
