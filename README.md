# Python Server Health Monitor

A Python-based system monitoring tool that tracks CPU, memory, and disk usage, detects high resource utilization, and records monitoring results in a log file.

## Features

- **System Monitoring:** Collects actual CPU, memory, and disk usage using `psutil`.
- **Configurable Thresholds:** Loads warning limits and monitoring intervals from a YAML configuration file.
- **Smart Alerts:** Generates alerts when resource usage crosses a threshold and reports when usage returns to normal.
- **Continuous Monitoring:** Checks system health at a configurable interval.
- **Logging:** Saves timestamped monitoring results to a report file.
- **Error-Free Shutdown:** Stops monitoring safely using `Ctrl+C`.

## Technologies Used

- Python
- psutil
- PyYAML
- YAML
- PowerShell / Windows

## Project Structure

```text
python-server-health-monitor/
├── server_health.py
├── config.yaml
└── README.md
```

The monitoring report, `server_health_report.txt`, is generated automatically when the program runs.

## Configuration

The `config.yaml` file contains the monitoring thresholds and interval.

```yaml
cpu_limit: 80
memory_limit: 80
disk_limit: 80
interval_seconds: 5
```

You can modify these values without changing the Python monitoring logic.

## Installation and Usage

### 1. Install Python dependencies

```bash
python -m pip install psutil pyyaml
```

### 2. Run the monitor

Make sure `server_health.py` and `config.yaml` are in the same folder, then run:

```bash
python server_health.py
```

### 3. Stop monitoring

Press `Ctrl+C` in the terminal.

## Sample Output

```text
CPU: 13.8% - Normal
Memory: 82.8% - WARNING
ALERT: Memory usage reached 82.8%!
Disk: 62.5% - Normal
```

*Actual readings vary depending on system usage.*

## Learning Outcomes

This project helped me practise Python automation, system resource monitoring, configuration management with YAML, threshold-based alerts, and timestamped logging.

## Future Improvements

- Linux system monitoring
- Remote server monitoring
- Email or other notification integrations
- Dashboard for visualizing system metrics

---

**Status:** Personal learning project in development.
