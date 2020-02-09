# ASI - Automatic Sign In - ML Based Technology
![alt text](https://i.ibb.co/QMC15WY/Screen-Shot-2019-08-13-at-15-22-59.png)

ASI can perform automatic login with machine learning based techniques. It learns the HTML structure of many banks, and when given a new login page it can find the necessary elements (username, password and submit button) to perform the login automatically.

Feature Extraction from HTML:

Html Iterator (Class):
  1. Holds pandas instance with the data
  2. Iterate over Login urls
  3. Get the html response.
  4. Call Html parser for each Html


Html parser (Class):
  1. Takes body of html
  2. Takes features for the current element (skip if body)
  3. get All children
  4. If there are no children -> return

Model (Class):
  1. feature engineering
  2. Categorization (0,1,2,3)
  3. return raw data of categorized element

Features required:
- HTML_ID (will not be used in the model but will help us identify different htmls)
- TAG_NAME
- ATTRIBUTE_ID (Empty if doesn't have)
- ATTRIBUTE_NAME (Empty if doesn't have)
- ATTRIBUTE_CLASS (Empty if doesn't have)
- ATTRIBUTE_CLASS (Empty if doesn't have)
- ATTRIBUTE_PLACEHOLDER (Empty if doesn't have)
- IN_FORM (boolean true/false)
- TAG_DEPTH
- TAG_STRING
- LABEL (0,1,2,3)   0 - Other, 1 - User name, 2 - Password, 3 - Submit
