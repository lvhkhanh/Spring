---
name: ai
description: '**WORKFLOW SKILL** — Create, train, deploy, and optimize AI/ML models and applications. USE FOR: machine learning model development, data preprocessing, model training and evaluation, AI application deployment, computer vision and NLP tasks, MLOps workflows. DO NOT USE FOR: general programming, web development, or non-AI data processing. INVOKES: file system tools for model creation/modification, terminal for training commands, semantic search for AI pattern discovery.'
---

# AI/ML Development Skill

## Overview

This skill provides comprehensive support for artificial intelligence and machine learning development, from data preparation through model deployment. It covers traditional ML, deep learning, computer vision, natural language processing, and MLOps practices.

## Key Capabilities

### Data Processing & Preparation
- Load and preprocess datasets (CSV, JSON, images, text)
- Handle missing data, outliers, and feature engineering
- Create data pipelines with scikit-learn, pandas, and custom transformers
- Implement data validation and quality checks

### Model Development
- Build ML models with scikit-learn, TensorFlow, PyTorch
- Design neural networks for classification, regression, and generation
- Implement computer vision models (CNNs, object detection, segmentation)
- Create NLP models (transformers, RNNs, embeddings)

### Training & Optimization
- Configure training loops with proper loss functions and optimizers
- Implement cross-validation and hyperparameter tuning
- Apply regularization techniques (dropout, batch norm, early stopping)
- Handle distributed training and GPU acceleration

### Model Evaluation & Deployment
- Calculate metrics (accuracy, precision, recall, F1, AUC-ROC)
- Create confusion matrices and performance visualizations
- Deploy models to production (Flask/FastAPI APIs, cloud services)
- Implement model monitoring and A/B testing

### MLOps & Production
- Version control for datasets and models (DVC, MLflow)
- Create CI/CD pipelines for ML workflows
- Implement model serving and inference optimization
- Set up monitoring, logging, and automated retraining

## Usage Examples

### Computer Vision Classification
```
Create a CNN model to classify images of cats and dogs using transfer learning with ResNet50.
```

### NLP Text Classification
```
Build a sentiment analysis model using BERT transformers to classify movie reviews as positive or negative.
```

### Time Series Forecasting
```
Develop an LSTM model to predict stock prices using historical market data with proper train/validation splits.
```

## Common Patterns

### Data Pipeline Setup
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load and split data
df = pd.read_csv('data.csv')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Model Training Loop
```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

model = MyModel()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())

for epoch in range(num_epochs):
    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
```

### Model Evaluation
```python
from sklearn.metrics import classification_report, confusion_matrix

predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
```

## Best Practices

### Data Management
- Always split data into train/validation/test sets before training
- Use stratified sampling for imbalanced datasets
- Implement proper data versioning and lineage tracking
- Validate data quality and handle edge cases

### Model Development
- Start with simple models (baseline) before complex architectures
- Use cross-validation to prevent overfitting
- Implement proper regularization and early stopping
- Document model assumptions and limitations

### Production Deployment
- Containerize models with Docker for consistent environments
- Implement proper error handling and fallback mechanisms
- Monitor model performance and data drift in production
- Use model versioning for rollback capabilities

### Performance Optimization
- Profile code to identify bottlenecks
- Use appropriate data structures and algorithms
- Implement batch processing for large datasets
- Consider distributed computing for scale

## Troubleshooting

### Common Training Issues
- **Overfitting**: Add regularization, increase dataset size, use data augmentation
- **Underfitting**: Increase model complexity, train longer, add features
- **Vanishing gradients**: Use better activation functions (ReLU), batch normalization
- **Mode collapse (GANs)**: Improve discriminator, use different architectures

### Data Problems
- **Imbalanced classes**: Use class weights, oversampling, or SMOTE
- **Missing values**: Impute with mean/median, or use algorithms that handle missing data
- **Outliers**: Remove, transform, or use robust algorithms
- **Feature scaling**: Always scale features for gradient-based algorithms

### Performance Issues
- **Slow training**: Use GPU acceleration, optimize batch size, reduce model complexity
- **Memory errors**: Reduce batch size, use gradient accumulation, implement model parallelism
- **Poor accuracy**: Check data quality, tune hyperparameters, try different architectures

### Deployment Challenges
- **Model serialization**: Use joblib/pickle for sklearn, save/load for deep learning frameworks
- **API latency**: Optimize model size, use quantization, implement caching
- **Scalability**: Use load balancing, implement async processing, consider serverless

## Integration Points

### Cloud Platforms
- **AWS**: SageMaker for training, Lambda for inference, S3 for data storage
- **Google Cloud**: AI Platform, Vertex AI, BigQuery ML
- **Azure**: Machine Learning Studio, Cognitive Services

### Development Tools
- **Jupyter**: Interactive development and experimentation
- **MLflow**: Experiment tracking and model registry
- **Weights & Biases**: Training monitoring and visualization
- **DVC**: Data and model versioning

### Frameworks & Libraries
- **Deep Learning**: TensorFlow, PyTorch, Keras
- **Traditional ML**: scikit-learn, XGBoost, LightGBM
- **Computer Vision**: OpenCV, Pillow, torchvision
- **NLP**: Hugging Face Transformers, spaCy, NLTK

### Data Sources
- **Databases**: PostgreSQL, MongoDB, Redis
- **Data Lakes**: S3, GCS, Azure Blob Storage
- **Streaming**: Kafka, Kinesis, Pub/Sub
- **APIs**: REST APIs, GraphQL, WebSocket