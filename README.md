# Stock Market Data Pipeline

This project is a stock market data pipeline built with Python. It connects to a stock market API, extracts stock data, and saves the results for analysis.

---

## Project Overview

The purpose of this project is to practice building a simple data engineering pipeline from start to finish.

The pipeline follows these steps:

1. Set up the project folder
2. Connect the folder to GitHub
3. Create a Python virtual environment
4. Install the required Python packages
5. Connect to the stock market API
6. Extract stock data
7. Save the data locally
8. Add Docker support for running the project in a container

---

## Tech Stack

- Python
- Requests
- Docker
- Git
- GitHub
- VS Code

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
├── requirements.txt
├── compose.yml
├── README.md
└── .gitignore
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

## Step 5: Install Required Packages

I installed the required Python packages using:

```bash
pip install -r requirements.txt
```

---

## Step 6: Create the Environment File

I created a `.env` file in the project folder to store my API key.

```env
API_KEY=your_api_key_here
```

The `.env` file is not pushed to GitHub because it contains private information.

---

## Step 7: Configure the Project

The `config.py` file stores the project configuration and stock symbols used for the API requests.

Example:

```python
stocks = ["TSLA", "MSFT", "GOOGL"]
```

---

## Step 8: Run the Extraction Script

I ran the extraction script from the terminal.

```bash
python extract.py
```

The script connects to the stock market API and retrieves stock market data.

---

## Step 9: Run the Main File

I used the `main.py` file to run the overall project workflow.

```bash
python main.py
```

---

## Step 10: Save the Data

The extracted stock data is saved locally inside the `data/raw` folder.

---

## Step 11: Run the Project with Docker

I created Docker files so the project can run in a container.

To build the Docker image:

```bash
docker build -t stock-pipeline .
```

To run the container:

```bash
docker run stock-pipeline
```

---

## Step 12: Run with Docker Compose

I used `compose.yml` to run the project with Docker Compose.

```bash
docker compose -f compose.yml up
```

To stop the container:

```bash
docker compose down
```

---

## Usage Example

The project can collect stock data for selected companies.

Example stock symbols:

```python
stocks = ["TSLA", "MSFT", "GOOGL"]
```

---

## Features

- Automated stock data extraction
- API integration using Python
- Docker container support
- GitHub version control
- Beginner-friendly project structure
- Virtual environment setup

---

## Troubleshooting

### API Premium Endpoint Error

While testing the project, I received a message that some Alpha Vantage endpoints require a premium subscription.

To fix this, I updated the project to use free API endpoints where possible.

---

## Future Improvements

In the future, I would like to improve this project by:

- Adding PostgreSQL for database storage
- Scheduling the pipeline with Apache Airflow
- Creating a Power BI dashboard
- Deploying the project to the cloud
- Adding more error handling and logging

---

## Author

Igho Ogbobine