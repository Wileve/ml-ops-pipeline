from prometheus_client import Counter

PREDICTIONS = Counter('model_predictions_total', 'Total model predictions')