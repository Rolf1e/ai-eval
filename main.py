import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def plot_data(data, hue):
    sns.set_style('whitegrid')
    sns.pairplot(data, hue=hue)
    plt.show()


def label_encode(data, col_name):
    le = LabelEncoder()
    unique = list(data[col_name].unique())
    le_fitted= le.fit(unique) 
    values = list(data[col_name].values)
    values_transformed= le.transform(values)
    data[col_name] = values_transformed

    

def analyze_data(data):
    averages = data.mean()
    print(averages)

    sns.set()
    plt.figure(figsize=(15, 8))
    plt.hist(data)
    print(data.shape)
    sns.heatmap(data.corr(), vmax=0.5, cmap="PiYG")
    plt.title('Correlation matrix')
    plt.show()


def analyze(file_name):
    df = pd.read_csv(file_name)

    print('HEAD =>\n', df.head()) 
    print('Nombre d\'exemples :\n', df.shape)

    print('\n INFO:')
    df.info()

    label_encode(df, 'C')
    print('describe:\n', df.describe())
    analyze_data(df)


analyze('./exam.csv')

