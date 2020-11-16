from setuptools import setup, find_packages
from pathlib import Path

lines = Path(".").joinpath("__init__.py")
# version = "0.1.2"  # will be overwritten if defined in init
for line in lines.read_text().split("\n"):
    if line.startswith("__version__ ="):
        version = line.split(" = ")[-1].strip('"')
        break

setup(
    name="flusstools",
    version=version,
    python_requires=">=3.4",
    author="FlussTeam",
    author_email="sebastian.schwindt@iws.uni-stuttgart.de",
    url="https://flusstools.readthedocs.io/",
    project_urls={
        "Documentation": "https://flusstools.readthedocs.io/",
        "Funding": "https://www.uni-stuttgart.de/",
        "Source": "https://github.com/Ecohydraulics/flusstools",
        "Tracker": "https://github.com/Ecohydraulics/flusstools/issues",
    },
    # this should be a whitespace separated string of keywords, not a list
    keywords="rivers geo-spatial data processing numerical model validation",
    description="Analyze and design fluvial ecosystems",
    long_description=Path("./README.md").read_text(),
    long_description_content_type="text/markdown",
    license="BSD 3-Clause",
    packages=find_packages(),
    install_requires=[
        "alphashape",
        "descartes",
        "earthpy",
        "gdal",
        "geojson",
        "geopandas",
        "laspy",
        "mapclassify",
        "matplotlib",
        "numpy",
        "pandas",
        "pyshp",
        "rasterio",
        "rasterstats",
        "scipy",
        "shapely",
        "tabulate",
        "tk",
        ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 2 - Pre-Alpha",
    ],
)
