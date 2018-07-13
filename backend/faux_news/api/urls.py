from django.urls import path

import api.views as views

urlpatterns = [
    path("articles/", views.get_articles),
]