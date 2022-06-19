# Statgis Toolbox

`statgis` is a Python package developed and maintained by StatGIS.org used to perform several spatial data science analysis.This package counts with function operate with Google Earth Engine.

## Dependencies

This package depends of [earthengine-api](https://developers.google.com/earth-engine/tutorials/community/intro-to-python-api) and [geopandas](https://geopandas.org/en/stable/getting_started.html).

```bash
$ conda install geopandas
$ conda install earthengine-api
```

To use `earthengine-api` you have to sing up to [Google Earth Engine](https://earthengine.google.com/new_signup/) and authneticate with the comand `Authenticate()`.

```Python
import ee

ee.Authenticate()
```

## Installation

To install `statgis` you only have to run the `pip install` comand:

```bash
$ pip install statgis
```

## Credits

All the attribution of the development and maintance of this package is for StatGIS.org and its developers team:

- Sebástian Narváez.
- Brayan Navarro.
- Cristian Carrascal.