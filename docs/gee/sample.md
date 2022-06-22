# Sample 

With this module you can sample all raster values in an ee.Image or an ee.ImageCollection with the function `sample_image()` and `sample_collection()` respectly.

## sample an ee.Image in a Specific Region

```python
sample_image(Image:ee.Image, band:str, geom:ee.Geometry, scale:float) -> np.array
```

The `sample_image()` function take a ee.Geometry (or `ee.Feature` or `ee.FeatureCollection`) and sample all the pixel values in the specified band from the `ee.Image`. The `scale` attribute refers to the pixel size of the image (minor scale more data).

### Usage

```Python
import ee

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
```

## Sample all ee.Image in an ee.ImageCollection in a Specific Region

```python
sample_collection(ImageCollection:ee.ImageCollection, band:str, geom:ee.Geometry, scale:float) -> list
```

The `sample_collection()` function take the `sample_image()` function and apply it to the entire `ee.ImageCollection`. To perform this, this function use a `for` loop, so it's require time.

## Usage

```Python
import ee

from statgis.gee.landsat_functions import landsat_scaler, landsat_cloud_mask, landsat_ndvi_collection
from statgis.gee.time_series_analysis import basic_tsp
from statgis.gee.sample import sample_collection

ee.Initialize()

# %% Prepare data
bqlla = [-74.7963, 10.9638]
roi = ee.Geometry.Rectangle([bqlla[0]-0.05, bqlla[1]-0.05, bqlla[0], bqlla[1]])
L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterBounds(roi)

L8 = L8.map(landsat_scaler).map(landsat_cloud_mask)
ndvi = landsat_ndvi_collection(L8, L8=True, add_bands=False)
ndvi, monthly_mean = basic_tsp(ndvi, 'NDVI')

# %% Sample all ee.Image in an ee.ImageCollection
data_months = sample_collection(monthly_mean, 'stational_mean', roi, 30)
```
