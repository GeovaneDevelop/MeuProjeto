from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^(?P<postagens_id>[0-9]+)/resultados/$', views.resultados, name='resultados'),
]