import arxiv

import pandas as pd
import nltk
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))


from collections import Counter




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










count_19 = Counter(" ".join(df19["key_words"]).split()).most_common(100)
Counter(" ".join(df20["key_words"]).split()).most_common(100)