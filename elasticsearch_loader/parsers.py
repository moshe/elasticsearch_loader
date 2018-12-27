import sys

try:
    import ujson as json
except ImportError:
    import json  # noqa: F401
try:
    import parquet
except ImportError:
    parquet = False

if sys.version_info.major == 2:
    import unicodecsv as csv
else:
    import csv
