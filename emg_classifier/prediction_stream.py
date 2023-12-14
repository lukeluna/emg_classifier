from pylsl import StreamOutlet, StreamInfo


class PredictionStream:
    def __init__(self):
        info = StreamInfo('PredictionStream', 'Markers', 1, 0, 'float32', 'DrivingAnalyticsStream')
        self.stream = StreamOutlet(info)

    def send_prediction(self, prediction: float):
        self.stream.push_sample([prediction])

