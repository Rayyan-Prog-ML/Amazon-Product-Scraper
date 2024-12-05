from bs4 import BeautifulSoup
import os 
import pandas as pd

d={"Name":[],"Price":[],"link":[]}
for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc=f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t=soup.find("h2")
        title=t.get_text()
        p=soup.find("span",attrs={"class":"a-price-whole"})
        price=p.get_text()
        l=t.find("a")
        link="https://amazon.in" + l["href"]
        d["Name"].append(title)
        d["Price"].append(price)
        d["link"].append(link)
    
    except Exception as e:
        print(e)


#cleaning the data
df=pd.DataFrame(d)
df.set_index("Name", inplace=True) #inplace is for updating the dataframe in real time
df["Price"]=df["Price"].str.replace(",","").astype(float)
# df["Price"].head()
# df.drop_duplicates(inplace=True)
# df.drop_duplicates(subset='Name', inplace=True) # subset ka matlab us col ki aagr duplicate val hogi to puri row ko hatadia jaga
# df.dropna(inplace=True)  #to drop missing val 
# df["Price"].fillna(0,inplace=True) #apni marzi ki val
df.to_csv("New cleaining Amazonss-Products.csv")




