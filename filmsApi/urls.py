from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView


urlpatterns = {
    url(r'^film-lists/$', CreateView.as_view(), name="film"),
    url(r'^update/$', CreateView.upload, name="upload"),
}

urlpatterns = format_suffix_patterns(urlpatterns)