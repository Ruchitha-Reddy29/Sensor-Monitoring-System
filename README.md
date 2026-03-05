# Sensor-Monitoring-System
Project Overview
This project implements an automated real-time sensor monitoring system that continuously analyzes sensor data and sends alerts when safety thresholds are exceeded.
The system simulates sensor data using a Python-based sensor generator, stores the data in a CSV file, and uses n8n automation workflows to monitor the data and trigger alerts.
This approach reduces the need for manual monitoring and enables automatic detection of abnormal conditions in testing environments.
| Technology                         | Purpose                            |
| ---------------------------------- | ---------------------------------- |
| Python                             | Sensor data simulation             |
| n8n                                | Workflow automation and monitoring |
| CSV                                | Data storage for sensor readings   |
| SMTP / Email                       | Alert notifications                |
| JavaScript Logic (n8n IF node)     | Threshold validation               |

🚨 Alert System
When a sensor value exceeds predefined thresholds, the system automatically sends an alert email.
