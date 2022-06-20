# Time Series Analysis

To perform time series processing algoritmhs to `ee.ImageCollection`, the `statgis.gee` subpackage counts with a module named `time series analysis`.

In this module you will find functions for extract dates for `ee.Image`'s in an `ee.imageCollection`, find the linear trend, the stational variation, the anomalies for an `ee.ImageCollection` and calc monthly statisticals for `ee.Image` based in a `ee.ImageCollection`.

## Extract Dates

```python
extract_dates(ImageCollection:ee.ImageCollection) -> pd.DatetimeIndex:
```

The `extract_dates()` function take an `ee.ImageCollection` and returns a `pandas.DatetimeIndex` series with all the dates of the images in the `ee.ImageCollection`.

### Usage

```python
import ee
import pandas as pd
from statgis.gee.time_series_analysis import extrac_dates

ee.Initialize()

# %% Prepare data
bqlla = [-74.839, 10.995] # Visit Barranquilla!

poi = ee.Geometry.Point(bqlla)
L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterBounds(poi)

# %% Extract dates
dates = extract_dates(L8)
```

## Trend and Stational Variation of an ee.ImageCollection

```python
trend(ImageCollection:ee.ImageCollection, band:str) -> ee.ImageCollection:
```

The `trend()` function first calc a time band for all `ee.Image`, next, calc the linear trend of the specified band in the `band` attribute with `ee.Reducer.linearFit()`, next, calc stational variation subtracting the linear trend data to the original data and restore its mean. 

Finally, the function returns a new `ee.ImageCollection` with the raw data, time, predicted (by linear trend), and stational (stational variation with the mean restored) bands for all `ee.Image`.

### Usage

```python
import ee
from statgis.gee.landsat_functions import landsat_ndvi_collection
from statgis.gee.time_series_analysis import trend

ee.Initialize()

# %% Prepare data
bqlla = [-74.839, 10.995] # Visit Barranquilla!

poi = ee.Geometry.Point(bqlla)
L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterBounds(poi)

ndvi = landsat_ndvi_collection(L8, L8=True, addBands=False)

# %% Calc linear trend and stational variation
ndvi = trend(ndvi, 'NDVI')
```

## Reduce ee.ImageCollection to monthly statistical

```python
monthly_calc(ImageCollection:ee.ImageCollectiom, reducer:ee.Reducer, band:str) -> ee.ImageCollection:
```

`monthly_calc()` function calc the statistical function what you set in the `reducer` attribute (it have to be an `ee.Reducer`) for an `ee.ImageCollection` in the specified band (in `band` attribute).

### Usage

```python
import ee
from statgis.gee.landsat_functions import landsat_ndvi_collection
from statgis.gee.time_series_analysis import trend, monthly_calc

ee.Initialize()

# %% Prepare data
bqlla = [-74.839, 10.995] # Visit Barranquilla!

poi = ee.Geometry.Point(bqlla)
L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterBounds(poi)

ndvi = landsat_ndvi_collection(L8, L8=True, addBands=False)

# %% Calc linear trend and stational variation
ndvi = trend(ndvi, 'NDVI')

# %% Calc monthly means
montlhy_mean_ndvi = monthly_calc(ndvi, reducer=ee.Reducer.mean(), band='stational')
```

## Calc anomalies

```python
calc_anomalies(ImageCollection:ee.ImageCollection, monthly_mean:ee.ImageCollection) -> ee.ImageCollection:
```

`calc_anomalies()` function take the `ee.ImageCollection` and add the band `stational_mean` from the second `ee.ImageCollection` with the `monthly_mean` caculated to subtracting this from the first collection to obtain the anomalies.

Returns the first `ee.ImageCollection` with the `stational_mean` and the `anomalies` as bands per image.

### Usage

```python
import ee
from statgis.gee.landsat_functions import landsat_ndvi_collection
from statgis.gee.time_series_analysis import trend, monthly_calc, calc_anomalies

ee.Initialize()

# %% Prepare data
bqlla = [-74.839, 10.995] # Visit Barranquilla!

poi = ee.Geometry.Point(bqlla)
L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterBounds(poi)

ndvi = landsat_ndvi_collection(L8, L8=True, addBands=False)

# %% Calc linear trend and stational variation
ndvi = trend(ndvi, 'NDVI')

# %% Calc monthly means
montlhy_mean_ndvi = monthly_calc(ndvi, reducer=ee.Reducer.mean(), band='stational')

# %% Calc anomalies 
ndvi = calc_anomalies(ndvi, monthly_mean_ndvi)
```

## All in One, Basic Time Series Processing

```python
basic_tsp(imageCollection:ee.ImageCollection, band:str) -> tsp:ee.ImageCollection, monthly_mean:ee.ImageCollection
```

To perform all the process, this module count with the `basic_tsp()` function (TSP=Time Series Processing). This function take an ee.ImageCollection and calc the linear trend, the stational variation, the monthly mean and the anomalies for the spefied band (in `band` attribute).

Returns two `ee.ImageCollection` the first have the band raw data, the predicted values (linear trend), the stational variation, the stational mean and the anomalies, the second one have the monthly mean for the stational variation data.

This function works like a "wrapper" function of all the functions presented here (except for `extract_dates()`).

### Usage

```python
import ee
from statgis.gee.landsat_functions import landsat_ndvi_collection
from statgis.gee.time_series_analysis import *

ee.Initialize()

# %% Prepare data
bqlla = [-74.839, 10.995] # Visit Barranquilla!

poi = ee.Geometry.Point(bqlla)
L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterBounds(poi)

ndvi = landsat_ndvi_collection(L8, L8=True, addBands=False)

# %% Perform the basic time series processing
ndvi, monthly_mean_ndvi = basic_tsp(ndvi, 'NDVI')
```