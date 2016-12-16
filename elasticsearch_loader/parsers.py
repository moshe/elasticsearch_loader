try:
    import ujson as json
except ImportError:
    import json  # noqa: F401
try:
    import parquet
except ImportError:
    parquet = False
