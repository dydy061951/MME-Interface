#encoding=utf-8
import requests,json,urllib3

# 请求封装

def send_request(method,url,header,data):
    if(method=="get"):
        return send_get(url,header,data)
    elif(method=="post"):
        return send_post(url,header,data)
    elif(method=="put"):
        return send_put(url,header,data)
    elif(method=="delete"):
        return send_delete(url,header,data)


def send_get(url,header,data):
    requests.packages.urllib3.disable_warnings()
    r=requests.get(url=url,headers=header,params=data,verify=False)    # verify：证书取消验证
    # js_response = json.loads(r.text)
    # str_response = json.dumps(js_response, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'))
    return r


def send_post(url,header,data):
    requests.packages.urllib3.disable_warnings()
    datas=json.loads(data)
    r=requests.post(url=url,headers=header,json=datas,verify=False)       # verify：证书取消验证
    # js_response = json.loads(r.text)
    # str_response = json.dumps(js_response, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'))
    return r


def send_put(url,header,data):
    requests.packages.urllib3.disable_warnings()
    datas = json.loads(data)
    r = requests.put(url=url, headers=header, json=datas, verify=False)     # verify：证书取消验证
    # js_response = json.loads(r.text)
    # str_response = json.dumps(js_response, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'))
    return r

def send_delete(url,header,data):
    requests.packages.urllib3.disable_warnings()
    datas = str(data)
    url_ok=url+"/"+datas
    r = requests.put(url=url_ok, headers=header, json=datas, verify=False)  # verify：证书取消验证
    # js_response = json.loads(r.text)
    # str_response = json.dumps(js_response, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'))
    return r

