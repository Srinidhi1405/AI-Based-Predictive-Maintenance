# AI-Based Predictive Maintenance using Vibration Analysis

## Overview

Industrial machines rarely fail without warning. As machine components such as bearings begin to wear out, their vibration patterns change. This project aims to detect these changes by analyzing vibration signals and using machine learning to identify faults before they lead to unexpected machine failures.

Since an industrial motor setup was not available during the initial development phase, this project uses the **Case Western Reserve University (CWRU) Bearing Dataset**, a benchmark dataset widely used for bearing fault diagnosis. The final objective is to deploy the trained machine learning model on a Raspberry Pi with an MPU6050 vibration sensor for real-time predictive maintenance.

---

## Objectives

- Analyze vibration signals from healthy and faulty bearings.
- Extract meaningful statistical and frequency-domain features.
- Train a machine learning model to classify bearing faults.
- Deploy the trained model on Raspberry Pi for real-time monitoring.

---

## Features

- MATLAB (.mat) dataset loading
- Time-domain vibration signal visualization
- Statistical feature extraction
- RMS comparison of bearing conditions
- Frequency-domain analysis using FFT *(In Progress)*
- Machine Learning-based fault classification *(Planned)*
- Raspberry Pi deployment *(Planned)*

---

## Technologies Used

- Python
- NumPy
- SciPy
- Pandas
- Matplotlib
- Scikit-learn
- Raspberry Pi 4
- MPU6050 Accelerometer

---

## Dataset

This project uses the **Case Western Reserve University (CWRU) Bearing Dataset**, one of the most widely used benchmark datasets for bearing fault diagnosis.

**Bearing Conditions**
- Healthy
- Ball Fault
- Inner Race Fault
- Outer Race Fault

---

## Project Workflow

```text
CWRU Bearing Dataset
          │
          ▼
Load MATLAB Files
          │
          ▼
Signal Visualization
          │
          ▼
Statistical Feature Extraction
          │
          ▼
Frequency Analysis (FFT)
          │
          ▼
Machine Learning Model
          │
          ▼
Fault Classification
          │
          ▼
Deployment on Raspberry Pi
```

## Statistical Features Extracted

- Mean
- Standard Deviation
- Root Mean Square (RMS)
- Peak Value
- Kurtosis

These features help distinguish healthy bearings from faulty ones and serve as inputs for the machine learning model.

---

## Future Enhancements

- Real-time vibration acquisition using MPU6050
- Edge AI deployment on Raspberry Pi
- Industrial monitoring dashboard
- IoT-based predictive maintenance system
- Cloud-based fault monitoring and alerts

---
