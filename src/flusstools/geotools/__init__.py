"""Geospatial tools for creating, modifying, and transforming datasets."""

from .dataset_mgmt import coords2offset, get_layer, offset2coords, verify_dataset
from .geotools import float2int, raster2line, raster2polygon, rasterize
from .kml import kmx2other
from .kmx_parser import ModHTMLParser, PlacemarkHandler
from .raster_mgmt import (
    clip_raster,
    create_raster,
    open_raster,
    raster2array,
    remove_tif,
    xy_raster_shift,
)
from .shortest_path import (
    build_graph_from_lines,
    create_shortest_path,
    get_full_path,
    get_path,
    write_geojson,
)
from .shp_mgmt import (
    create_shp,
    get_geom_description,
    get_geom_simplified,
    polygon_from_shapepoints,
    verify_shp_name,
)
from .srs_mgmt import (
    get_esriwkt,
    get_srs,
    get_wkt,
    make_prj,
    reproject,
    reproject_raster,
    reproject_shapefile,
)

__all__ = [
    "coords2offset",
    "get_layer",
    "offset2coords",
    "verify_dataset",
    "float2int",
    "raster2line",
    "raster2polygon",
    "rasterize",
    "kmx2other",
    "ModHTMLParser",
    "PlacemarkHandler",
    "clip_raster",
    "create_raster",
    "open_raster",
    "raster2array",
    "remove_tif",
    "xy_raster_shift",
    "build_graph_from_lines",
    "create_shortest_path",
    "get_full_path",
    "get_path",
    "write_geojson",
    "create_shp",
    "get_geom_description",
    "get_geom_simplified",
    "polygon_from_shapepoints",
    "verify_shp_name",
    "get_esriwkt",
    "get_srs",
    "get_wkt",
    "make_prj",
    "reproject",
    "reproject_raster",
    "reproject_shapefile",
]
