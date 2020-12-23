from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.root),
    path('signup', views.signup),
    path('details', views.details),
    path('order', views.order),
    path('about', views.about),
    path('contact', views.contact),
    path('account', views.account),
    path('admin', views.admin),
    path('like', views.like),
    path('review', views.review),
]
