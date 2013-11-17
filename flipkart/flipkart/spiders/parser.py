import re


def parseToFile(items, filename, spider):
    with open(filename, 'a') as f:
        for item in items:
            if spider == 'productPage':
                allData = item['text'].encode('utf-8')
                positionStart = list(re.finditer('pu-image fk-product-thumb', allData))
                positionEnd = list(re.finditer('pu-offers', allData))
                for start, end in zip(positionStart, positionEnd):
                    prodDesc = allData[start.end():end.end() + 1]
                    link = prodDesc[:prodDesc.index("pu-details lastUnit")]
                    href = link[link.index("href=") + 6:link.index("amp;ref") - 1]
                    name = link[link.index("alt=") + 5:link.index("data-error-url") - 2]
                    image = link[link.index("src=") + 5:link.index("alt=") - 2]
                    price = prodDesc[prodDesc.index("pu-price"):prodDesc.index("pu-offers")]
                    price = price[price.index("Rs") + 3:price.index("&lt;/span")]
                    f.write("www.flipkart.com" + href + "," + name + "," + image + "," + price)
                    f.write("\n")
            else:
                href = str(item['link'])
                count = str(item['count'])[3:-2]
                f.write(href+","+count)
                f.write("\n")
