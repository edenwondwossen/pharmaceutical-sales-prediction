import mlflow
import pandas as pd
import numpy as np
import datetime
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from file_handler import FileHandler

class TrainModel():
    '''
    Class for training a model using sklearn pipeline
    '''

    def __init__(self, model, name):
        self.model = model
        self.name = name
        self.file_handler = FileHandler()

    def scaler(self):
        scaler = StandardScaler()
        return scaler

    def train(self, X, y, model_type):
        mlflow.set_experiment(self.name)
        mlflow.sklearn.autolog()
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
        
        train_pipe = Pipeline(
                    [('Scaling', self.scaler()),
                    (self.name, self.model)])

        pipe = train_pipe.fit(X_train, y_train.values.ravel())
        self.file_handler.save_model(pipe.steps[1][1], str(self.name + "_" + model_type))
        print(pipe.score(X_test, y_test)) 

    
    def calculate_metrics(y_test, y_preds):
        rmse = np.sqrt(mean_squared_error(y_test, y_preds))
        r_sq = r2_score(y_test, y_preds)
        mae = mean_absolute_error(y_test, y_preds)

        return {'RMSE Score': rmse, 'R2_Squared': r_sq, 'MAE Score': mae} 

    def train_sales(self):
        X = pd.read_csv('../data/features/train_features.csv')
        y = pd.read_csv('../data/features/target_sales.csv')
        model = self.train(X, y, 'Sales')

        #train_score = model.score(X_train, y_train)
        #test_score = model.score(X_test, y_test)
        #test_metrics = calculate_metrics(y_test, rf.predict(X_test))

    def train_customers(self):
        X = pd.read_csv('../data/features/train_features.csv')
        y = pd.read_csv('../data/features/target_customers.csv')
        self.train(X, y, 'Customers')