from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.landing, name='landing'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^new/profile/$', views.edit, name='new-profile'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^project/(\d+)$', views.single_project, name='project'),
    url(r'^rating/(\d+)$', views.review_rating, name="review"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'^api/merch1/$', views.MerchList2.as_view())

    # url(r'^user_profile/(?P<username>\w+)', views.user_profile, name='user_profile'),
    # # url('^$',views.front, name='front'),
    # url(r'^new/post/$', views.new_post, name='new-post'),
]   