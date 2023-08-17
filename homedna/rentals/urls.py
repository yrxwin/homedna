from django.urls import path

from . import views

app_name = "rentals"
urlpatterns = [
    # ex： /rentals/
    path("", views.index, name="index"),
    # ex: /rentals/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /rentals/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /rentals/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]