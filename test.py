#requests is a module(package) that can be used for interacting with websites
import requests

#the get function from requests gets the information from the specified URL
r = requests.get("https://xkcd.com/353/")

#
print(r)

print(dir(r))

print(help(r))

print(r.text)

p = requests.get("https://imgs.xkcd.com/comics/python.png")

print(p.content)

with open("comic.png", 'wb') as f:
    f.write(p.content)

hendo = requests.get("https://d3j2s6hdd6a7rg.cloudfront.net/v2/uploads/media/default/0001/89/thumb_88507_default_news_size_5.jpeg")

with open("hendo.png", 'wb') as h:
    h.write(hendo.content)