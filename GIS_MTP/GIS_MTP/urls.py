from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', views.map_view, name='map_view'),
    path('gis-data/', views.gis_data_view, name='gis-data'),
    path('district-gis-data/', views.district_data_view, name='district-gis-data'),
    path('get-precipitation/<str:district_name>/', views.get_precipitation_data, name='get_precipitation_data'),
    # path('create-matplotlib-plot/<str:district_name>/', views.create_matplotlib_plot, name='create_matplotlib_plot'),
    path('get-precipitation-csv/<str:district_name>/', views.get_precipitation_csv_data, name='get_precipitation_csv_data'),

]
