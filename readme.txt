Key Points of the Python Code:

1. Data Stream Simulation - "data_stream_simulation":
Simulates a continuous stream of data with seasonal trends, a slow upward trend and random noice.

2. Z-score Anamoly Detection - "z_score_anomaly_detection":
Uses a sliding window of the last N data points (default being 50) and calculates Z-scores.
Flags points that deviate beyond the threshold (default being 3) as anomalies.

3. Real-Time Visualization - real_time_plot:
Plots the data stream in real-time using "matplotlib" and marks anomalies in red.
The graph is updated dynamically using "plt.pause()" to simulate real-time streaming.

For running the code:

1. Install required libraries (in case not installed):
      pip install matplotlib 

2. Execute the script and we will see a real-time plot with anomalies flagged in red.      