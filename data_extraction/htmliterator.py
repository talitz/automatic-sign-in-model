import requests
import pandas as pd
from requestUtil import *
from htmlParser import HtmlParser

id=1
#Column names
COLUMN_NAMES = ["HTML_ID", "TAG_NAME", "ATTRIBUTE_ID", "ATTRIBUTE_NAME", "ATTRIBUTE_CLASS", "ATTRIBUTE_PLACEHOLDER", "IN_FORM", "TAG_DEPTH", "TAG_STRING", "LABEL"]
#Initializing dataframe
df = pd.DataFrame(columns=COLUMN_NAMES)


#Read urls from xslx file
loginurls = pd.read_csv("loginurls.csv")

#Creating parser object
htmlParser=HtmlParser()

#Iterating over all login urls
for loginurl in loginurls["LOGIN_URL"]:
   try:
      print("Requesting : " + loginurl)
      src = getHtmlString(loginurl)
      df = HtmlParser.parseHtml(src, id, df, loginurl)
      print("finished parsing html num " + str(id))
   except Exception as e:
      print("Could not load: " + loginurl)
   id = id + 1
  



#converting dataframe to csv
df.to_csv("features.csv")







