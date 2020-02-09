import pandas as pd
from bs4 import BeautifulSoup
from bs4 import NavigableString
from parseUtil import *


class HtmlParser:

    COLUMN_NAMES = ["HTML_ID", "TAG_NAME", "ATTRIBUTE_ID", "ATTRIBUTE_NAME", "ATTRIBUTE_CLASS", "ATTRIBUTE_PLACEHOLDER", "IN_FORM", "TAG_DEPTH", "TAG_STRING", "LOGIN_URL", "LABEL"]

    

    
    def parseHtml(src, id, df, login_url):
        soup = BeautifulSoup(src, "html.parser")
        body = soup.body
        parents = []
        df = recursiveParse(body, id, parents, df, login_url)
        return df

    
   

        

      

