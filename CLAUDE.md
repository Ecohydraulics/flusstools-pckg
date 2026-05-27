# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`flusstools` is a published PyPI package (https://pypi.org/project/flusstools/) of Python tools for
river, floodplain, and hydro-morphological analysis. Source lives in `src/flusstools/` (src-layout).
The package is documented from a **separate repository** — `flusstools-docs` (Ecohydraulics/GitHub),
**locally cloned at `/home/schwindt/github/flusstools-docs/`**. The `docs/` folder here only holds
contributor/build notes, not the rendered Sphinx docs. readthedocs builds from `flusstools-docs`, and
code changes here do **not** auto-sync there (see `docs/CONTRIBUTING.md` — gdal cannot be imported on
readthedocs, so docs are updated manually): edit the local `flusstools-docs` clone, then commit/push it.

## Environment

GDAL is the central pain point. As of 2.0.0 it **is** declared as a runtime dependency (`gdal>=3.10`),
so `pip install flusstools` will pull it — but GDAL ships **no PyPI wheels**, so pip compiles it against
the *system* libgdal (`gdal-config` must be on PATH and the versions must match). On a machine without a
system GDAL the pip build fails; use conda there instead. The dev environment is defined in
`environment.yml` (conda env name `flussenv`, conda-forge, GDAL 3.10–3.11 / NumPy-2 ABI). Use it for
anything that imports the package:

```sh
mamba env create -f environment.yml      # first time
mamba run -n flussenv python -c "import flusstools"
```

(The global default `wrr-proj` env does **not** have the geospatial stack; use `flussenv` here.)

## Common commands

```sh
mamba run -n flussenv python -m build            # build sdist + wheel into dist/ (hatchling backend)
mamba run -n flussenv python -m pytest           # run tests (see caveat below — tests/ is empty)
mamba run -n flussenv python -m pytest tests/test_x.py::test_fn   # single test
mamba run -n flussenv ruff check src             # lint (config in pyproject.toml [tool.ruff])
mamba run -n flussenv ruff format src            # format (line-length 100)
mamba run -n flussenv mypy src                   # type check (strict, py3.13)
pip-compile requirements.in                      # regenerate requirements.txt (needs pip-tools)
```

Version is hard-coded in `pyproject.toml` (`version = "2.0.1"`) despite `hatch-vcs` being listed —
bump it there. Release/publish steps (twine, git tag `vX.Y.Z`) are in `docs/CONTRIBUTING.md`.

## Architecture

The package uses **explicit, per-module imports** (refactored away from the former global `import_mgmt`
hub + `sys.path` manipulation — do not reintroduce those). Each module imports the stdlib/third-party
packages it actually uses, and intra-package symbols are imported **relatively from their defining
module**.

- `var_config.py` — pure constants only (`cache_folder`, `nan_value`, `gdal_dtype_dict`, `sql_command`).
  Import the names you need: `from ..var_config import nan_value`. Imports only `os`.
- `helpers.py` — cross-cutting utilities (`cache`, `err_info`, `get_file_names`, `remove_directory`, …),
  imported explicitly. **Note:** these helpers are not used anywhere inside the package; they exist purely
  as a public API re-exported at the top level via `flusstools.<fn>`.
- `__init__.py` files are the **public-API aggregators**: each imports its submodules' public names
  explicitly and declares `__all__`. The top-level `flusstools/__init__.py` imports the three subpackages
  and re-exports `helpers`.

Three feature subpackages:

- `geotools/` — raster/shapefile/SRS/KML processing (the gdal-heavy core). Real internal dependency
  graph (leaf → consumer): `raster_mgmt` + `shp_mgmt` → `dataset_mgmt` → `srs_mgmt`; `kmx_parser` →
  `kml`; `geotools.py` pulls from `raster_mgmt`/`shp_mgmt`/`srs_mgmt`/`dataset_mgmt`. `shortest_path.py`
  is standalone. `geotools/__init__.py` aggregates the full public API.
- `fuzzycorr/` — fuzzy map comparison (uses `skfuzzy`); `prepro`, `plotter`, `fuzzycomp` (internal
  cross-links: `fuzzycomp` imports `read_raster` from `plotter`; `prepro` imports `rasterize` from
  `geotools.geotools`), aggregated by `fuzzycorr.py`. `convertor.py` is a standalone script (runs file
  conversions at import — not imported by the package).
- `bedanalyst/` — riverbed clogging analysis: `config` (constants) → `utils` → `degree_clogging`;
  `interp_z2shp` is standalone.

`geotools` is a (small) dependency of `fuzzycorr`: `prepro.plain_raster` delegates to
`geotools.geotools.rasterize` instead of duplicating the GDAL rasterization (the earlier `clip_raster`
duplicate was removed). The old `from geotools import *` star-imports are gone — only this one explicit
symbol is pulled. `bedanalyst` remains independent of the other two subpackages.

## Known issues to be aware of

These are the active problems this repo was flagged for — verify against current state before assuming:

- **GDAL is now a declared dependency (`gdal>=3.10`), but has no PyPI wheels.** `pip install flusstools`
  pulls every requirement including GDAL, yet GDAL compiles against the *system* libgdal — so the pip
  install only succeeds where `gdal-config` is present and version-matched; otherwise use conda
  (`environment.yml`). The full import set is declared (incl. `scikit-fuzzy`/`skfuzzy`, used only by
  `bedanalyst`, and `pyproj`). Because GDAL is now a dep, the **docs repo installs flusstools `--no-deps`**
  on Read the Docs (`.readthedocs.yaml` post_install) and mocks the heavy imports in `conf.py`.
- **`hatch-vcs` is declared but unwired.** It's in `[build-system].requires`, yet `version` is hard-coded
  in `pyproject.toml` while `vX.Y.Z` git tags exist. Consider switching to dynamic VCS versioning
  (`dynamic = ["version"]` + `[tool.hatch.version] source = "vcs"`) — left as-is here because the build
  backend isn't installed in `flussenv` and the change can't be build-tested.
- **NumPy version conflict in docs vs. metadata.** `README.md` says "enforce numpy<2.0.0" (old GDAL 3.6
  constraint), but `pyproject.toml` and `environment.yml` now require numpy>=2.3 (GDAL 3.10+). The README
  note is stale.
- **`tests/` is empty** even though pytest/pytest-cov/pytest-xdist are configured. There is no CI
  (`.github/` does not exist). Any "run the tests" request currently has nothing to run.
- **Ruff is configured permissively** — many docstring/import/style codes are ignored (see
  `[tool.ruff.lint].ignore`), and `docs` + `tests/data` are excluded. `F401` is allowed in `__init__.py`
  because those files re-export the public API.

## Conventions

- Docstrings use **Google style** (`Args:` / `Returns:`) and are rendered by the external docs repo —
  keep them accurate; some carry inline warnings like `!!!FUNCTION NOT YET DEBUGGED!!!` (e.g.
  `helpers.lookup_value`).
- Public API is what each `__init__.py` (and `fuzzycorr.py`) re-exports via `__all__`. Renaming or
  removing a listed function is a breaking change for downstream users and the docs repo; when you add a
  public function, add it to the relevant `__all__`.
- When a module needs a stdlib/third-party package or an intra-package symbol, add an explicit import at
  the top (relative, from the defining module for intra-package). Never re-add a global import hub or
  `sys.path` manipulation.
