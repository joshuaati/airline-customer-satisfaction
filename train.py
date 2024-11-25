import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier


# parameters
max_depth = 15
min_samples_leaf=1

print('Importing data...')
# import data
test = pd.read_csv('./data/test.csv')
train = pd.read_csv('./data/train.csv')
df = pd.concat([train, test], ignore_index=True)

print('Cleaning data...')
# drop non-useful columns
df = df.drop(columns=['Unnamed: 0', 'id'])
# format column headers
df.columns = df.columns.str.lower().str.replace(' ', '_')
# drop null values
df = df.dropna()
# convert arrival_delay_in_minutes to correct datatype
df.arrival_delay_in_minutes = df.arrival_delay_in_minutes.astype('int64')
# convert the target column into binary
df['satisfaction'] = (df['satisfaction']== 'satisfied').astype(int)


df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.satisfaction.values
y_val = df_val.satisfaction.values
y_test = df_test.satisfaction.values

del df_train['satisfaction']
del df_val['satisfaction']
del df_test['satisfaction']


dv = DictVectorizer(sparse=False)
train_dict = df_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

val_dict = df_val.to_dict(orient='records')
X_val = dv.transform(val_dict)

print('Training the model...')
rf_model = RandomForestClassifier(n_estimators=200,
                            max_depth=max_depth,
                            min_samples_leaf=min_samples_leaf,
                            random_state=1)
rf_model.fit(X_train, y_train)


print('Saving the model')
import pickle
output_file = f'rf_model.bin'

f_out = open(output_file, 'wb') 
pickle.dump((dv, rf_model), f_out)
f_out.close()

print(f'The model is save to {output_file}')
