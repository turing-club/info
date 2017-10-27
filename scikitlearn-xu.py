import os
import numpy as np
import pandas as pd
HOUSING_PATH = "C:\\Users\\lenovo\\Downloads\\housing\\"
def load_housing_data(housing_path=HOUSING_PATH):
   csv_path = os.path.join(housing_path, "housing.csv")
   return pd.read_csv(csv_path)

housing = load_housing_data()
housing.head()
housing.info()
import matplotlib.pyplot as plt
housing.hist(bins=50,figsize=(20,15))
plt.show()
from sklearn.model_selection import train_test_split
train_set,test_set=train_test_split(housing,test_size=0.2,random_state=42)
corr_matrix=housing.corr()
corr_matrix['median_house_value'].sort_values(ascending=False)
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["median_house_value"]): 
 strat_train_set = housing.loc[train_index] 
 strat_test_set = housing.loc[test_index]
housing=strat_train_set.drop("median_house_value",axis=1)
housing_labels=strat_train_set["median_house_value"].copy()
from sklearn.preprocessing import Imputer
imputer=Imputer(strategy='median')
housing_num=housing.drop('ocean_proximity',axis=1)
imputer.fit(housing_num)
X=imputer.trasnform(housing_num)
housing_cat=housing['ocean_proximity']
from sklearn.preprocessing import CategoricalEncoder # or get from notebook
cat_encoder = CategoricalEncoder()
housing_cat_reshaped = housing_cat.values.reshape(-1, 1)
housing_cat_1hot = cat_encoder.fit_transform(housing_cat_reshaped)
housing_cat_1hot
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.pipeline import FeatureUnion
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
   def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
       self.add_bedrooms_per_room = add_bedrooms_per_room
   def fit(self, X, y=None):
       return self  # nothing else to do
   def transform(self, X, y=None):
       rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
       population_per_household = X[:, population_ix] / X[:, household_ix]
       if self.add_bedrooms_per_room:
           bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
           return np.c_[X, rooms_per_household, population_per_household,
                        bedrooms_per_room]
       else:
           return np.c_[X, rooms_per_household, population_per_household]

num_pipeline = Pipeline([
       ('selector', DataFrameSelector(num_attribs)),
       ('imputer', Imputer(strategy="median")),
       ('attribs_adder', CombinedAttributesAdder()),
       ('std_scaler', StandardScaler()),
   ])

cat_pipeline = Pipeline([
       ('selector', DataFrameSelector(cat_attribs)),
       ('cat_encoder', CategoricalEncoder(encoding="onehot-dense")),
   ])


full_pipeline = FeatureUnion(transformer_list=[
       ("num_pipeline", num_pipeline),
       ("cat_pipeline", cat_pipeline),
   ])
    


rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6

attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_adder.transform(housing.values)

housing_prepared = full_pipeline.fit_transform(housing)
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)

from sklearn.metrics import mean_squared_error
housing_predictions = lin_reg.predict(housing_prepared)
lin_mse = mean_squared_error(housing_labels, housing_predictions)
lin_rmse = np.sqrt(lin_mse)
lin_rmse

from sklearn.model_selection import cross_val_score
scores = cross_val_score(lin_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)

lig_rmse_scores = np.sqrt(-scores)

def display_scores(scores):
      print("Scores:", scores)
      print("Mean:", scores.mean())
      print("Standard deviation:", scores.std())

display_scores(lig_rmse_scores)
