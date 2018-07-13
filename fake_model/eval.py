#
# eval.py
# Evaluates given fake news Urls,
# checking whether the news articles are fake
#

from bs4 import BeautifulSoup

import requests
import csv
import pandas as pd

URL_SRC= ""

# load model with timestamp in filename
def load_model(name_prefix="sklearn_linearsvc_model", suffix=".pickle"):
    fnames = glob.glob("./models/{}*{}".format(name_prefix, suffix))
    # Pick the most recently built model
    fnames = list(reversed(sorted(fnames)))
    fname = fnames[0]
    
    
    with open(fname, "rb") as f:
        return pickle.load(f)

# Retrieves and parse the contents of urls, returing 2 list with the following
# values:
# titles - title of the article
# text - text of the article 
# img url - image url of the article
def parse_urls(urls):
    titles = []
    texts = []
    img_urls = []
    for url in urls:
        # Retrieve contents of url
        r = requests.get(url)
        soup =  BeautifulSoup(r.text, "html.parser")
        
        # Parse contents of url
        text = ""
        for paragraph in soup.find_all("p"):
            text += "\n{}".format(paragraph.string)
        
            
        imgs = soup.find_all("img")
        if len(imgs) > 0:
            img_urls.append(imgs[0].get("src"))
        titles.append(soup.title.string)
        texts.append(text)
        
    
    return titles, texts, img_urls
    
# Predict the legitmacy for the given news article specfied by the title and text
# returns a list of prediction results, with 1 makring fake news
vectorizer = load_model("sklearn_linearsvc_vectorizer")
model = load_model()
def evaluate_legitmacy(titles, texts):
    full_texts = [ "{}\n{}".format(titles[i], texts[i]) for i in range(len(titles)) ]

    full_texts = vectorizer.transform(full_texts)
    predicts = model.predict(full_texts)
    
    return predicts

    
    
if __name__ == "__main__":
    # Read the data
    df = pd.read_csv(URL_SRC)
    urls.loc[:,"url"]
 
    # Add parsed data to dataframe
    titles, texts, img_urls = parse_urls(urls)
    df["title"] = titles
    df["text"] = texts
    df["img_url"] = img_urls
    df["fake"] = evaluate_legitmacy(titles, texts)

    
    df.to_csv("../backend/menu.csv")
