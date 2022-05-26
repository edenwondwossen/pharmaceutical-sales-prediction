from sklearn.ensemble import RandomForestRegressor
import os
import sys
sys.path.append(os.path.abspath(os.path.join('../scripts')))
from config import Config
from modelling import TrainModel

# create a model
model = RandomForestRegressor(n_jobs=-1, n_estimators=15,
                                verbose=True,
                                max_depth=15,
                                min_samples_split=2,
                                min_samples_leaf=1)

train_model = TrainModel(model, "Random Forest Regressor")

train_model.train_sales()
train_model.train_customers()