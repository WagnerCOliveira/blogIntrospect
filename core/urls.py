from django.urls import path

from .views import IndexView, QuemsouView, ElementsView, BlogView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('quemsou/', QuemsouView.as_view(), name='quemsou'),
    path('elements/', ElementsView.as_view(), name='elements'),
    path('blog/', BlogView.as_view(), name='blog'),
]