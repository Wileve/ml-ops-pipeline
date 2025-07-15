
import time
import random
from prometheus_client import start_http_server, Gauge

# Create Prometheus metrics
MODEL_PREDICTIONS = Gauge('model_predictions_total', 'Total number of predictions made by the model')
MODEL_LATENCY = Gauge('model_prediction_latency_seconds', 'Latency of model predictions in seconds')
MODEL_ACCURACY = Gauge('model_accuracy_score', 'Current accuracy score of the model')

def generate_metrics():
    while True:
        # Simulate model activity
        MODEL_PREDICTIONS.inc(random.randint(10, 100))
        MODEL_LATENCY.set(random.uniform(0.05, 0.5))
        MODEL_ACCURACY.set(random.uniform(0.85, 0.99))
        print("Metrics updated...")
        time.sleep(random.randint(5, 15))

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000.")
    # Generate random metrics in the background.
    generate_metrics()

# Commit 1 marker: 2023-05-01 09:00:00

# Commit 2 marker: 2023-08-10 11:00:00

# Commit 3 marker: 2023-11-15 15:00:00

# Commit 4 marker: 2024-03-01 10:00:00

# Commit 5 marker: 2024-06-05 14:00:00

# Commit 6 marker: 2024-09-01 11:00:00

# Commit 7 marker: 2024-12-10 16:00:00

# Commit 8 marker: 2025-04-01 09:00:00

# Commit 9 marker: 2025-07-15 13:00:00
