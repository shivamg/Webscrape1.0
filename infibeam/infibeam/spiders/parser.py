def parseToFile(items, filename, spider):
    with open(filename, 'a') as f:
        for item in items:
            if spider == 'productPage':

                href = "http://www.infibeam.com"+str(item['link'])[3:-2]
                name = str(item['name'])[3:-2]
                image = str(item['image'])[3:-2]
                price = str(item['price'])[3:-2]
                f.write(href + "," + name + "," + image + "," + price)
                f.write("\n")
            else:
                href = str(item['link'])[:-1]
                count = str(item['count']).split('u')[4][1:-3]
                f.write(href + "," + count)
                f.write("\n")
