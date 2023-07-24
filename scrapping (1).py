#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests
from bs4 import BeautifulSoup
URL="https://engg.kkwagh.edu.in/academic_programme/photogallery/14"
r = requests.get(URL)
soup=BeautifulSoup(r.content,'html5lib')
print("\nlinks found are\n")
text_data=soup.find_all('div',attrs={'class':'col-sm-4 col-md-4 col-lg-4'})
no_items=len(text_data)
for i in range(no_items):
    found_text=text_data[i].get_text()
    print(found_text)


# In[21]:


import requests
from bs4 import BeautifulSoup
URL="https://engg.kkwagh.edu.in/academic_programme/photogallery/14"
r = requests.get(URL)
soup=BeautifulSoup(r.content,'html5lib')
#print(soup.prettify())
text_data=soup.find_all('div',attrs={'class':'col-sm-4 col-md-4 col-lg-4'})
print(text_data)


# In[25]:


import pandas as pd
                                                                                                            
url = 'http://swsfspl.in/temp/samplefile.html'
dfs = pd.read_html(url)

df = dfs[0]


print(dfs[0]['Company'])  
print(dfs[0]['Country'])

df.to_excel('ScrappedDataFromSimple.xlsx')
print("\n Scrapped Data Moved To Xlsx File")


# In[1]:


import pandas as pd
file = open('CompStaff.csv', 'w', encoding='utf-8')                                                                                              
url = 'https://engg.kkwagh.edu.in/academic_programme/faculty/1'
dfs = pd.read_html(url)

df = dfs[0]


print(dfs[0]['Name of staff'])  


dfs[0]['Name of staff'].to_csv('CompSatff.csv')
print("\n Scrapped Data Moved To Xls File")


# In[ ]:




