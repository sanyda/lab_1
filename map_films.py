import geopy
from geopy.geocoders import Nominatim
import folium


def get_data(string):
    year = string.split(')')[0][-4:]
    film_name = string.split('(')[0][:-1]
    if "'" in film_name:
        for i in film_name:
            if i == "'":
                film_name = film_name[:film_name.index(i)] + film_name[film_name.index(i)+1:]
    if ')'and'(' in string.split('\t')[-1]:
        film_location = string.split('\t')[-2]
    else:
        film_location = string.split('\t')[-1]

    result = [film_name,year,film_location]
    return result


required_year = input("please input the year you want")

file = open("locations.list",'r')
data = file.read()
lines = data.split('\n')


map = folium.Map()
fg = folium.FeatureGroup(name ="Film map")
geolocator = Nominatim()
a = 0
for i in range(len(lines)-16):
    if get_data(lines[i+14])[1] == required_year:
        print(get_data(lines[i+14]))
        location = geolocator.geocode(get_data(lines[i+14])[2],timeout=100)
        if isinstance(location, geopy.location.Location) == True:
            a+=1
            fg.add_child(folium.Marker(location=(location.latitude, location.longitude), popup=get_data(lines[i + 14])[0],
                                       icon=folium.Icon()))
            if a >= 100:
                break
        else:
            pass
map.add_child(fg)
map.save("Film_map.html")
        




