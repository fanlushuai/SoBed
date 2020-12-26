# Sobed
躺床上，控制一下电脑。应对，天太冷，不想下床关电脑

## 开发
### 搭建环境
方式一：本地python环境**不推荐**

1. 安装**python3.6**

2. pip install -r requirements.txt

方式二：使用conda虚拟环境
1. 使用conda创建虚拟环境,安装依赖。freeze.yml为本人开发的时候导出的conda环境。（可能不是最精简的）
conda env create -f freeze.yml
2. conda info --envs 查看当前所有的conda环境信息
3. conda activate Sobed-env （这个名字在freeze.yml里面写的，同时创建的位置默认在conda的默认环境路径下）

方式三：idea创建conda环境，配置项目拦截。pip安装依赖

### 开发
使用了这些包，看文档
- fastapi作为一个web服务器。暴露控制电脑的请求
- pyautogui 来通过快捷键，或者鼠标手势，来操控电脑

### 运行
- idea直接运行就行。
- python boot_with_uvicorn.py  运行
- 或者，uvicorn api:app  运行

### 打可执行包
~~~
pyinstaller -F boot_with_uvicorn.py --noconsole --hidden-import uvicorn.lifespan.off --hidden-import uvicorn.lifespan.on --hidden-import uvicorn.lifespan --hidden-import uvicorn.protocols.websockets.auto --hidden-import uvicorn.protocols.websockets.wsproto_impl --hidden-import uvicorn.protocols.websockets_impl --hidden-import uvicorn.protocols.http.auto --hidden-import uvicorn.protocols.http.h11_impl --hidden-import uvicorn.protocols.http.httptools_impl --hidden-import uvicorn.protocols.websockets --hidden-import uvicorn.protocols.http --hidden-import uvicorn.protocols --hidden-import uvicorn.loops.auto --hidden-import uvicorn.loops.asyncio --hidden-import uvicorn.loops.uvloop --hidden-import uvicorn.loops --hidden-import uvicorn.logging 
~~~

- -F：每次打包覆盖之前打的包
- --noconsole 打包一个不带控制台的后台进程
- --hidden-import 导入隐含引入的包

#### 遇到的坑：
- 缺失模块uvicorn logging

uvicorn 有些包属于隐含导入，pyinstaller扫描不到，需要手动配置。

 1. 运行pyinstaller -F boot_with_uvicorn.py
 2. 修改生成的boot_with_uvicorn.spec
 3. 替换下面的值
~~~
hiddenimports=['uvicorn.lifespan.off','uvicorn.lifespan.on','uvicorn.lifespan',
                          'uvicorn.protocols.websockets.auto','uvicorn.protocols.websockets.wsproto_impl',
                          'uvicorn.protocols.websockets_impl','uvicorn.protocols.http.auto',
                          'uvicorn.protocols.http.h11_impl','uvicorn.protocols.http.httptools_impl',
                          'uvicorn.protocols.websockets','uvicorn.protocols.http','uvicorn.protocols',
                          'uvicorn.loops.auto','uvicorn.loops.asyncio','uvicorn.loops.uvloop','uvicorn.loops',
                          'uvicorn.logging'],
~~~

参考：
https://stackoverflow.com/questions/64281002/pyinstaller-compiled-uvicorn-server-does-not-start-correctly

- 运行exe时，发现api模块找不到

uvicorn和api.py一个文件的时候，可以运行。
但是命令行的时候，需要单独写个文件，使用from api import app的形式，才能使得uvicorn发现这个模块。

所以，你看到boot_with_uvicorn.py单独抽取出来，导入api的方式来搞。这是必须的。

参考：https://stackoverflow.com/a/64549088/6800227


## 使用
### 直接打包好了，直接用
dist/boot_with_uvicorn.exe



## 逻辑实现
fastapi，暴露web服务，调用pyautogui来操作电脑部分功能。
实现简单的，music播放控制。关闭屏幕之类的。等等，可以以基于这个架子随便搞的。
同时，fastapi提供了swagger文档，直接局域网访问文档，执行你想要的操作就好了。
因为pyautogui具有一定的跨平台特性。所以，mac，win都基本试用。
ok，自己看着用，耗子尾汁。

## 进一步的使用建议
手机端，写个app。控制。
或者，搞个页面，里面能够自动扫描局域网端口，来让用户选择服务。同时包装一下控制请求，提供更加优美的控制体验就好了。
另外，本人的使用方式，是通过手机chrome浏览器访问，手机chrome可以在桌面生成链接。平常直接点击链接，和app效果一样了。

