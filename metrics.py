def log_metric(metrics, metric_data):
    metrics.append(metric_data)
    return metric_data


def metrics_summary(metrics, user_id, metric_type, period):
    start_date, end_date = period
    values = []

    for metric in metrics:
        if metric['user_id'] == user_id and metric['type'] == metric_type:
            if start_date <= metric['date'] <= end_date:
                values.append(metric['value'])

    return {
        'count': len(values),
        'values': values
    }


def goal_progress(users, metrics, user_id):
    for user in users:
        if user['email'] == user_id:
            return user.get('goals', {})
    return {}


def generate_ascii_chart(values):
    chart = ""

    for value in values:
        chart += "*" * int(value) + "\n"

    return chart
