import os


def isNonZeroFile(fpath):
    return True if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else False


def cleanFile():
    if not isNonZeroFile('all products'):
        open('all products.txt', 'w').close()
    if not isNonZeroFile('main page links count'):
        open('main page links count.txt', 'w').close()


# empty out output files, create config files for scrapy/parser consumption
def setEnv():
    cleanFile()


setEnv()
