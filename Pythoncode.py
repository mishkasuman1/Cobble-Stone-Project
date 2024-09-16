import math
import random
from collections import deque
import matplotlib.pyplot as plt

# Data Stream Simulation Function
def data_stream_simulation(n_points=1000):
    """
    Generator that simulates a data stream with seasonal variation, trend, and noise.
    """
    for i in range(n_points):
        seasonality = 10 * math.sin(i * (2 * math.pi / 50))  # Seasonal component
        trend = i * 0.01  # Gradual increasing trend
        noise = random.gauss(0, 1)  # Gaussian noise
        data_point = seasonality + trend + noise
        yield data_point

# Z-Score based Anomaly Detection
def z_score_anomaly_detection(data_point, window, threshold=3):
    """
    Detects anomalies using Z-Score.
    - window: deque to store the last N data points (sliding window)
    - threshold: Z-Score threshold for anomaly detection
    """
    window.append(data_point)
    
    if len(window) == window.maxlen:  # Check only when the window is full
        mean = sum(window) / len(window)
        std_dev = (sum([(x - mean) ** 2 for x in window]) / len(window)) ** 0.5
        z_score = (data_point - mean) / std_dev if std_dev != 0 else 0
        return abs(z_score) > threshold  # Flag as anomaly if Z-Score exceeds threshold
    return False

# Real-time Plotting
def real_time_plot(data_stream, window_size=50, threshold=3):
    """
    Plots the data stream in real-time and flags anomalies.
    """
    plt.ion()  # Enable interactive mode for real-time plotting
    fig, ax = plt.subplots()
    
    x_data, y_data, anomaly_x, anomaly_y = [], [], [], []
    window = deque(maxlen=window_size)
    
    for i, data_point in enumerate(data_stream):
        x_data.append(i)
        y_data.append(data_point)
        
        # Anomaly detection
        if z_score_anomaly_detection(data_point, window, threshold):
            anomaly_x.append(i)
            anomaly_y.append(data_point)
        
        # Plotting
        ax.clear()
        ax.plot(x_data, y_data, label='Data Stream')
        ax.scatter(anomaly_x, anomaly_y, color='red', label='Anomaly')
        ax.legend()
        plt.pause(0.01)  # Pause for real-time update
    
    plt.ioff()  # Disable interactive mode
    plt.show()

# Main function to run the anomaly detection and visualization
if _name_ == "_main_":
    # Simulate a data stream with 1000 points
    data_stream = data_stream_simulation(1000)
    
    # Run real-time plotting and anomaly detection
    real_time_plot(data_stream, window_size=50, threshold=3)