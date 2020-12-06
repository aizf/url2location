from urllib import request
from urllib.parse import urlparse
from socket import gethostbyname
import json


def genApi(ip):
    api = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?"
    params = {
        # "query": "121.51.18.68",
        "co": "",
        "resource_id": "5809",
        "ie": "utf8",
        "oe": "gbk",
        "format": "json",
        "tn": "baidu"
    }
    params["query"] = ip
    params_str = "&".join([key + "=" + val for (key, val) in params.items()])
    return api + params_str


raw = r"https://blog.csdn.net/qq_28877125/article/details/81409748"

url = urlparse(raw)
# print(url.netloc)
ip = gethostbyname(url.netloc)
# print(ip)
api = genApi(ip)
# print(api)
res = request.urlopen(api)
data = res.read().decode('utf8')
print(json.loads(data)["data"][0]["location"])
with open('./res.json', 'w') as f:
    f.write(data)
