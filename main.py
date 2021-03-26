import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import confusion_matrix
import copy


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


def splitData(data, test_ratio, y_columns):
    Y = data[y_columns]
    del data[y_columns]
    return train_test_split(data, Y, test_size=test_ratio, shuffle=True, stratify=Y)


file_name = './exam.csv'
# analyze(file_name)

df = pd.read_csv(file_name)

  # D, G, K, L, M, Q, S
df = df.drop(columns=['A', 'B', 'C', 'E', 'F', 'H', 'I', 'J', 'N', 'O', 'P', 'R', 'T', 'U', 'V', 'W', 'X', 'Y'], axis=1)

x_train, x_test, y_train, y_test = splitData(copy.deepcopy(df), 0.5, 'Z')

# K voisins
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
print('KNN')
print('train :', knn.score(x_train, y_train))
print('test :', knn.score(x_test, y_test))
print(confusion_matrix(y_test, knn.predict(x_test)))

# Neural network
print('MLP')
x_train, x_test, y_train, y_test = splitData(copy.deepcopy(df), 0.5, 'Z')
mlp = MLPClassifier()
train = mlp.fit(x_train, y_train)

print('train :', mlp.score(x_train, y_train))
print('test :', mlp.score(x_test, y_test))
print(confusion_matrix(y_test, mlp.predict(x_test)))

# Arbre de decision
print('TREE')
x_train, x_test, y_train, y_test = splitData(copy.deepcopy(df), 0.5, 'Z')
tree = DecisionTreeClassifier(criterion='entropy')
tree.fit(x_train, y_train)
print('train :', tree.score(x_train, y_train))
print('test :', tree.score(x_test, y_test))
print(confusion_matrix(y_test, tree.predict(x_test)))

export_graphviz(tree, out_file='glass_tree.dot',
        feature_names=['D', 'G', 'K', 'L', 'M', 'Q', 'S'])

