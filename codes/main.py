import pandas as pd
from decision_tree import Decision_Tree
from data_analyze import analyze_mean
from data_classifier import classify_data


classify_data(pd.read_csv('.\\data\\onlinefraud.csv'),balanced=1)
train_data=pd.read_csv('.\\data\\onlineFraud_train.csv')
test_data=pd.read_csv('.\\data\\onlineFraud_test.csv')


d_tree=Decision_Tree(train_data,method='entropy',max_node=60)
d_tree.test(test_data)
d_tree.visualize_tree()

