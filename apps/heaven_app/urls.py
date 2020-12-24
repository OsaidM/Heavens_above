from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.root),
<<<<<<< HEAD
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('signup', views.signup),
    path('details', views.details),
=======
    path('search', views.search),
    path('autocomplete', views.autocomplete, name="autocomplete"),
    path('signup', views.signup),
    path('details/<int:p_id>', views.details),
>>>>>>> 1f3de7e9e6ce4b31d74774df3f861a4d838d8306
    path('order', views.order),
    path('about', views.about),
    path('contact', views.contact),
    path('account', views.account),
    path('admin', views.admin),
<<<<<<< HEAD
=======
    path('like/<int:p_id>', views.like),
    path('review', views.review),
>>>>>>> 1f3de7e9e6ce4b31d74774df3f861a4d838d8306
]
