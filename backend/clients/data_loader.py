import numpy as np
import pandas as pd
import random

class DataLoader:
    def __init__(self, num_samples=1000, anomaly_rate=0.1):
        self.num_samples = num_samples
        self.anomaly_rate = anomaly_rate

    def generate_data(self):
        # Simulate normal data
        normal_data = np.random.normal(loc=0.0, scale=1.0, size=(self.num_samples, 1))
        # Simulate anomalies
        num_anomalies = int(self.num_samples * self.anomaly_rate)
        anomalies = np.random.normal(loc=5.0, scale=1.0, size=(num_anomalies, 1))
        # Combine normal data and anomalies
        dataset = np.vstack((normal_data, anomalies))
        return pd.DataFrame(dataset, columns=['powerline_reading'])

    def save_to_csv(self, file_path='powerline_data.csv'):
        data = self.generate_data()
        data.to_csv(file_path, index=False)
        print(f'Dataset saved to {file_path}')