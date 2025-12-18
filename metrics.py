def log_metric(metrics: list, metric_data: dict) -> dict:
    metric_data["id"] = str(len(metrics) + 1)
    metrics.append(metric_data)
    return metric_data

def metrics_summary(metrics: list, user_id: str, metric_type: str, period: tuple[str, str]) -> dict:
    #tupledaki verileri start ve end atadık
    start, end = period
    
    values = [m["value"] for m in metrics if m["user_id"] == user_id and m["type"] == metric_type and start <= m["date"] <= end]
    total = sum(values)
    # değer varsa ortalama al yoksa 0
    avg = total / len(values) if values else 0
    return {"average": avg, "count": len(values)}


