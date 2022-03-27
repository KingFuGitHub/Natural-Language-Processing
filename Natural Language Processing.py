import spacy
from newsapi import NewsApiClient
from spacy.lang.en import English
# Natural Language Processing
nlp = spacy.load('en_core_web_lg')

newsapi = NewsApiClient(api_key='02f0ae732bcb4f2db1d77ef4288f237e')

data = newsapi.get_everything(q='coronavirus', language='en', from_param='2022-03-04',
                                to='2022-03-24', sort_by='relevancy', page=5)
articles = data['articles']

for index, x in enumerate(articles):
    print("Article: "+ str(index+1) + ": "+ str(x['title']))
    doc = nlp(x['content'])
    print("Keywords: ")
    for index, ent in enumerate(doc.ents):
        print(str(index+1)+". "+str(ent.text) + " (" + str(ent.label_)+")")
    print()


