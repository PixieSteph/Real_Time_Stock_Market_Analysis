# Stock Market Data Pipeline

This project is a stock market data pipeline built with Python. It connects to a stock market API, extracts stock data, streams the data through Kafka, processes it with Spark, stores it in PostgreSQL, and prepares it for visualization in Power BI.

The project was built to practice core data engineering concepts such as API integration, containerization, distributed processing, and database storage.

---

## Project Architecture

The diagram below shows the overall data pipeline architecture used in this project.

![Stock Market Pipeline Architecture](Real-Time%20Stock%20Market%20Insights_Data%20Pipeline.png)

---

## Project Overview

The purpose of this project is to practice building a modern data engineering pipeline from start to finish.

The pipeline follows these steps:

1. Connect to the stock market API using Python
2. Extract stock market data
3. Stream the data through Kafka
4. Process the data using Spark
5. Store the data in PostgreSQL
6. Prepare the data for reporting and visualization in Power BI
7. Run all services using Docker Compose

---

## Technologies Used

- Python
- Apache Kafka
- Apache Spark
- PostgreSQL
- Docker
- Docker Compose
- Power BI
- Requests Library
- GitHub
- VS Code
- Windows

---

## Project Structure

```bash
stock-market-data-pipeline/
│
├── data/
│   └── raw/
│
├── config.py
├── extract.py
├── main.py
│
├── Dockerfile
├── compose.yml
├── requirements.txt
├── README.md
├── .gitignore
│
└── Real-Time Stock Market Insights_Data Pipeline.png
```

---

## Step 1: Open the Project Folder

I opened my existing project folder in VS Code.

```bash
cd stock-market-data-pipeline
```

---

## Step 2: Confirm GitHub Connection

Since my folder was already connected to GitHub, I confirmed the remote connection using:

```bash
git remote -v
```

---

## Step 3: Create a Virtual Environment

I created a virtual environment for the project using:

```bash
python -m venv venv
```

---

## Step 4: Activate the Virtual Environment

I activated the virtual environment on Windows using:

```bash
venv\Scripts\activate
```

---

## Step 5: Create the Requirements File

I created a `requirements.txt` file and added the required packages.

```txt
requests
python-dotenv
```

---

## Step 6: Install Required Packages

I installed the required Python packages using:

```bash
pip install -r requirements.txt
```

---

## Step 7: Create the Environment File

I created a `.env` file in the project folder to store my API key.

```env
API_KEY=your_api_key_here
```

The `.env` file is not pushed to GitHub because it contains private information.

---

## Step 8: Configure the Project

The `config.py` file stores the project configuration and stock symbols used for API requests.

Example:

```python
stocks = ["TSLA", "MSFT", "GOOGL"]
```

---

## Step 9: Run the Extraction Script

I ran the extraction script from the terminal.

```bash
python extract.py
```

The script connects to the stock market API and retrieves stock market data.

---

## Step 10: Run the Main File

I used the `main.py` file to run the overall project workflow.

```bash
python main.py
```

---

## Step 11: Create the Docker Compose File

I created a `compose.yml` file to run all project services together.

The services include:

- Python application
- Kafka
- Spark
- PostgreSQL

---

## Step 12: Run Docker Compose

To start all services:

```bash
docker compose up
```

To stop all services:

```bash
docker compose down
```

---

## Docker Services

### Python Application

Runs the stock market extraction pipeline.

### Apache Kafka

Streams stock market data between services.

### Apache Spark

Processes and handles distributed data workloads.

### PostgreSQL

Stores the stock market data for analysis and reporting.

---

## Features

- API data extraction using Python
- Distributed streaming with Kafka
- Data processing using Spark
- PostgreSQL database integration
- Docker containerization
- Power BI reporting workflow
- Beginner-friendly data engineering project structure

---

## Troubleshooting

### Docker Not Found Error

If Docker commands are not recognized:

1. Install Docker Desktop
2. Restart the computer
3. Open Docker Desktop
4. Wait for the Docker engine to start

Verify installation using:

```bash
docker --version
```

---

## Future Improvements

In the future, I would like to improve this project by:

- Adding real-time streaming
- Automating workflows with Apache Airflow
- Deploying the project to the cloud
- Adding better logging and monitoring
- Expanding Power BI dashboards

---

## Author

### Igho Ogbobine

Data Engineering Project