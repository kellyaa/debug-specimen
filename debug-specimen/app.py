import os
import time
import logging
import urllib.request
import json
from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CONFIG_SERVICE_URL = os.environ.get(
    "CONFIG_SERVICE_URL", "http://config-service:8888/config"
)
CONFIG_REFRESH_INTERVAL = int(os.environ.get("CONFIG_REFRESH_INTERVAL", "60"))

# In-memory config cache
_config = {"version": "default", "features": {}}
_config_last_fetch = 0


def _ensure_config():
    """Refresh config from the config service if the cache is stale."""
    global _config, _config_last_fetch
    now = time.time()
    if now - _config_last_fetch < CONFIG_REFRESH_INTERVAL:
        return
    _config_last_fetch = now
    try:
        resp = urllib.request.urlopen(CONFIG_SERVICE_URL)
        data = json.loads(resp.read().decode())
        _config = data
        logger.info("Config refreshed successfully")
    except Exception as e:
        logger.warning("Failed to fetch config: %s", e)


@app.route("/")
def index():
    _ensure_config()
    version = _config.get("version", "unknown")
    return f"Hello from debug-specimen (config version: {version})\n"


@app.route("/healthz")
def healthz():
    _ensure_config()
    return "OK\n", 200
