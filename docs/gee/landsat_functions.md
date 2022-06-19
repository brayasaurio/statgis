# Landsat Functions

The module `landsat_functions` allow the user to scale, cloud mask and calc NDVI a Landsat Image from the Surface Reflectance (SR) Collection:

- LANDSAT/LT04/C02/T1_L2
- LANDSAT/LT05/C02/T1_L2
- LANDSAT/LE07/C02/T1_L2
- LANDSAT/LC08/C02/T1_L2
- LANDSAT/LC09/C02/T1_L2

## Scale

```python
landsat_scaler(Image:ee.Image) -> ee.Image
```

With `landsat_scaler()` you can scale an image to SR values only passing to it the `ee.Image` like an attribute. If you want to scale an  `ee.ImageCollection` you can pass this function like an attribuite to the `ee.ImageCollection` method `map()`

### Usage

```python
import ee
from statgis.gee.landsat_functions import landsat_scaler

L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
img = L8.first()

# %% Scale an ee.Image
img = landsat_scaler(img)

# %% Scale an ee.ImageCollection
L8 = L8.map(landsat_scaler)
```

## Cloud masking

```python
landsat_cloud_mask(Image:ee.Image, all:bool=True) -> ee.Image
```

To mask clouds the module counts with `landsat_cloud_mask` functions thit use QA_PIXEL.

The function have 1 mandatory attribuite and 1 optional attribute:

| Attribuite | Type | Default | Level | Descrption |
|---|---|---|---|---|
| Image | ee.Image |  | Mandatory | Image to be masked |
| all | bool | True | Optional | If True, the image will be masked with all the QA_PIXEL parameters: Cirrus, Cloud, Shadow and Snow |
|  |  |  |  | If False, the image will be masked only with Cloud values. |

This function can be mapped to an `ee.ImageCollection`.

### Usage

```python
import ee
from statgis.gee.landsat_functions import landsat_cloud_mask

L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
img = L8.first()

# %% Mask an ee.Image
img = landsat_cloud_mask(img)

# %% Mask images from an ee.ImageCollection
L8 = L8.map(landsat_cloud_mask)
```

## NDVI

To calc NDVI the `landsat_functions` module count with two functions, one to calc CDVI for an `ee.Image` and another to calc NDVI for all `ee.Image` in a `ee.ImageCollection`:

### For one ee.Image

```python
landsat_ndvi(Image:ee.Image, L8:bool=True): -> ee.Image
```

`landsat_ndvi()` calc de NDVI for an ee.Image and add this in a new band. The `L8` attribute tell to the function that the image is from Landsat 8 or 9.

### For all ee.Image in a ee.ImageCollection

```python
landsat_ndvi_collection(ImageCollection:ee.ImageCollection, L8:bool=True, add_bands:bool=False): -> ee.ImageCollection
```

`landsat_ndvi_collection()` calc de NDVI for all `ee.Image` in a `ee.ImageCollection`. The `L8` attribute tell to the function that the images are from Landsat 8 or 9 and the `add_bands` attribute tell to the function you want all the bands or only the NDVI calculated.

### Usage

```python
import ee
from statgis.gee.landsat_functions import landsat_ndvi, landsat_ndvi_collection

L8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
img = L8.first()

# %% NDVI for one ee.Image
ndvi_img = landsat_ndvi(img)

# %% NDVI for a ee.ImageCollection
L8_ndvi = landsat_ndvi_collection(L8, L8=True, add_bands=False)
```