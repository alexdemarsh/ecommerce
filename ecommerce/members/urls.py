from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.members, name='members'),
    # url(r'^$', views.signup, name='signup'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', views.authenticate_user, name='authenticate_user'),
    url(r'^signin/', views.login_user, name='login_user'),
    url(r'^logout/', views.logout_view, name='logout_view'),
    url(r'^showall/', views.showall, name='showall'),
    url(r'^showlatest/', views.showlatest, name='show latest'),
    url(r'^listing/$', views.listing, name='listing'),
    url(r'^showone/', views.showone, name='showone'),
    url(r'^listing/(?P<item_id>[0-9]+)/add/', views.add, name='add'),
]