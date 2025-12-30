# 🧠 Stroke Prediction Using Machine Learning
This **GitHub repository** serves as a digital storage space for a **machine learning** capstone project focused on **stroke prediction** using Binary Classification. Created for the **DataTalks ML Zoomcamp** course, the collection includes a **healthcare dataset** alongside the necessary **Python code** and **Jupyter notebooks** to train a predictive model. The technical setup is supported by files for **containerisation** via Docker and **cloud deployment** using AWS Lambda functions and API Gateway. Users can access specific scripts for **model training**, dependency management files, and the final **binary model** file. Overall, the source highlights a practical application of **Machine Learning** aimed at identifying medical risks.

## 🚨 Problem Statement

Stroke is one of the **leading causes of death and long-term disability worldwide**. It occurs when the blood supply to part of the brain is interrupted or reduced, depriving brain tissue of oxygen and nutrients. Many risk factors—such as hypertension, heart disease, high glucose levels, and lifestyle choices—develop silently over time, making early detection difficult.

**Machine Learning (ML)** enables early identification of high-risk individuals by analyzing complex health data and uncovering hidden patterns. Predicting stroke risk before it occurs can support preventive care, timely intervention, and improved patient outcomes.

## 🚀 Features

- 📊 Data preprocessing and feature engineering  
- 🤖 Machine learning model training  
- 💾 Model persistence using serialized artifacts  
- 🧪 Model evaluation  
- 🚢 Docker-based containerization  
- ☁️ AWS Lambda deployment support

## 📓 Jupyter Notebook

For a detailed walkthrough of the project, including **data exploration, preprocessing, model training, and evaluation**, please refer to the Jupyter notebook:

[`stroke-prediction-model.ipynb`](stroke-prediction-model.ipynb)

The notebook provides:

- Exploratory Data Analysis (EDA) with visualizations  
- Feature engineering and preprocessing steps  
- Model selection and evaluation metrics  
- Insights and observations from the dataset  

## 💾 Saving the Model

The trained machine learning model is saved as a binary file using the `train.py` script. This allows the model to be reused for inference without retraining.

### Steps to Save the Model

1. Run the training script:

```bash
python train.py

```

## 🐳 Docker Build & AWS Lambda Deployment

This project includes a `deploy.sh` script to simplify building the Docker image for the Lambda function and deploying it to AWS.

### Build Docker Image

Build the Lambda Docker image locally:

```bash
docker build -t stroke-prediction-lambda .
```

You can test container locally

```bash
docker run -it --rm -p  8080:8080 stroke-prediction-lambda

cd tests
python test_local.py
```

### Deploy image to Lambda Function

Run the deploy.sh script to deploy to aws:

```
chmod +x deploy.sh
./deploy.sh

```
### Test Lamda function exposed via API Gateway 

To test the aws deployment:

```bash

cd tests
python test_aws.py

```

Expected Output:

```bash
{'stroke_probability': 0.14552579820156097, 'stroke prediction': False}

```