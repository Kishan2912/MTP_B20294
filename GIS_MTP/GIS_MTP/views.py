import re
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from .models import *
from django.shortcuts import render
from django.db.models import F

from django.http import HttpResponse
import csv
from .models import DistrictData


def map_view(request):
        # Your view logic here
        return render(request, 'map.html')  # Replace with your actual template

# State-layer data
def gis_data_view(request):
        # Query the GIS data from the database
        queryset = GIS.objects.all()

        # Serialize the queryset with the simplified geometries
        geojson_data = serialize('geojson', queryset, geometry_field='geom')

        return HttpResponse(geojson_data, content_type='application/json')

# district layer
def district_data_view(request):
        # Query the GIS data from the database
        queryset = GIS_District.objects.all()

        # Serialize the queryset with the simplified geometries
        geojson_data = serialize('geojson', queryset, geometry_field='geom')

        return HttpResponse(geojson_data, content_type='application/json')


# Pcp time series data view (using chart js)
def get_precipitation_data(request, district_name):
        # Fetch precipitation data for the given district name
        # Convert district_name to lowercase
        if district_name=='Lahul & Spiti':
            district_name='lahul_spiti'
        else:
            district_name = district_name.lower()
            # Replace spaces with underscores and ignore special characters
            district_name = re.sub(r'[^a-zA-Z0-9\s]', '', district_name).replace(' ', '_')
            
        # Fetch precipitation data for the modified district name
        print(district_name, "district name show")
        print(district_name,"district name show")
        try:
            # Retrieve only 'date' and the specified district field
            district_data = DistrictData.objects.values('date', district_name)
            
            # Convert data to separate arrays for labels and data
            labels = [entry['date'] for entry in district_data]
            precipitation_data = [entry[district_name] for entry in district_data]

            return JsonResponse({'labels': labels, 'precipitation_data': precipitation_data}, safe=False)
        except DistrictData.DoesNotExist:
            return HttpResponse(status=404)
        except Exception as e:
            return HttpResponse(status=500)
        



# for downloading csv data
def get_precipitation_csv_data(request, district_name):
    try:
        # Fetch evapotranspiration data for the modified district name
        if district_name == 'Lahul & Spiti':
            district_name = 'lahul_spiti'
        else:
            district_name = district_name.lower()
            district_name = re.sub(r'[^a-zA-Z0-9\s]', '', district_name).replace(' ', '_')

        district_data = DistrictData.objects.values('date', district_name)

        # Create a CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={district_name}_precipitation.csv'

        # Create a CSV writer and write the header
        csv_writer = csv.writer(response)
        csv_writer.writerow(['Date', 'Precipitation'])

        # Write data rows
        for entry in district_data:
            csv_writer.writerow([entry['date'], entry[district_name]])

        return response
    except Exception as e:
        return HttpResponse(status=500)
