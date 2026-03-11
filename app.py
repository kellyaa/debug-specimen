import time
from flask import Flask

app = Flask(__name__)
start_time = time.time()
HEALTHY_DURATION_SECONDS = 30


@app.route("/")
def index():
    uptime = int(time.time() - start_time)
    return f"Hello from debug-specimen! Uptime: {uptime}s\n"


@app.route("/healthz")
def healthz():
    uptime = time.time() - start_time
    if uptime > HEALTHY_DURATION_SECONDS:
        return "UNHEALTHY: app has degraded\n", 500
    return "OK\n", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
