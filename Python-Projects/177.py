import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

from collections.abc import Sequence
from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shutil
import os
import tensorflow as tf
from sklearn import metrics
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
# Encode text values to indexes(i.e. [1],[2],[3] for red,green,blue).
def encode_text_index(df, name):
    le = preprocessing.LabelEncoder()
    df[name] = le.fit_transform(df[name])
    return le.classes_


dataset = np.array([['Toyota Corolla', 40, 20175],
       ['Ford', 45, 25000],
       ['Dodge', 62, 35782],
       ['Chevrolet', 50, 30000],
       ['Canoo', 57, 34750],
       ['Tesla', 113, 54000],
       ['BMW', 70, 36400]], dtype='<U21')
df = pd.DataFrame(dataset, columns = ['Car','MPG','Cost'])
encode_text_index(df,'Car')

print(df)
# select all rows by : and column 1
# by 1:2 representing features
y = pd.DataFrame(df, columns=['Cost'])
x = pd.DataFrame(df, columns=['MPG'])
print(x)
print(y)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(x, y)

y_pred = regressor.predict([[100]])
print("Predicted price: % d\n"% y_pred)

from six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
import os
os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz\bin'

feature_cols = ['Car','MPG','Cost']
dot_data = StringIO()
export_graphviz(regressor, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')
Image(graph.create_png())