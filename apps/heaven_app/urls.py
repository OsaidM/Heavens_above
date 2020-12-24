from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.root),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('signup', views.signup),
    path('search', views.search),
    path('autocomplete', views.autocomplete, name="autocomplete"),
    path('details/<int:p_id>', views.details),
    path('account/<int:u_id>', views.account),
    path('update/<int:u_id>', views.update),
    path('order', views.order),
    path('account/about', views.about),
    path('account/contact', views.contact),
    path('admin', views.admin),
    path('like/<int:p_id>', views.like),
    path('review', views.review),
]