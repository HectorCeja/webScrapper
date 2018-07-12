import requests

page = requests.get("http://httpbin.org/ip")
print(page.text)

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

page = session.get("http://httpbin.org/ip")
print(page.text)
