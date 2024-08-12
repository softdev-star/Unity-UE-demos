import json
import os
from GPSPhoto import gpsphoto
import copy

defualtFeature = {
    'type': 'Feature',
    'properties': {
        'description': "",
        'image': "",
        'imageloc': "",
        'icon': 'attraction'
    },
    'geometry': {
        'type': 'Point',
        'coordinates': [0,0]
    }
}
os.chdir("C:\\Users\\Xenolupus\\Desktop\\GithubWebsite\\softdev-star.github.io\\japanquest\\photos")
images = os.listdir()
images = [a for a in images if a.endswith('jpg')]
features = []
for a in images: 
  data = gpsphoto.getGPSData(os.getcwd() + f'\\{a}')
  newFeature = copy.deepcopy(defualtFeature)
  newFeature['properties']['image'] = "<img src=\"photos/"+a+"\" id=\"photo\">"
  newFeature['properties']['imageloc'] = "url(photos/"+a+")"
  newFeature['properties']['description'] = "<img src=\"photos/"+a+"\" id=\"photo\">"
  newFeature['geometry']['coordinates'] = [data['Longitude'], data['Latitude']]
  features.append(newFeature)


geoData = {
  'type': 'FeatureCollection',
  'features': features
}

result_json = json.dumps(geoData, indent=3)
#print(result_json)

with open("C:\\Users\\Xenolupus\\Desktop\\GithubWebsite\\softdev-star.github.io\\japanquest\\result.json", "w") as outfile:
    outfile.write(result_json)
