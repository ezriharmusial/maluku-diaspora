from django.urls import path, re_path
from . import views


app_name = 'adresboek'

urlpatterns = [
    # ex /adresboek
    path('', views.AdresListView.as_view(), name='adres_lijst'),
    # ex /adresboek/adres/4142EA/13
    path('adres/<slug:slug>/', views.AdresDetailView.as_view(), name='adres_details'),
    # re_path(
    #     r'^adres/(?P<pk>[1-9][0-9]{3}[A-Z]{2}\d+\D*)/$',
    #     views.AdresDetail.as_view(), name='adres_detail'
    # ),
]
