
import time
import psutil
import yaml

from datetime import datetime
from pathlib import Path


# File paths
PROJECT_DIR = Path(__file__).parent
CONFIG_PATH = PROJECT_DIR / "config.yaml"
REPORT_PATH = PROJECT_DIR / "server_health_report.txt"


# Load configuration
with open(CONFIG_PATH, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

CPU_LIMIT = config["cpu_limit"]
MEMORY_LIMIT = config["memory_limit"]
DISK_LIMIT = config["disk_limit"]
INTERVAL = config["interval_seconds"]


# Remember previous warning states
previous_warnings = {
    "CPU": False,
    "Memory": False,
    "Disk": False,
}


def check_status(usage, limit):
    if usage >= limit:
        return "WARNING"
    return "Normal"


def monitor_system():
    # Collect actual system metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("C:\\").percent

    metrics = [
        ("CPU", cpu_usage, CPU_LIMIT),
        ("Memory", memory_usage, MEMORY_LIMIT),
        ("Disk", disk_usage, DISK_LIMIT),
    ]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines = [
        f"\n[{timestamp}] SYSTEM HEALTH"
    ]

    for name, usage, limit in metrics:
        status = check_status(usage, limit)

        line = f"{name}: {usage}% - {status}"
        print(line)
        report_lines.append(line)

        is_warning = status == "WARNING"

        # Alert only when entering warning state
        if is_warning and not previous_warnings[name]:
            message = f"ALERT: {name} usage reached {usage}%!"
            print(message)
            report_lines.append(message)

        # Report recovery
        elif not is_warning and previous_warnings[name]:
            message = f"RECOVERED: {name} usage is back to normal."
            print(message)
            report_lines.append(message)

        previous_warnings[name] = is_warning

    report_lines.append("-" * 35)

    # Append readings without deleting older reports
    with open(REPORT_PATH, "a", encoding="utf-8") as file:
        file.write("\n".join(report_lines) + "\n")


print("===== SYSTEM HEALTH MONITOR =====")
print(f"CPU warning limit: {CPU_LIMIT}%")
print(f"Memory warning limit: {MEMORY_LIMIT}%")
print(f"Disk warning limit: {DISK_LIMIT}%")
print(f"Check interval: {INTERVAL} seconds")
print("Press Ctrl+C to stop.\n")


try:
    while True:
        monitor_system()
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
    print(f"Report saved to: {REPORT_PATH}")
