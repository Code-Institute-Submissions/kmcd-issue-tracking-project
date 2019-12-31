from django.conf.urls import url
from .views import features_home, feature_details, get_features, new_edit_feature, update_feature,new_feature_comment, features_report

urlpatterns = [
    url(r'^features/$', features_home, name="features_home"),
    url(r'^features/new_feature/$', new_edit_feature, name="new_feature"),
    url(r'^features/(?P<pk>\d+)-(?P<view_comments>[y,n])/$', feature_details, name='feature_details'),
    url(r'^features/(?P<pk>\d+)/edit/$', new_edit_feature, name='edit_feature'),
    url(r'^features/(?P<pk>\d+)/update/$', update_feature, name='update_feature'),
    url(r'^features/featurelist$', get_features, name="get_features"),
    url(r'^features(?P<pk>\d+)/comments/$', new_feature_comment, name='new_feature_comment'),
    url(r'^featuresreport/$', features_report, name='features_report'),
]