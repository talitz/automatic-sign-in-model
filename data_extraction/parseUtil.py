
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import NavigableString


TAGS_TO_SKIP_ENTIRELY = ["p","img","script","b","h1", "h2", "h3", "\n"]
TAGS_TO_SKIP_AND_CONTINUE_TO_CHILDREN = ["body", "div"]


def recursiveParse(soup, id, parents, df, login_url):

    #Skipping noise elements
    if soup.name in TAGS_TO_SKIP_ENTIRELY or isinstance(soup, NavigableString): 
        return df
    #not extracting features for noise tags
    if not soup.name in TAGS_TO_SKIP_AND_CONTINUE_TO_CHILDREN:
        df = extractFeatures(soup, id, parents, df, login_url)
    #Continuing to next
    for child in soup.children:
        parents.append(soup.name)
        df = recursiveParse(child, id, parents, df, login_url)
        parents.pop()

    return df
    

def extractFeatures(soup, id, parents, df, login_url):
    html_id = str(id)
    tag_name = soup.name
    attribute_id = getAttribute(soup, 'id')
    attribute_name = getAttribute(soup, 'name')
    attribute_class = getAttribute(soup, 'class')
    attribute_placeholder = getAttribute(soup, 'placeholder')
    in_form = isInForm(parents)
    tag_depth = len(list(soup.parents))
    tag_string = soup.string

    label = "0"
    data = [{'HTML_ID':html_id, 'TAG_NAME':tag_name, 'ATTRIBUTE_ID':attribute_id, 'ATTRIBUTE_NAME':attribute_name, 'ATTRIBUTE_CLASS':attribute_class, 'ATTRIBUTE_PLACEHOLDER':attribute_placeholder, 'IN_FORM':in_form, 'TAG_DEPTH':tag_depth, 'TAG_STRING':tag_string, 'LOGIN_URL':login_url, 'LABEL':label}]
    return df.append(data, ignore_index=True, sort=False)

def getAttribute(soup, attribute):
    if soup.has_attr(attribute):
        return soup[attribute]
    return "None"

def isInForm(parents):
    if "form" in parents:
        return "True";
    
    return "False"