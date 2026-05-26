"""Package-wide constants for flusstools.

This module defines plain configuration constants only. Import the specific
names you need, e.g. ``from ..var_config import nan_value``.
"""

import os

cache_folder = os.path.abspath("") + "/__cache__/"
nan_value = -9999.0

gdal_dtype_dict = {
    0: "gdal.GDT_Unknown",
    1: "gdal.GDT_Byte",
    2: "gdal.GDT_UInt16",
    3: "gdal.GDT_Int16",
    4: "gdal.GDT_UInt32",
    5: "gdal.GDT_Int32",
    6: "gdal.GDT_Float32",
    7: "gdal.GDT_Float64",
    8: "gdal.GDT_CInt16",
    9: "gdal.GDT_CInt32",
    10: "gdal.GDT_CFloat32",
    11: "gdal.GDT_CFloat64",
}

sql_command = """
CREATE TABLE IF NOT EXISTS plants (
species VARCHAR(255),
name VARCHAR(255),
nativ BOOLEAN,
endangered VARCHAR(255),
habitat VARCHAR(255),
waterdepthmin INTEGER(255),
waterdepthmax  INTEGER(255),
rootdepth INTEGER(255),
groundwatertablechange VARCHAR(255),
floodheightmax INTEGER(255),
floodloss REAL(255),
floodduration INTEGER(255),
PRIMARY KEY (species, name, habitat)
);"""
