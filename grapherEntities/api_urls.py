from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import grapherEntityView

app_name = 'grapherEntities'


urlpatterns = [
]

urlpatterns += format_suffix_patterns([

    url(r'^grapherEntity/$',
        grapherEntityView.as_view(),
        name='grapherEntity_list'),

])

