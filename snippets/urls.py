from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    # root url
    url(r'^$', views.api_root),
    # snippets urls
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    # highlight url
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    # users urls
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<username>[^/.]+)/$', views.UserDetail.as_view(), name='user-detail'),
]

format_suffix_patterns(urlpatterns)
