# 🛡️ FraudShield - Bank Fraud Detection System

FraudShield is an AI-powered bank fraud detection system that identifies suspicious financial transactions in real time using Machine Learning.

Built using XGBoost, FastAPI, Streamlit, Docker, and Render.

- Check App: https://fraudshield-app-saq5.onrender.com/
- Check API: https://fraudshield-api-4op5.onrender.com/
- Check DockerHUB Repositoty: https://hub.docker.com/repositories/ashish7733,
docker pull ashish7733/fraudshield-ui:latest, docker pull ashish7733/fraudshield-api:latest

---

## Features

* Real-time fraud prediction
* Interactive Streamlit APP
* FastAPI backend integration
* Fraud probability score
* Risk level classification
* Dockerized application
* Cloud deployment using Render

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* FastAPI
* Streamlit
* Docker
* Docker Hub
* Render

---

## Project Structure

```text
FraudShield-Bank-Fraud-Detection_System/
│
├── app.py
├── api.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── artifacts/
├── experiments/
├── notes/
├── plots/
├── schema/
└── src/
```

---

## Workflow

```text
Transaction Details
        |
Feature Engineering
        |
Data Preprocessing
        |
XGBoost Model
        |
Fraud Probability
        |
Risk Classification
        |
Prediction Result
```

---

## Run Application

```bash
docker compose up -d
```

Or

```bash
streamlit run app.py
```

---

## Future Improvements

* Add transaction history dashboard
* Add user authentication
* Add monitoring and logging
* Integrate MLflow
* Add CI/CD pipeline
* Deploy on AWS

```
```
