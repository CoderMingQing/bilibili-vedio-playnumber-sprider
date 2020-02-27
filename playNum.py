import requests

url = "https://api.bilibili.com/x/space/arc/sea\
rch?mid=379041822&pn=1&ps=25&jsonp=jsonp"


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
    except Exception as identifier:
        print(r.status_code)
        print(identifier)
    return rt


def getVediosInfo():
    stringList = []
    rt = getJson(url)
    if rt is not None:
        try:
            vedios = rt["data"]["list"]["vlist"]
            for v in vedios:
                stringList.append(v["title"] + " ")
                stringList.append("播放数：")
                stringList.append(str(v["play"]))
                stringList.append("\n")
            return "".join(stringList)
        except KeyError as identifier:
            print(str(identifier) + "已不存在该json的keys中，请根据下面的json修改\n")
            print(rt)
    return "抓取失败，重试或查看日志"


if __name__ == "__main__":
    print(getVediosInfo())
