# Zonal Statistics

When we want a scope of the behavior of variable in a some,
we reduce this variable to basic zonal statistics.

This module count with two functions to perform zonal statistics one for `ee.Image` and another for `ee.ImageCollection`. Both functions returns a `pandas.DataFrame` with the count, the mean, the maximun, the minimum, the standard deviation and time of the `ee.Image`.

## Zonal Statistics for one ee.Image

```python
zonal_statistics_image(Image:ee.Image, band:str, geom:ee.Geometry, scale:float) -> pandas.DataFrame
```

`zonal_statistics_image()` perform the early mentioned statistics for one `ee.Image` in the specified band. `geom` is the Region of interest and `scale` is the pixel size of the image to perform the algorithm.

This function return a `pandas.DataFrame` with all the statistics.

### Usage

```python
import numpy as np
import pandas as pd
import geopandas as gpd

import ee
from statgis.gee.landsat_functions import landsat_scaler, landsat_cloud_mask, landsat_ndvi_collection
from statgis.gee.time_series_analysis import basic_tsp
from statgis.gee.zonal_statistics import zonal_statistics_image, zonal_statistics_collection

ee.Initialize()

# %% Prepare the data
bqlla = [-74.7963, 10.9638]
roi = ee.Geometry.Rectangle([bqlla[0]-0.05, bqlla[1]-0.05, bqlla[0], bqlla[1]])
L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterBounds(roi)

L8 = L8.map(landsat_scaler).map(landsat_cloud_mask)
ndvi = landsat_ndvi_collection(L8, L8=True, add_bands=False)
ndvi, monthly_mean = basic_tsp(ndvi, 'NDVI')

ene = monthly_mean.first()

# %% Zonal statistics for an ee.Image
zsi = zonal_statistics_image(ene, 'stational_mean', roi, 30)
```

## Zonal Statistics for all ee.Image in an ee.ImageCollection

```python
zonal_statistics_collection(ImageCollection:ee.ImageCollection, band:str, geom:ee.Geometry, scale:float) -> pandas.DataFrame
```

To do the same preocess of `zonal_statistics_image()` for all `ee.Image` in an `ee.ImageCollection` this module count with the `zonal_statistics_collection()` function, this function also return a `pandas.DataFrame` in wich each row contain the statistics for each `ee.Image`.

### Usage

```python
import numpy as np
import pandas as pd
import geopandas as gpd

import ee
from statgis.gee.landsat_functions import landsat_scaler, landsat_cloud_mask, landsat_ndvi_collection
from statgis.gee.time_series_analysis import basic_tsp
from statgis.gee.zonal_statistics import zonal_statistics_image, zonal_statistics_collection

ee.Initialize()

# %% Prepare the data
bqlla = [-74.7963, 10.9638]
roi = ee.Geometry.Rectangle([bqlla[0]-0.05, bqlla[1]-0.05, bqlla[0], bqlla[1]])
L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterBounds(roi)

L8 = L8.map(landsat_scaler).map(landsat_cloud_mask)
ndvi = landsat_ndvi_collection(L8, L8=True, add_bands=False)
ndvi, monthly_mean = basic_tsp(ndvi, 'NDVI')

ene = monthly_mean.first()

# %% Zonal statistics for an ee.ImageCollection
zsc = zonal_statistics_collection(ndvi, 'stational', roi, 30)
```