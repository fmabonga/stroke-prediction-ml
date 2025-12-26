import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
import xgboost as xgb
import pickle 

# Data preparation
df = pd.read_csv('healthcare-dataset-stroke-data.csv')
df.columns = df.columns.str.replace(" ","_").str.lower()
categorical = list(df.dtypes[df.dtypes == 'object'].index)
for c in categorical:
    df[c] = df[c].str.lower().str.replace(' ', '_')

df = df.dropna()
del df['id']

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)


df_test = df_test.reset_index(drop=True)
df_full_train = df_full_train.reset_index(drop=True)

y_full_train = df_full_train.stroke
y_test = df_test.stroke

del df_full_train["stroke"]
del df_test["stroke"]

train_dicts = df_full_train.to_dict(orient='records')
test_dicts = df_test.to_dict(orient='records')

# One hot encoding 
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)
features = list(dv.get_feature_names_out())
X_test = dv.transform(test_dicts)

dtrain = xgb.DMatrix(X_train, label=y_full_train, feature_names=features)
dtest = xgb.DMatrix(X_test, label=y_test, feature_names=features)

#Training Model
dtrain = xgb.DMatrix(X_train, label=y_full_train, feature_names=features)
dtest = xgb.DMatrix(X_test, label=y_test, feature_names=features)

xgb_params = {
    'eta': 0.1, 
    'min_child_weight': 1,
    'max_depth': 2,
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'nthread': 8,
    'gamma':6,
    'min_child_weight': 1,
    'seed': 1,
    'verbosity': 1,
    'max_delta_step': 0,
}

model = xgb.train(xgb_params, dtrain, num_boost_round=100,
                  verbose_eval=5,
                 )
y_pred = model.predict(dtest)
auc_score = roc_auc_score(y_test, y_pred)
print("auc_score %f " % (round(auc_score,2)))

# Save the model
with open('stroke-prediction-model.bin', 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print('model saved to stroke-prediction-model.bin')