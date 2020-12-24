from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.root),
    path('search', views.search),
    path('autocomplete', views.autocomplete, name="autocomplete"),
    path('signup', views.signup),
    path('details/<int:p_id>', views.details),
    path('order/<int:p_id>', views.order),
    path('order/post_order/<int:p_id>', views.post_order),
    path('about', views.about),
    path('contact', views.contact),
    path('account', views.account),
    path('admin', views.admin),
    path('like/<int:p_id>', views.like),
    path('review/<int:p_id>', views.review),
]
