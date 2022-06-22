import ee
import numpy as np

from statgis.gee.landsat_functions import landsat_scaler, landsat_cloud_mask, landsat_ndvi_collection
from statgis.gee.time_series_analysis import basic_tsp
from statgis.gee.sample import sample_image, sample_collection

ee.Initialize()

# %% Prepare data
bqlla = [-74.7963, 10.9638]
roi = ee.Geometry.Rectangle([bqlla[0]-0.05, bqlla[1]-0.05, bqlla[0], bqlla[1]])
L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterBounds(roi)

L8 = L8.map(landsat_scaler).map(landsat_cloud_mask)
ndvi = landsat_ndvi_collection(L8, L8=True, add_bands=False)
ndvi, monthly_mean = basic_tsp(ndvi, 'NDVI')

ene = monthly_mean.first()

# %% Sample an ee.Image
data_ene = sample_image(ene, 'stational_mean', roi, 30)

# %% Sample all ee.Image in an ee.ImageCollection
data_months = sample_collection(monthly_mean, 'stational_mean', roi, 30)