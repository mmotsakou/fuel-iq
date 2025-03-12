# 🎈FueliQ App and Fuel-efficiency Classification Project

This is a project for the We Lead Data Science and Business Insights Bootcamp! The FueliQ app & model was build by Alexandra Vasileiadou, Ioanna Delemissi, Eleni Kakouri, Margarita Meletlidou & Maria Motsakou

## To Run the FueliQ APP: 
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine
1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```
2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
## FuelIQ Classification Model development 
### Dataset
The dataset contains various attributes related to vehicle specifications, such as:

mpg: Miles per gallon (target variable for classification)
cylinders: Number of engine cylinders
displacement: Engine displacement (in cubic inches)
horsepower: Engine horsepower
weight: Vehicle weight (in lbs)
acceleration: Time taken to accelerate from 0 to 60 mph (in seconds)
model year: The year the vehicle was manufactured
origin: Region of origin (categorical variable)
car name: The name of the vehicle



### Preprocessing Steps

1. Loading the Dataset
The dataset is read from a CSV file (mpg.data.csv) and loaded into a pandas DataFrame. The initial exploration includes checking for missing values, inspecting column names, and dropping irrelevant columns.

2. Dropping Unnecessary Columns
Several unnamed columns were dropped from the dataset (Unnamed: 9, Unnamed: 10, Unnamed: 11, Unnamed: 12) as they provided no useful information.

3. Handling Missing Data
mpg and horsepower columns had missing values.
Missing values in mpg and horsepower were either removed or imputed respectively based on their overall impact on the dataset. Imputation technique involves using mean values.

4. Feature Engineering
The origin column was transformed into categorical data, representing different regions.
The mpg column (which is continuous) was transformed into four fuel efficiency classes:
A/B/C/D in equal percentile pins

5. Normalization
Continuous features like weight, displacement, and horsepower were normalized to ensure that they are on a similar scale, improving model performance during training.

6. Outlier Detection and Removal 
Outliers in continuous variables like mpg, displacement, weight, and acceleration were identified using statistical method of Z-scores.
Outliers that could negatively impact the model's performance were removed to ensure the data distribution is more consistent and representative of typical vehicle behavior.

7. Data Transformation
All categorical variables were one-hot encoded to make them compatible with machine learning models.

8. Final Cleaned Dataset
The dataset is now ready for use in model training, with all missing values handled, features engineered, and irrelevant columns removed. The dataset will be saved under 'processed_mpg_data.csv'



## Evaluation of Random Forest

### Overview
After completing the preprocessing, we used the refined dataset to train 4 different models for mpg predictions.

### Models Evaluated
- K-Nearest Neighbors (KNN)
- Support Vector Classifier (SVC)
- Logistic Regression
- Random Forest

### Additionally, Voting Classifiers have been implemented, combining the basic algorithms with Random Forest to improve accuracy.

### Evaluation Summary
- Best Model: Random Forest delivered the best performance.
- Hyperparameters:  
  - max_depth = 8  
  - n_estimators = 200
- Tuning Result: Achieved the highest score of 0.784 during hyperparameter tuning.
- Observation: Increasing `n_estimators` from 50 to 200 improved overall performance.

### Overall Model Performance Validation
- Accuracy: 0.875
- Precision: 0.883
- Recall: 0.874
- Latency: 24.2ms delay


# Usage
To run the preprocessing script and get the cleaned dataset:
1. Clone the repository:
<git clone https://github.com/mmotsakou/fuel-iq.git> 

2. Navigate to the project directory:
cd fuel-iq

3. Install the required dependencies:
pip install -r requirements.txt

4. Run the EDA, preprocessing and Model notebooks:
jupyter notebook EDA.ipynb
jupyter notebook Preprocessing.ipynb
jupyter notebook KNN.ipynb
jupyter notebook RF.ipynb
jupyter notebook Logistic_regression.ipynb
jupyter notebook SVC.ipynb




