from django.shortcuts import render
import folium
import os
import logging
import time

# Create your views here.

logging.basicConfig(level=logging.DEBUG)


def index(request):
    Base_dir = os.path.dirname(os.path.abspath(__file__))
    isTime = time.time()
    isTime = time.strftime("%A %d %B %Y %H:%M:%S")
    logging.debug(isTime)
    map = folium.Map(location=[65, -15], zoom_start=5)
    folium.Marker(location=[65.2, -15.2]).add_to(map)
    folium.Marker(location=[48.8534, 2.3488], popup="PARIS").add_to(map)
    folium.Marker(location=[40.416775, -3.703790], popup="MADRID").add_to(map)
    folium.Marker(location=[51.5085300,  -0.1257400],
                  popup="LONDRES").add_to(map)
    map.save('%s/Templates/map.html' % Base_dir)
    content = {
        "title": "Titre de l'application",
        "presentation": "Presentation de la carte: %s" % isTime,
    }

    return render(request, 'home.html', content)
