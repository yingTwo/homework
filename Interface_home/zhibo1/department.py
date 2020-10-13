import requests

corpid = 'ww228382814e46e3a7'
corpsecret = 'iton7ufNa898V0By7pZ8rmUpW0nPcXDSBIVc3BA3H-k'#注释

def get_token():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
    r = requests.get(url)
    # print(r.json()['access_token'])
    return r.json()['access_token']

def test_addD():
    token = get_token()
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}'
    data = {
        "name": "HNTC4",
        "name_en": "河南测试中心4",   #在web端显示的部门名称是此字段，是否接口文档有些问题
        "parentid": 1,
        "order": 9,
        "id": 10
    }
    d_new = requests.post(url, json=data)
    print(d_new.json())
    assert d_new.json()['errcode'] == 0

def test_read():
    Did = 1
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={get_token()}&id={Did}'
    print(requests.get(url).json())
    assert requests.get(url).json()['errcode'] == 0

def test_modify():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={get_token()}'
    data = {
        "id": 2,
        "name_en": "北京测试中心1",
    }
    # print(requests.post(url, json=data).json())
    assert requests.post(url, json=data).json()['errcode'] == 0

def test_del():
    Did = 10
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={get_token()}&id={Did}'
    D_del = requests.get(url).json()
    print(D_del)
    assert D_del['errcode'] == 0


