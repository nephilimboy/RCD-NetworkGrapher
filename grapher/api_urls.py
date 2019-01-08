from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import LogParserView, CustomPatternView

app_name = 'companies'


urlpatterns = [
]

urlpatterns += format_suffix_patterns([

    url(r'^logParser/$',
        LogParserView.as_view(),
        name='logParser_list'),

    url(r'^customPattern/$',
        CustomPatternView.as_view(),
        name='custom_pattern_list'),

    url(r'^customPattern/(?P<pk>\d+)/$',
        CustomPatternView.as_view(),
        name='custom_pattern_list'),
])

