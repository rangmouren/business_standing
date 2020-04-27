import json
import requests
# from kazoo.client import KazooClient
class Searcher(object):
    # def __init__(self,hosts="192.168.118.111:2181"):
    #     self.zk = KazooClient(hosts=hosts)
    #     self.zk.start()
    def run(self,registration_number):
        # host = self.zk.get_children("/registration_number")[0]
        p_data = {'registration_number':registration_number}
        gresp = requests.get(url="http://{}:7000/registration_number".format('127.0.0.1'),params=p_data)
        result = {"result":json.loads(gresp.content.decode())}
        return result
if __name__ == '__main__':
    s=Searcher()
    print(s.run('350503600308244'))