# System Health Monitor

A Dockerized Python system-monitoring application that reports CPU, memory, and disk utilization and classifies resource usage as **Normal**, **Warning**, or **Critical**.

[![System Health Monitor CI](https://github.com/mshrinath12-boop/System-health-monitor/actions/workflows/test.yaml/badge.svg)](https://github.com/mshrinath12-boop/System-health-monitor/actions/workflows/test.yaml)

## Features

- Monitors CPU utilization with `psutil`
- Monitors RAM utilization
- Monitors disk utilization
- Applies configurable warning and critical thresholds
- Prints timestamped health information to the terminal
- Uses a JSON configuration file for thresholds and polling interval
- Runs as a Docker container
- Validates Python syntax and the Docker image in GitHub Actions

## Tech Stack

- Python 3.12
- `psutil`
- Docker
- GitHub Actions
- Git and GitHub

## Repository Structure

```text
.
├── 04_JSON/
│   ├── config.json
│   └── jsonexperiment.py
├── .github/workflows/test.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

The repository also contains Python learning and automation exercises under `01_Basics/`, `02_Functions/`, `03_File_Handling/`, `05_Logging/`, `06_Exception_Handling/`, and `08_Experiments/`.

## Configuration

Resource thresholds and the monitoring interval are defined in [`04_JSON/config.json`](04_JSON/config.json):

```json
{
  "cpu_warning": 80,
  "cpu_critical": 90,
  "ram_warning": 80,
  "ram_critical": 90,
  "disk_warning": 80,
  "disk_critical": 90,
  "interval": 10,
  "log_file": "system.log"
}
```

## Run Locally

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python 04_JSON/jsonexperiment.py
```

Linux/macOS:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
python 04_JSON/jsonexperiment.py
```

The monitor is a continuous process. Stop it with `Ctrl+C`.

## Run with Docker

Build the image:

```bash
docker build -t system-health-monitor .
```

Run the monitor:

```bash
docker run --rm system-health-monitor
```

Stop the continuous monitor with `Ctrl+C`.

## CI Pipeline

The [`System Health Monitor CI`](.github/workflows/test.yaml) workflow runs on pushes to `main` and `master`, and on pull requests. It:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs dependencies
4. Checks Python syntax
5. Builds the Docker image
6. Verifies required files inside the image

## What I Learned

- Collecting system metrics with Python and `psutil`
- Using JSON configuration for threshold-based monitoring
- Writing portable paths with `pathlib`
- Building and validating Docker images
- Automating checks with GitHub Actions
- Working with Git branches, rebases, and merge conflicts

## Future Improvements

- Add automated unit tests
- Improve graceful shutdown and error handling
- Write structured logs and health reports
- Add a CLI for configuration overrides
- Publish the image to a container registry
- Add a tested Kubernetes deployment manifest
