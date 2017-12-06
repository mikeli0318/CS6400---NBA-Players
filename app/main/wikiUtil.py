def getWikiUrl(name):
    url = "https://en.wikipedia.org/wiki/"
    splitted = name.split(" ")
    url = url + splitted[0]
    for i in range(1, len(splitted)):
        url = url + "_" + splitted[i]
    return url