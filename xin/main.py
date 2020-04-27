import uvicorn as uvicorn

from xin_spider import X_spider
from kazoo.client import KazooClient
from utils import get_host_ip
from fastapi import FastAPI
def zk():
    zk = KazooClient(hosts="192.168.118.111:2181")
    zk.start()
    zk.ensure_path("/registration_number")
    zk.create("/registration_number/%s" % get_host_ip(), ephemeral=True)


app = FastAPI()

# zk()
@app.get("/registration_number")
def xin(registration_number: str = None):
    try:
        x=X_spider()
        item=x.run(registration_number)
        if item:
            return {"code":200,"result":item,"error":""}
        else:
            return {"code":201,"result":"","error":""}
    except Exception as e:
        return {"code":202,"result":"","error":e}
if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=7000)