import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
   if not os.path.isdir(housing_path):
       os.makedirs(housing_path)
   tgz_path = os.path.join(housing_path, "housing.tgz")
   urllib.request.urlretrieve(housing_url, tgz_path)
   housing_tgz = tarfile.open(tgz_path)
   housing_tgz.extractall(path=housing_path)
   housing_tgz.close()
import pandas as pd

def load_housing_data(housing_path=HOUSING_PATH):
   csv_path = os.path.join(housing_path, "housing.csv")
   return pd.read_csv(csv_path)

housing = load_housing_data()

housing.head()   
housing.info()

%matplotlib inline   # only in a Jupyter notebook
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))
plt.show()

from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

corr_matrix = housing.corr()
corr_matrix[“median_house_value”].sort_values(ascending=False)

housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()

rom sklearn.preprocessing import Imputer

imputer = Imputer(strategy="median")

housing_num = housing.drop("ocean_proximity", axis=1)
imputer.fit(housing_num)

X = imputer.transform(housing_num)

housing_cat = housing["ocean_proximity"]
from sklearn.preprocessing import CategoricalEncoder # or get from notebook
	cat_encoder = CategoricalEncoder()
housing_cat_reshaped = housing_cat.values.reshape(-1, 1)
	housing_cat_1hot = cat_encoder.fit_transform(housing_cat_reshaped)
	housing_cat_1hot

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]

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

from sklearn.pipeline import FeatureUnion

full_pipeline = FeatureUnion(transformer_list=[
       ("num_pipeline", num_pipeline),
       ("cat_pipeline", cat_pipeline),
   ])

from sklearn.base import BaseEstimator, TransformerMixin

rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
   def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
       self.add_bedrooms_per_room = add_bedrooms_per_room
   def fit(self, X, y=None):
       return self  # nothing else to do
   def transform(self, X, y=None):
       rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
       population_per_household = X[:, population_ix] / X[:, household_ix]
       if self.add_bedrooms_per_room:
           bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
           return np.c_[X, rooms_per_household, population_per_household,
                        bedrooms_per_room]
       else:
           return np.c_[X, rooms_per_household, population_per_household]

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

lig_mnse_scores = np.sqrt(-scores)

def display_scores(scores):
      print("Scores:", scores)
      print("Mean:", scores.mean())
      print("Standard deviation:", scores.std())

display_scores(tree_rmse_scores)
