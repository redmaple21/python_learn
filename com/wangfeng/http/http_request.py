import requests


def get(url, params):
    try:
        print('send get request')
        res = requests.get(url=url, params=params)
        for k, v in res.json().items():
            print(k, v)
    except Exception:
        print('连接发生错误')


def post(url, params):
    try:
        print('send get request')
        res = requests.post(url=url, params=params)
        for k, v in res.json().items():
            print(k, v)
    except Exception:
        print('连接发生错误')


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/gettest'
    params = {'name': 'wangfeng', 'age': 37}
    get(url, params)
    url = 'http://127.0.0.1:5000/posttest'
    params = {'name': 'wangfeng', 'age': 37}
    post(url, params)
