import arxiv
import pandas as pd
import nltk
from nltk.corpus import stopwords
import streamlit as st
from collections import Counter
import matplotlib.pyplot as plt
import altair as alt

stopwords = set(stopwords.words('english'))



test = arxiv.query(query="cat:stat.AP", sort_by="lastUpdatedDate", max_results=10000)




papers = []

for i in range(len(test)):
    paper = []
    paper.append(test[i].get('updated').split("-")[0])
    paper.append(test[i].get('updated').split("-")[1])    
    title = (str(test[i].get('title')).casefold())
    paper.append(title)
    words = title.split()
    key_words = ""
    for r in words:  
        if not r in stopwords:
            key_words = key_words + " " + r
    paper.append(key_words)
    papers.append(paper)


df = pd.DataFrame(papers)
df.columns = ["year", "month", "title", "key_words"]

df19 = df.loc[df["year"] == "2019"]
df20 = df.loc[df["year"] == "2020"]
df21 = df.loc[df["year"] == "2021"]










count_19 = Counter(" ".join(df19["key_words"]).split()).most_common(100)

prc_19 = []
for i in range(len(count_19)):
    
    print(count_19[i])
    prc_19.append(list(count_19[i]))


for i in range(len(prc_19)):
    prc_19[i][1] = (int(prc_19[i][1])/len(df19))*100

dfperc = pd.DataFrame.from_records(prc_19)

dfperc.columns = ["key_word", "2019"]

count_20 = Counter(" ".join(df20["key_words"]).split()).most_common(100)

prc_20 = []
for i in range(len(count_20)):
    
    print(count_20[i])
    prc_20.append(list(count_20[i]))


for i in range(len(prc_20)):
    prc_20[i][1] = (int(prc_20[i][1])/len(df20))*100

dic20 = {}

for i in prc_20:
    dic20[i[0]] = i[1:]


dfperc["2020"] = dfperc["key_word"].map(dic20)
dfperc["2020"] = dfperc["2020"].map(lambda x: x if not isinstance(x, list) else x[0] if len(x) else '')


count_21 = Counter(" ".join(df21["key_words"]).split()).most_common(100)

prc_21 = []
for i in range(len(count_21)):
    
    print(count_21[i])
    prc_21.append(list(count_21[i]))


for i in range(len(prc_21)):
    prc_21[i][1] = (int(prc_21[i][1])/len(df21))*100

dic21 = {}

for i in prc_21:
    dic21[i[0]] = i[1:]


dfperc["2021"] = dfperc["key_word"].map(dic21)
dfperc["2021"] = dfperc["2021"].map(lambda x: x if not isinstance(x, list) else x[0] if len(x) else '')

dfperc = dfperc.set_index("key_word")


st.title("Keyword in Arxiv titlkes")
st.write("This small scripts download 10000 paper titles from the categorie Applied Statistics of the preprint repository Arxiv, in order to analyze the percentage of key_words that appear in the titles year by year.")
st.write(dfperc)
st.line_chart(dfperc)

