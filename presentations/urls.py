from django.urls import  path
from .views import ListPrezis


urlpatterns = [
    path('', ListPrezis.as_view(), name="all_prezis"),
]