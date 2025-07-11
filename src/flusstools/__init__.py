import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

try:
    import bedanalyst
    import fuzzycorr
    import geotools
    import lidartools
    from helpers import *
except ModuleNotFoundError:
    print("Failed to initialize FlussTools - consider re-installation")

try:
    logging.getLogger()
except NameError:
    pass
