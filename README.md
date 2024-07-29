## FlussTools

Head for Python scripts for river analyses.

The full documentation is available at [https://flusstools.readthedocs.io](https://flusstools.readthedocs.io/en/latest/).

### Issues

We depend on GDAL and GDAL installation is buggy. To enable cross-platform support, we currently need to enforce numpy<2.0.0 because most Linux derivatives run on GDAL v3.6 but numpy2 requires GDAL>=3.9.1.

### Create Requirements.txt

`pip-tools` helps to manage `requirements.txt` with more control. It separates direct dependencies from transitive ones.

1. **Install `pip-tools`**:

```sh
pip install pip-tools
```

2. **Create `requirements.in`**:

   List your direct dependencies in a `requirements.in` file. For example:

```plaintext
requests
numpy
```

3. **Compile `requirements.txt`**:

   Run `pip-compile` to generate `requirements.txt` from `requirements.in`:

```sh
pip-compile requirements.in
```


