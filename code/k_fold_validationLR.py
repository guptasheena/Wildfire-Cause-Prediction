import pandas as pd
from LogisticRegression import LRModel
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score,confusion_matrix,accuracy_score
import sys
sys.path.append("../")
from preprocessing_scripts.labels import labels

train_df = pd.read_csv('../data/train.csv',usecols = ['STAT_CAUSE_DESCR','LATITUDE','LONGITUDE','DISCOVERY_DATE','FIRE_SIZE'])
y = pd.DataFrame()
y['STAT_CAUSE_DESCR']=train_df['STAT_CAUSE_DESCR']
y=labels.createLabel(y)
y=y['STAT_CAUSE_DESCR'].astype(int)
train_df = train_df.drop(columns=['STAT_CAUSE_DESCR'])



#K-fold validation
kf = KFold(n_splits=10)
for train_index, test_index in kf.split(train_df):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = train_df.iloc[train_index].reset_index(drop=True), train_df.iloc[test_index].reset_index(drop=True)
    y_train, y_test = y[train_index], y[test_index]
    model_val = LRModel()
    model_val.trainModel(X_train,y_train)
    y_pred = model_val.predict(X_test)
    print("F1-score: %f"%(f1_score(y_test,y_pred,average='macro')))
    print("Accuracy: %f"%(accuracy_score(y_test,y_pred)))