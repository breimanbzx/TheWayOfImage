import requests


# 存储API调用的URL。最新的 GitHub API版本为第3版
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# 通过指定headers显式地要求使用这个 版本的API
headers = {'Accept': 'application/vnd.github.v3+json'}
# 再使用requests调用API，返回响应对象赋值给r
r = requests.get(url, headers=headers)
# 响应对象包含一个名为status_code的属性，指出了请求是否成功（状态码 200表示请求成功）
print('状态码', r.status_code)
if r.status_code == 200:
    # 这个响应对象还包括JSON格式的信息
    print(r.json().keys())
