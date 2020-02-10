from datetime import datetime


class PrometheusAlert:
    def __init__(self, alert):
        self.alert = alert

    def plain(self):
        alerts = []
        for i, alert in enumerate(self.alert['alerts']):
            alert_name = alert['labels']['alertname']
            alert_time = str(datetime.strptime(alert['startsAt'][:-4], "%Y-%m-%dT%H:%M:%S.%f"))[0:19]
            alert_high = alert['labels']['severity'].upper()
            alert_inst = alert['labels']['instance']
            alert_desc = alert['annotations']['title']
            msg = "[{}] {} at {} on {} {}".format(alert_high, alert_name, alert_time, alert_inst, alert_desc)
            alerts.append(msg)
        return '\n'.join(alerts)
