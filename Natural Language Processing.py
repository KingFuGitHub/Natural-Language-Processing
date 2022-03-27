import spacy
from newsapi import NewsApiClient
from spacy.lang.en import English
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Natural Language Processing

myList = []

#saves the API dataset locally inside a txt file
text_file = open('/Users/KingFu/Desktop/Class 2022 Spring/CS 4650/[CS4650] HW5/data.txt', 'w')

nlp = spacy.load('en_core_web_lg')

newsapi = NewsApiClient(api_key='02f0ae732bcb4f2db1d77ef4288f237e')

data = newsapi.get_everything(q='coronavirus', language='en', from_param='2022-03-04',
                                to='2022-03-24', sort_by='relevancy', page_size = 100)
articles = data['articles']

for index, article in enumerate(articles):
    print("Article: "+ str(index+1) + ": "+ str(article['title']))
    text_file.write("Article: "+ str(index+1) + ": "+ str(article['title'])+"\n"+str(article['description'])+"\n"+str(article['content'])+"\n\n")
    doc = nlp(article['content'])
    print("Keywords: ")
    for index, ent in enumerate(doc.ents):
        print(str(index+1)+". "+str(ent.text) + " (" + str(ent.label_)+")")
        myList.append(ent.text)
    print()

text_file.close()

unique_string=(" ").join(myList)
wordcloud = WordCloud(width = 1000, height = 500, colormap='tab20c').generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
plt.close()
print(type(articles))




