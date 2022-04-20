from django.conf.urls import url
from django.urls import path

from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'properties'

urlpatterns = [
    path('', views.listings, name='index'),
    path(r'listings', views.listings, name='listings'),
    path(r'profile/<int:property_id>/', views.display_property_profile, name="profile"),
    path(r'add_property_listing', views.add_property_listing,name="add_property_listing"),
    path(r'property_add_error', views.property_add_error,name="property_add_error"),
    path(r'property_add_error', views.property_add_error,name="property_add_error"),
    path(r'create_receipt/<str:propertyId>/', views.create_receipt, name='create_receipt'),
    path(r'update_receipt/<str:receiptId>/<str:propertyId>/', views.update_receipt, name='update_receipt'),
    path(r'delete_receipt/<str:receiptId>/<str:propertyId>/', views.delete_receipt, name='delete_receipt'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
