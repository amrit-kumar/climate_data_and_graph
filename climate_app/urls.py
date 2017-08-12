from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^download_climate_files', views.download_climate_files, name='download_files'),
    url(r'^text_yearwise_data', views.text_yearwise_data, name='yearwise_data'),
    url(r'^convert_to_csv/(?P<id>.*)$', views.convert_to_csv, name='export_csv'),

   ]