"""Basic imports and functions for flusstools"""

try:
    import csv
    import glob
    import itertools
    import logging
    import os
    import platform
    import shutil
    import subprocess
    import sys
    import urllib
    from pathlib import Path

    from tabulate import tabulate
except ImportError as e:
    raise ImportError(f"Could not import standard libraries:\n{e}")

# import scientific python packages
try:
    import matplotlib.pyplot as plt  # for fuzzycor
    import matplotlib.transforms
    import numpy as np
    from matplotlib import colors, patches
    from scipy import interpolate, stats
except ImportError as e:
    raise ImportError(f"Could not import numpy/matplotlib (is it installed?). {e}")
try:
    import pandas as pd
except ImportError as e:
    raise ImportError(f"Could not import pandas (is it installed?). {e}")

# import osgeo python packages
try:
    from osgeo import gdal, ogr, osr
except ImportError as e:
    raise ImportError(f"Could not import gdal and dependent packages (is it installed?). {e}")

# import other geospatial python packages
try:
    import geopandas
except ImportError as e:
    raise ImportError(f"Could not import geopandas (is it installed?). {e}")
try:
    import alphashape
except ImportError as e:
    raise ImportError(f"Could not import alphashape (is it installed?). {e}")
try:
    import shapely
    from shapely.geometry import LineString, Point, Polygon
except ImportError as e:
    raise ImportError(f"Could not import shapely (is it installed?). {e}")
# try:
#     import fiona
# except ImportError as e:
#     raise ImportError("Could not import fiona (is it installed?). {0}".format(e))
try:
    # install pyshp to enable shapefile import
    import shapefile
except ImportError as e:
    raise ImportError(f"Could not import shapefile (included in pyshp - is it installed?). {e}")
try:
    import geojson
except ImportError as e:
    raise ImportError(f"Could not import fiona (is it installed?). {e}")
try:
    import earthpy.plot as ep
except ImportError as e:
    raise ImportError(f"Could not import earthpy (is it installed?). {e}")
try:
    import rasterio as rio
except ImportError as e:
    raise ImportError(f"Could not import rasterio (is it installed?). {e}")
try:
    import rasterstats
except ImportError as e:
    raise ImportError(f"Could not import rasterstats (is it installed?). {e}")
try:
    import laspy
except ImportError as e:
    raise ImportError(f"Could not import laspy (is it installed?). {e}")
try:
    import mapclassify.classifiers as mc
except ImportError as e:
    raise ImportError(f"Could not import mapclassify (is it installed?). {e}")
try:
    import pyproj
except ImportError as e:
    raise ImportError(f"Could not import pyproj (is it installed?). {e}")
try:
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl
except ImportError as e:
    raise ImportError(f"Could not import scikit-fuzzy (is it installed?). {e}")


# GUI mgmt
try:
    import tkinter as tk
    from tkinter import filedialog, messagebox
except ImportError as e:
    raise ImportError(f"Could not import tkinter (is it installed?). {e}")

# append own directories

sys.path.append(r"" + os.path.abspath(""))
sys.path.insert(0, r"" + os.path.abspath("") + "/geotools")
sys.path.insert(0, r"" + os.path.abspath("") + "/fuzzycorr")
sys.path.insert(0, r"" + os.path.abspath("") + "/lidartools")
sys.path.insert(0, r"" + os.path.abspath("") + "/bed_analyst")
