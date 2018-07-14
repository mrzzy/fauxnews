#
# eval.py
# Evaluates given fake news Urls,
# checking whether the news articles are fake
#

from bs4 import BeautifulSoup

import requests
import csv
import pandas as pd
import glob
import pickle 
import sys
from urllib.parse import unquote

from multiprocessing.pool import Pool
from multiprocessing import cpu_count

URL_SRC = "../scraper/facebook_urls.csv"
 

# load model with timestamp in filename
def load_model(name_prefix="sklearn_linearsvc_model", suffix=".pickle"):
    fnames = glob.glob("./models/{}*{}".format(name_prefix, suffix))
    # Pick the most recently built model
    fnames = list(reversed(sorted(fnames)))
    fname = fnames[0]
    
    
    with open(fname, "rb") as f:
        return pickle.load(f)

# convert those pesky facebook urls to normal urls
def convert_urls(urls):
    no_fb_urls = [ url.replace("https://l.facebook.com/l.php?u=","") for url in urls ]
    unencoded_urls = [ unquote(url) for url in no_fb_urls ]
    
    return unencoded_urls
    
    
# Retrieves and parse the content one url, tuple of the following
# values:
# titles - title of the article
# text - text of the article 
# img url - image url of the article
def parse_url(url):
    try:
        # Retrieve contents of url
        # Lie that we a browser not a damned web crawer
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        
        # Parse contents of url
        text = ""
        for paragraph in soup.find_all("p"):
            text += "\n{}".format(paragraph.string)
        
            
        imgs = soup.find_all("img")
        img_url = None if len(imgs) <= 0 else imgs[0].get("src")

        
        title = None if soup.title == None else soup.title.string
        
        print("Parsed {}...".format(url))
    
        return title, text, img_url
    except:
        return None, None, None
        
    
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
    raw_urls = convert_urls(df.loc[:,"url"])
    raw_authors = df.loc[:,"author"]
    raw_timestamps = df.loc[:,"date"]
    
    # Filter out duplicate urls
    duplicate = []
    url_set = set()
    for url in raw_urls:
        if not url in url_set:
            duplicate.append(False)
            url_set.add(url)
        else:
            duplicate.append(True)
        
    
    assert len(duplicate) == len(raw_urls)
    
    filtered_urls = [ raw_urls[i] for i in range(len(raw_urls)) if not duplicate[i] ]
    filtered_authors = [ raw_authors[i] for i in range(len(raw_urls)) if not duplicate[i] ]
    filtered_timestamps = [ raw_timestamps[i] for i in range(len(raw_urls)) if not duplicate[i] ]
    
    # Concurrent retrieval of news article data
    parsed_df = list(map(parse_url, filtered_urls))
    
    # Filter out urls with missing or deleted pages
    urls = [] 
    titles = []
    texts = []
    img_urls = []
    timestamps = []
    authors = []
    
    title_set = set()

    for i, url in enumerate(filtered_urls):
        entry = parsed_df[i]

        if entry[0] != None and not "404" in entry[0].lower() and not "not found" in entry[0].lower() and entry[1] != None and not entry[0] in title_set:
            urls.append(url)
            titles.append(entry[0])
            texts.append(entry[1])
            img_urls.append(entry[2])
            timestamps.append(filtered_timestamps[i])
            authors.append(filtered_authors[i])
            title_set.add(entry[0])
            
        
    assert len(urls) == len(titles) == len(texts) == len(img_urls) == len(timestamps) == len(authors)

    # Rank news as fake or real
    legitmacy_ratings = evaluate_legitmacy(titles, texts)

    df = pd.DataFrame(data={"title": titles, "fake": legitmacy_ratings, "url": urls, "text": texts, "img_url": img_urls, "timestamp": timestamps, "author": authors})
    df = df[df.fake == 1]
    print(df)
    df.to_csv("../backend/menu.csv")
