import requests



def getHtmlString(loginurl):
    result = requests.get(loginurl)
    return result.content