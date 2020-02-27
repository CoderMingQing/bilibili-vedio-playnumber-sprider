import requests
import json


def getJson(url):
    rt = None
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        rt = r.json()
        # 通过code的值判断json是否是正确数据，0为正确值
        if rt["code"] != 0:
            rt = None
    except expression as identifier:
        print(r.status_code)
        print(identifier)
    return rt
def get

if __name__ == "__main__":
    url = "https://api.bilibili.com/x/space/arc/search?mid=25533789&pn=1&ps=25&jsonp=jsonp"
    rt = getJson(url)
    if rt != None:
        try:
            print(rt["data"]["list"]["vlist"][0]["play"])
        except KeyError as identifier:
            print(str(identifier) + "已不存在该json的keys中，请根据下面的json修改\n")
            print(rt)
