import re


def parseToFile(fileinput,fileoutput):

    with open(fileinput,'r') as f:
        allData = f.read()
    
    with open(fileoutput, 'a') as f:
            positionStart = list(re.finditer('headerProductCategories', allData))
            positionEnd = list(re.finditer('pickCategory', allData))
            for start, end in zip(positionStart, positionEnd):
                    prodDesc = allData[start.end():end.start()]
                    catID = prodDesc[prodDesc.index('catId=')+12:prodDesc.index('catUrl=')-7].strip()
                    catUrl = prodDesc[prodDesc.index('catUrl=')+13:prodDesc.index('name=')-7].strip()
                    f.write("http://www.snapdeal.com/products/"+catUrl+"?sort=plrty&,"+catID)
                    f.write("\n")

parseToFile("catscraper.txt","main page links.txt")