import ee
from statgis.gee.landsat_functions import landsat_ndvi_collection
from statgis.gee.time_series_analysis import *

ee.Initialize()

bqlla = [-74.83867302723779, 10.99475962094864]

poi = ee.Geometry.Point(bqlla)
L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterBounds(poi)

ndvi = landsat_ndvi_collection(L8)

tsd, monthly_mean = basic_tsp(ndvi, 'NDVI')