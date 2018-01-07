# --This script is built for easily download a map service / feature service from ARCGIS Online services as vector file (json type)--
# NO need of coding knowledge. 
# It dosen't require any GIS software to run, just python 2.
# Nore info (hebrew) can be found here XXXX
# More info of the modul can be found here https://github.com/Schwanksta/python-arcgis-rest-query

# First get the modul  using pip libray:
# 1. enter: cmd in windows run tray
# 2. enter: cd "path to your pip.exe folder" ("cd C:\Python27\Scripts" or something similar)
# 3. enter: pip install arcgis-rest-query

# Edit this file: choose the right service, the right layer id and give a name for your output file.
# Run the script.
# You should see in the script folder the output (a json file).


import arcgis 
import io, json
source = "https://ags.moin.gov.il/arcgis/rest/services/mehoziot_app/MapServer" # set map/feature service path. <----PLEASE FILL
service = arcgis.ArcGIS(source)
layer_id = 2 # set id of the layer. <----PLEASE FILL
shapes = service.get(layer_id)# leave as is for the whole layer or filter with a sql statment (eg: layer_id, where="OBJECTID<=10")
output = 'layer_file_name' # set a name for the output. <----PLEASE FILL

with io.open(output+'.json', 'w', encoding='utf-8') as f: 
  f.write(unicode(json.dumps(shapes, ensure_ascii=False)))


