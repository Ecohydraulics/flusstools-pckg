## FlussTools

`flusstools` is a Python toolbox for river, floodplain, and hydro-morphological analysis.

📖 **Documentation:** [flusstools.readthedocs.io](https://flusstools.readthedocs.io/en/latest/) &nbsp;•&nbsp; 📦 **PyPI:** [pypi.org/project/flusstools](https://pypi.org/project/flusstools/)

### Modules

- **`geotools`** – raster, shapefile, projection (SRS), and KML processing (GDAL-based)
- **`fuzzycorr`** – fuzzy-set map comparison to assess the accuracy of (numerical) river models
- **`bedanalyst`** – riverbed clogging analysis

### Installation

`flusstools` builds on **GDAL**, which has no pre-built PyPI wheel. The recommended, platform-independent way to install is therefore a **conda/mamba** environment:

```sh
mamba create -n flussenv -c conda-forge python=3.11 gdal
mamba activate flussenv
pip install flusstools
```

A plain `pip install flusstools` works **only** where a matching system GDAL is present (`gdal-config` on your `PATH`); otherwise pip tries to compile GDAL and fails. See the [installation guide](https://flusstools.readthedocs.io/en/latest/getstarted.html) for details.

### Contributing & development

The development environment is defined in `environment.yml` (conda, GDAL 3.10+ / NumPy-2 ABI):

```sh
mamba env create -f environment.yml
mamba activate flussenv
pip install -e . --no-deps
```

Runtime dependencies are declared in `pyproject.toml`; the pinned `requirements.txt` is regenerated from `requirements.in` with [`pip-tools`](https://github.com/jazzband/pip-tools) (`pip-compile requirements.in`). The full contribution and release workflow is on the [Contributing page](https://flusstools.readthedocs.io/en/latest/contribute.html) and in [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md).

### License

BSD license — see [`LICENSE`](LICENSE).
