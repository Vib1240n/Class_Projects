# %% [markdown]
# # Module 4: Data Preprocessing
# 
# The following tutorial contains Python examples for data preprocessing. You should refer to the "Data" chapter of the "Introduction to Data Mining" book (slides are available at https://www-users.cs.umn.edu/~kumar001/dmbook/index.php) to understand some of the concepts introduced in this tutorial. 
# Data preprocessing consists of a broad set of techniques for cleaning, selecting, and transforming data to improve data mining analysis. Read the step-by-step instructions below carefully. To execute the code, click on the corresponding cell and press the SHIFT-ENTER keys simultaneously.

# %% [markdown]
# ## Data Quality Issues
# 
# Poor data quality can have an adverse effect on data mining. Among the common data quality issues include noise, outliers, missing values, and duplicate data. This section presents examples of Python code to alleviate some of these data quality problems. We begin with an example dataset from the UCI machine learning repository containing information about breast cancer patients. We will first download the dataset using Pandas read_csv() function and display its first 5 data points.
# 
# **<font color="red">Code:</font>**

# %%
import pandas as pd
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data', header=None)
data.columns = ['Sample code', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                'Normal Nucleoli', 'Mitoses','Class']

data = data.drop(['Sample code'],axis=1)
print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))
data.head()

# %% [markdown]
# ### Missing Values
# 
# It is not unusual for an object to be missing one or more attribute values. In some cases, the information was not collected; while in other cases, some attributes are inapplicable to the data instances. This section presents examples on the different approaches for handling missing values. 
# 
# According to the description of the data (https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(original), the missing values are encoded as '?' in the original data. Our first task is to convert the missing values to NaNs. We can then count the number of missing values in each column of the data.
# 
# **<font color="red">Code:</font>**

# %%
import numpy as np

data = data.replace('?',np.NaN)

print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))

print('Number of missing values:')
for col in data.columns:
    print('\t%s: %d' % (col,data[col].isna().sum()))

# %% [markdown]
# Observe that only the 'Bare Nuclei' column contains missing values. In the following example, the missing values in the 'Bare Nuclei' column are replaced by the median value of that column. The values before and after replacement are shown for a subset of the data points.
# 
# **<font color="red">Code:</font>**

# %%
data2 = data['Bare Nuclei']

print('Before replacing missing values:')
print(data2[20:25])
data2 = data2.fillna(data2.median())

print('\nAfter replacing missing values:')
print(data2[20:25])

# %% [markdown]
# Instead of replacing the missing values, another common approach is to discard the data points that contain missing values. This can be easily accomplished by applying the dropna() function to the data frame.
# 
# **<font color="red">Code:</font>**

# %%
print('Number of rows in original data = %d' % (data.shape[0]))

data2 = data.dropna()
print('Number of rows after discarding missing values = %d' % (data2.shape[0]))

# %% [markdown]
# ### Outliers
# 
# Outliers are data instances with characteristics that are considerably different from the rest of the dataset. In the example code below, we will draw a boxplot to identify the columns in the table that contain outliers. Note that the values in all columns (except for 'Bare Nuclei') are originally stored as 'int64' whereas the values in the 'Bare Nuclei' column are stored as string objects (since the column initially contains strings such as '?' for representing missing values). Thus, we must  convert the column into numeric values first before creating the boxplot. Otherwise, the column will not be displayed when drawing the boxplot.
# 
# **<font color="red">Code:</font>**

# %%
matplotlib inline

data2 = data.drop(['Class'],axis=1)
data2['Bare Nuclei'] = pd.to_numeric(data2['Bare Nuclei'])
data2.boxplot(figsize=(20,3))

# %% [markdown]
# The boxplots suggest that only 5 of the columns (Marginal Adhesion, Single Epithetial Cell Size, Bland Cromatin, Normal Nucleoli, and Mitoses) contain abnormally high values. To discard the outliers, we can compute the Z-score for each attribute and remove those instances containing attributes with abnormally high or low Z-score (e.g., if Z > 3 or Z <= -3). 
# 
# **<font color="red">Code:</font>**
# 
# The following code shows the results of standardizing the columns of the data. Note that missing values (NaN) are not affected by the standardization process.

# %%
Z = (data2-data2.mean())/data2.std()
Z[20:25]

# %% [markdown]
# **<font color="red">Code:</font>**
# 
# The following code shows the results of discarding columns with Z > 3 or Z <= -3.

# %%
print('Number of rows before discarding outliers = %d' % (Z.shape[0]))

Z2 = Z.loc[((Z > -3).sum(axis=1)==9) & ((Z <= 3).sum(axis=1)==9),:]
print('Number of rows after discarding missing values = %d' % (Z2.shape[0]))

# %% [markdown]
# ### Duplicate Data
# 
# Some datasets, especially those obtained by merging multiple data sources, may contain duplicates or near duplicate instances. The term deduplication is often used to refer to the process of dealing with duplicate data issues. 
# 
# **<font color="red">Code:</font>**
# 
# In the following example, we first check for duplicate instances in the breast cancer dataset.

# %%
dups = data.duplicated()
print('Number of duplicate rows = %d' % (dups.sum()))
data.loc[[11,28]]

# %% [markdown]
# The duplicated() function will return a Boolean array that indicates whether each row is a duplicate of a previous row in the table. The results suggest there are 236 duplicate rows in the breast cancer dataset. For example, the instance with row index 11 has identical attribute values as the instance with row index 28. Although such duplicate rows may correspond to samples for different individuals, in this hypothetical example, we assume that the duplicates are samples taken from the same individual and illustrate below how to remove the duplicated rows.
# 
# **<font color="red">Code:</font>**

# %%
print('Number of rows before discarding duplicates = %d' % (data.shape[0]))
data2 = data.drop_duplicates()
print('Number of rows after discarding duplicates = %d' % (data2.shape[0]))

# %% [markdown]
# ### Shuffling Dataframes
# It is possible to shuffle.  

# %%
import os
import numpy as np
import pandas as pd

path = "./data/"

filename_read = os.path.join(path,"auto-mpg.csv")
df = pd.read_csv(filename_read, na_values=['NA','?'])

#np.random.seed(30) # Uncomment this line to get the same shuffle each time

df = df.reindex(np.random.permutation(df.index))
df.reset_index(inplace=True, drop=True)
# use inplace=False
df

# %% [markdown]
# ### Sorting Dataframes
# It is possible to sort. 

# %%
df = df.sort_values(by='name',ascending=True)
df

# %%
print("The first car is: {}".format(df['name'].iloc[0]))

# %%
print("The first car is: {}".format(df['name'].loc[0]))


#loc gets rows (or columns) with particular labels from the index.
#iloc gets rows (or columns) at particular positions in the index (so it only takes integers).

# %% [markdown]
# ### Saving a Dataframe
# 
# The following code performs a shuffle and then saves a new copy.

# %%
import os
import pandas as pd
import numpy as np

path = "./data/"

filename_read = os.path.join(path,"auto-mpg.csv")
filename_write = os.path.join(path,"auto-mpg-shuffle.csv")
df = pd.read_csv(filename_read,na_values=['NA','?'])
df = df.reindex(np.random.permutation(df.index))
df.to_csv(filename_write,index=False)   # Specify index = false to not write row numbers
print("Done")

# %% [markdown]
# ### Dropping Fields
# 
# Some fields are of no value to the neural network and can be dropped.  The following code removes the name column from the MPG dataset.

# %%
import os
import pandas as pd
import numpy as np

path = "./data/"

filename_read = os.path.join(path,"auto-mpg.csv")
df = pd.read_csv(filename_read,na_values=['NA','?'])

print("Before drop: {}".format(df.columns))
df.drop('name', axis=1, inplace=True)
print("After drop: {}".format(df.columns))
df[0:5]

# %% [markdown]
# ### Calculated Fields
# 
# It is possible to add new fields to the dataframe that are calculated from the other fields.  We can create a new column that gives the weight in kilograms.  The equation to calculate a metric weight, given a weight in pounds is:
# 
# $ m_{(kg)} = m_{(lb)} \times 0.45359237 $
# 
# This can be used with the following Python code:

# %%
import os
import pandas as pd
import numpy as np

path = "./data/"

filename_read = os.path.join(path,"auto-mpg.csv")
df = pd.read_csv(filename_read,na_values=['NA','?'])
df.insert(1,'weight_kg',(df['weight']*0.45359237).astype(int))
df

# %% [markdown]
# ### Feature Normalization 
# 
# A normalization allows numbers to be put in a standard form so that two values can easily be compared. One very common machine learning normalization is the Z-Score:
# 
# $z = {x- \mu \over \sigma} $
# 
# To calculate the Z-Score you need to also calculate the mean($\mu$) and the standard deviation ($\sigma$).  The mean is calculated as follows:
# 
# $\mu = \bar{x} = \frac{x_1+x_2+\cdots +x_n}{n}$
# 
# The standard deviation is calculated as follows:
# 
# $\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2}, {\rm \ \ where\ \ } \mu = \frac{1}{N} \sum_{i=1}^N x_i$
# 
# The following Python code ***replaces the mpg with a z-score***.  Cars with average MPG will be near zero, above zero is above average, and below zero is below average.  Z-Scores above/below -3/3 are very rare, these are outliers.

# %%
import os
import pandas as pd
import numpy as np
from scipy.stats import zscore

path = "./data/"

filename_read = os.path.join(path,"auto-mpg.csv")
df = pd.read_csv(filename_read,na_values=['NA','?'])
df['mpg'] = zscore(df['mpg'])
df

# %% [markdown]
# ### Missing Values
# 
# You can also simply drop any rows with any NA values.  Another common practice is to replace missing values with the median value for that column. The following code replaces any NA values in horsepower with the median:

# %%
import os
import pandas as pd
import numpy as np
from scipy.stats import zscore

path = "./data/"

filename_read = os.path.join(path,"auto-mpg.csv")
df = pd.read_csv(filename_read,na_values=['NA','?'])
med = df['horsepower'].median()
df['horsepower'] = df['horsepower'].fillna(med)

# df = df.dropna() # you can also simply drop NA values

# %% [markdown]
# ### Concatenating Rows and Columns
# Rows and columns can be concatenated together to form new data frames.

# %%
# Create a new dataframe from name and horsepower

import os
import pandas as pd
import numpy as np
from scipy.stats import zscore

path = "./data/"

filename_read = os.path.join(path,"auto-mpg.csv")
df = pd.read_csv(filename_read,na_values=['NA','?'])
col_horsepower = df['horsepower']
col_name = df['name']
result = pd.concat([col_name,col_horsepower],axis=1)
result

# %%
# Create a new dataframe from name and horsepower, but this time by row

import os
import pandas as pd
import numpy as np
from scipy.stats import zscore

path = "./data/"

filename_read = os.path.join(path,"auto-mpg.csv")
df = pd.read_csv(filename_read,na_values=['NA','?'])
col_horsepower = df['horsepower']
col_name = df['name']
result = pd.concat([col_name,col_horsepower])
result

# %% [markdown]
# # Helpful Functions for Tensorflow (Little Gems)
# 
# The following functions will be used with TensorFlow to help preprocess the data.  
# 
# ### They allow you to build the feature vector in the format that TensorFlow expects from raw data.
# 
# (1) Encoding data:
# 
# * **encode_text_dummy** - Encode text fields as numeric, such as the iris species as a single field for each class.  Three classes would become "0,0,1" "0,1,0" and "1,0,0". Encode non-target features this way. used when the data is part of input ***(one hot encoding)***
# * **encode_text_index** - Encode text fields to numeric, such as the iris species as a single numeric field as "0" "1" and "2".  Encode the target field for a classification this way.  used when data is part of output            ***(label encoding)***
# 
# (2) Normalizing data:
# 
# * **encode_numeric_zscore** - Encode numeric values as a z-score.  Neural networks deal well with "normalized" fields only. 
# * **encode_numeric_range** - Encode a column to a range between the given normalized_low and normalized_high.
# 
# (3) Dealing with missing data:
# 
# * **missing_median** - Fill all missing values with the median value.
# 
# 
# (4) Removing outliers:
# 
# * **remove_outliers**  - Remove outliers in a certain column with a value beyond X times SD
# 
# 
# (5) Creating the feature vector and target vector that *** Tensorflow needs***:
# 
# * **to_xy** - ***Once all fields are encoded to numeric, this function can provide the x and y matrixes that TensorFlow needs to fit the neural network with data.***
# 
# (6) Other utility functions:
# 
# * **hms_string** - Print out an elapsed time string.
# * **chart_regression** - Display a chart to show how well a regression performs.

# %%
import collections
from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shutil
import os


# Encode text values to dummy variables(i.e. [1,0,0],[0,1,0],[0,0,1] for red,green,blue)
def encode_text_dummy(df, name):
    dummies = pd.get_dummies(df[name])
    for x in dummies.columns:
        dummy_name = "{}-{}".format(name, x)
        df[dummy_name] = dummies[x]
    df.drop(name, axis=1, inplace=True)


# Encode text values to indexes(i.e. [1],[2],[3] for red,green,blue).
def encode_text_index(df, name):
    le = preprocessing.LabelEncoder()
    df[name] = le.fit_transform(df[name])
    return le.classes_


# Encode a numeric column as zscores
def encode_numeric_zscore(df, name, mean=None, sd=None):
    if mean is None:
        mean = df[name].mean()

    if sd is None:
        sd = df[name].std()

    df[name] = (df[name] - mean) / sd


# Convert all missing values in the specified column to the median
def missing_median(df, name):
    med = df[name].median()
    df[name] = df[name].fillna(med)


# Convert all missing values in the specified column to the default
def missing_default(df, name, default_value):
    df[name] = df[name].fillna(default_value)


# Convert a Pandas dataframe to the x,y inputs that TensorFlow needs
def to_xy(df, target):
    result = []
    for x in df.columns:
        if x != target:
            result.append(x)
    # find out the type of the target column. 
    target_type = df[target].dtypes
    target_type = target_type[0] if isinstance(target_type, collections.Sequence) else target_type
    # Encode to int for classification, float otherwise. TensorFlow likes 32 bits.
    if target_type in (np.int64, np.int32):
        # Classification
        dummies = pd.get_dummies(df[target])
        return df[result].values.astype(np.float32), dummies.values.astype(np.float32)
    else:
        # Regression
        return df[result].values.astype(np.float32), df[target].values.astype(np.float32)

# Nicely formatted time string
def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)


# Regression chart.
def chart_regression(pred,y,sort=True):
    t = pd.DataFrame({'pred' : pred, 'y' : y.flatten()})
    if sort:
        t.sort_values(by=['y'],inplace=True)
    a = plt.plot(t['y'].tolist(),label='expected')
    b = plt.plot(t['pred'].tolist(),label='prediction')
    plt.ylabel('output')
    plt.legend()
    plt.show()

# Remove all rows where the specified column is +/- sd standard deviations
def remove_outliers(df, name, sd):
    drop_rows = df.index[(np.abs(df[name] - df[name].mean()) >= (sd * df[name].std()))]
    df.drop(drop_rows, axis=0, inplace=True)


# Encode a column to a range between normalized_low and normalized_high.
def encode_numeric_range(df, name, normalized_low=-1, normalized_high=1,
                         data_low=None, data_high=None):
    if data_low is None:
        data_low = min(df[name])
        data_high = max(df[name])

    df[name] = ((df[name] - data_low) / (data_high - data_low)) * (normalized_high - normalized_low) + normalized_low


# %% [markdown]
# ### Examples of label encoding, one hot encoding,  and creating X/Y for TensorFlow

# %%
df=pd.read_csv("data/iris.csv",na_values=['NA','?'])
df

# %%
encode_text_index(df,"species")   # label encoding
df

# %%
df=pd.read_csv("data/iris.csv",na_values=['NA','?'])

encode_text_dummy(df,"species")   # One hot encoding
df

# %% [markdown]
# ### Make sure you encode the lables first before you call to_xy()

# %%
df=pd.read_csv("data/iris.csv",na_values=['NA','?'])

encode_text_index(df,"species")    # encoding first before you call to_xy()

df

# %%
x,y = to_xy(df,"species")

# %%
x

# %%
y

# %% [markdown]
# ## Example of Deal with Missing Values and Outliers

# %%
path = "./data/"

filename_read = os.path.join(path,"auto-mpg.csv")
df = pd.read_csv(filename_read,na_values=['NA','?'])

# Handle mising values in horsepower
missing_median(df, 'horsepower')
#df.drop('name', 1,inplace=True)

# Drop outliers in horsepower
print("Length before MPG outliers dropped: {}".format(len(df)))
remove_outliers(df,'mpg',2)
print("Length after MPG outliers dropped: {}".format(len(df)))


# %% [markdown]
# ## Training and Validation
# 
# The machine learning model will learn from the training data, but ultimately be evaluated based on the validation data.
# 
# * **Training Data** - **In Sample Data** - The data that the machine learning model was fit to/created from. 
# * **Validation Data** - **Out of Sample Data** - The data that the machine learning model is evaluated upon after it is fit to the training data.
# 
# There are two predominant means of dealing with training and validation data:
# 
# * **Training/Test Split** - The data are split according to some ratio between a training and validation (hold-out) set.  Common ratios are 80% training and 20% validation.
# * **K-Fold Cross Validation** - The data are split into a number of folds and models.  Because a number of models equal to the folds is created out-of-sample predictions can be generated for the entire dataset.

# %% [markdown]
# ### Training/Test Split
# 
# The code below performs a split of the MPG data into a training and validation set.  The training set uses 80% of the data and the test(validation) set uses 20%.
# 
# The following image shows how a model is trained on 80% of the data and then validated against the remaining 20%.
# 
# ![Training and Validation](https://raw.githubusercontent.com/jeffheaton/t81_558_deep_learning/master/images/class_1_train_val.png "Training and Validation")
# 
# 

# %%
import pandas as pd
import io
import numpy as np
import os
from sklearn.model_selection import train_test_split


path = "./data/"
    
filename = os.path.join(path,"iris.csv")    
df = pd.read_csv(filename,na_values=['NA','?'])

df[0:5]

# %%
from sklearn import preprocessing

le = preprocessing.LabelEncoder()
df['encoded_species'] = le.fit_transform(df['species'])

df[0:5]

# %%
# Split into train/test
x_train, x_test, y_train, y_test = train_test_split(df[['sepal_l', 'sepal_w', 'petal_l', 'petal_w']], df['encoded_species'], test_size=0.25, random_state=42)


# %%
x_train.shape

# %%
y_train.shape

# %%
x_test.shape

# %%
y_test.shape

# %%


# %% [markdown]
# # Aggregation
# 
# Data aggregation is a preprocessing task where the values of two or more objects are combined into a single object. The motivation for aggregation includes (1) reducing the size of data to be processed, (2) changing the granularity of analysis (from fine-scale to coarser-scale), and (3) improving the stability of the data.
# 
# In the example below, we will use the daily precipitation time series data for a weather station located at Detroit Metro Airport. The raw data was obtained from the Climate Data Online website (https://www.ncdc.noaa.gov/cdo-web/). The daily precipitation time series will be compared against its monthly values.
# 
# **<font color="red">Code:</font>**
# 
# The code below will load the precipitation time series data and draw a line plot of its daily time series.

# %%
daily = pd.read_csv('DTW_prec.csv', header='infer')
daily.index = pd.to_datetime(daily['DATE'])
daily = daily['PRCP']
ax = daily.plot(kind='line',figsize=(15,3))
ax.set_title('Daily Precipitation (variance = %.4f)' % (daily.var()))

# %%
daily

# %% [markdown]
# Observe that the daily time series appear to be quite chaotic and varies significantly from one time step to another. The time series can be grouped and aggregated by month to obtain the total monthly precipitation values. The resulting time series appears to vary more smoothly compared to the daily time series.
# 
# **<font color="red">Code:</font>**

# %%
monthly = daily.groupby(pd.Grouper(freq='M')).sum()
ax = monthly.plot(kind='line',figsize=(15,3))
ax.set_title('Monthly Precipitation (variance = %.4f)' % (monthly.var()))

# %% [markdown]
# In the example below, the daily precipitation time series are grouped and aggregated by year to obtain the annual precipitation values. 
# 
# **<font color="red">Code:</font>**

# %%
annual = daily.groupby(pd.Grouper(freq='Y')).sum()
ax = annual.plot(kind='line',figsize=(15,3))
ax.set_title('Annual Precipitation (variance = %.4f)' % (annual.var()))

# %% [markdown]
# # Sampling
# 
# Sampling is an approach commonly used to facilitate (1) data reduction for exploratory data analysis and scaling up algorithms to big data applications and (2) quantifying uncertainties due to varying data distributions. There are various methods available for data sampling, such as sampling without replacement, where each selected instance is removed from the dataset, and sampling with replacement, where each selected instance is not removed, thus allowing it to be selected more than once in the sample.
# 
# In the example below, we will apply sampling with replacement and without replacement to the breast cancer dataset obtained from the UCI machine learning repository.
# 
# **<font color="red">Code:</font>**
# 
# We initially display the first five records of the table.

# %%
data.head()

# %% [markdown]
# In the following code, a sample of size 3 is randomly selected (without replacement) from the original data.
# 
# **<font color="red">Code:</font>**

# %%
sample = data.sample(n=3)
sample

# %% [markdown]
# In the next example, we randomly select 1% of the data (without replacement) and display the selected samples. The random_state argument of the function specifies the seed value of the random number generator.
# 
# **<font color="red">Code:</font>**

# %%
sample = data.sample(frac=0.01, random_state=1)
sample

# %% [markdown]
# Finally, we perform a sampling with replacement to create a sample whose size is equal to 1% of the entire data. You should be able to observe duplicate instances in the sample by increasing the sample size.
# 
# **<font color="red">Code:</font>**

# %%
sample = data.sample(frac=0.01, replace=True, random_state=1)
sample

# %% [markdown]
# # Discretization
# 
# Discretization is a data preprocessing step that is often used to transform a continuous-valued attribute to a categorical attribute. The example below illustrates two simple but widely-used unsupervised discretization methods (equal width and equal depth) applied to the 'Clump Thickness' attribute of the breast cancer dataset.

# %% [markdown]
# First, we plot a histogram that shows the distribution of the attribute values. The value_counts() function can also be applied to count the frequency of each attribute value.
# 
# **<font color="red">Code:</font>**

# %%
data['Clump Thickness'].hist(bins=10)
data['Clump Thickness'].value_counts(sort=False)

# %% [markdown]
# For the equal width method, we can apply the cut() function to discretize the attribute into 4 bins of similar interval widths. The value_counts() function can be used to determine the number of instances in each bin.
# 
# **<font color="red">Code:</font>**

# %%
bins = pd.cut(data['Clump Thickness'],4)
bins.value_counts(sort=False)

# %% [markdown]
# For the equal frequency method, the qcut() function can be used to partition the values into 4 bins such that each bin has nearly the same number of instances.
# 
# **<font color="red">Code:</font>**

# %%
bins = pd.qcut(data['Clump Thickness'],4)
bins.value_counts(sort=False)

# %% [markdown]
# # Principal Component Analysis
# 
# Principal component analysis (PCA) is a classical method for reducing the number of attributes in the data by projecting the data from its original high-dimensional space into a lower-dimensional space. The new attributes (also known as components) created by PCA have the following properties: (1) they are linear combinations of the original attributes, (2) they are orthogonal (perpendicular) to each other, and (3) they capture the maximum amount of variation in the data.
# 
# The example below illustrates the application of PCA to an image dataset. There are 16 RGB files, each of which has a size of 111 x 111 pixels. The example code below will read each image file and convert the RGB image into a 111 x 111 x 3 = 36963 feature values. This will create a data matrix of size 16 x 36963.    
# 
# **<font color="red">Code:</font>**

# %%
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

numImages = 16
fig = plt.figure(figsize=(7,7))
imgData = np.zeros(shape=(numImages,36963))

for i in range(1,numImages+1):
    filename = 'pics/Picture'+str(i)+'.jpg'
    img = mpimg.imread(filename)
    ax = fig.add_subplot(4,4,i)
    plt.imshow(img)
    plt.axis('off')
    ax.set_title(str(i))
    imgData[i-1] = np.array(img.flatten()).reshape(1,img.shape[0]*img.shape[1]*img.shape[2])

# %% [markdown]
# Using PCA, the data matrix is projected to its first two principal components. The projected values of the original image data are stored in a pandas DataFrame object named projected.
# 
# **<font color="red">Code:</font>**

# %%
import pandas as pd
from sklearn.decomposition import PCA

numComponents = 2
pca = PCA(n_components=numComponents)
pca.fit(imgData)

projected = pca.transform(imgData)
projected = pd.DataFrame(projected,columns=['pc1','pc2'],index=range(1,numImages+1))
projected['food'] = ['burger', 'burger','burger','burger','drink','drink','drink','drink',
                      'pasta', 'pasta', 'pasta', 'pasta', 'chicken', 'chicken', 'chicken', 'chicken']
projected

# %% [markdown]
# Finally, we draw a scatter plot to display the projected values. Observe that the images of burgers, drinks, and pastas  are all projected to the same region. However, the images for fried chicken (shown as black squares in the diagram) are harder to discriminate. 
# 
# **<font color="red">Code:</font>**

# %%
import matplotlib.pyplot as plt

colors = {'burger':'b', 'drink':'r', 'pasta':'g', 'chicken':'k'}
markerTypes = {'burger':'+', 'drink':'x', 'pasta':'o', 'chicken':'s'}

for foodType in markerTypes:
    d = projected[projected['food']==foodType]
    plt.scatter(d['pc1'],d['pc2'],c=colors[foodType],s=60,marker=markerTypes[foodType])

# %%



