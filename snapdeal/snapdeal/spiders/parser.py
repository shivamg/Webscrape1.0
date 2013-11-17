import re


def mapToId(link):
    mapping = [line.strip() for line in open('main page links.txt')]
    dic = {}
    for entry in mapping:
        key, val = entry.split(',')
        dic[key] = val
    return dic[link]


def parseToFile(items, filename, spider):
    with open(filename, 'a') as f:
        for item in items:
            if spider == 'mainPage':
                catId = mapToId(str(item['link']))
                href = "http://www.snapdeal.com/json/product/get/search/%s" % (catId)
                count = "0" if item['count'] == [''] else str(item['count'])[3:-2]
                f.write(href + "," + count)
                f.write("\n")
            else:
                href = "www.snapdeal.com/" + item['pageUrl'].encode('utf-8')
                name = item['name'].encode('utf-8')
                image = item['image'].encode('utf-8')
                price = str(item['displayPrice'])
                f.write(href + "," + name + "," + image + "," + price)
                f.write("\n")

