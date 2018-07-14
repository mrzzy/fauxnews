from django.http import JsonResponse

import pandas as pd

df = pd.read_csv("../menu.csv")


def truncate(text, length=200):
    return text[:199] + "…"


def get_articles(request):
    """Returns a JsonResponse of the articles in the following form:
    [
        {
            "title": "Omelettes have been banned in 20 counties.",
            "subtitle": "Learn what you can do to prevent this from happening
            in your county.",
            "author": "Pseudononymous Bosch",
            "datePublished": "2018-07-13 8:00:00",
            "excerpt": "The <i>du fromage</i> law has recently been passed in
            20 different counties.",
            "thumbnail_url": "https://www.google.com",
        }
    ]
    """

    data = []
    for index, entry in df.iterrows():
        if entry["fake"] == 1:
            entry_text = entry["text"]
            if not isinstance(entry_text, str):
                entry_text = ""

            data.append({
                "title": entry["title"],
                "author": entry["author"],
                "timestamp": entry["timestamp"],
                "excerpt": truncate(entry_text),
                "thumbnail_url": entry["img_url"],
                "url": entry["url"],
            })

    return JsonResponse(data, safe=False)
