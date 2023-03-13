from django.contrib import admin
from django.urls import path
from employee import views

# make up of a url is the name of the route  , package with templates and then method in templates function.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('checkout/<int:id>', views.checkout),
    path('checkoutpay', views.checkoutpay),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('', views.show)
]


