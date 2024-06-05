import pandas as pd
import numpy as np
from jaal import Jaal


class Node:
    """
    every decicion node is an instance of class Node
    every node attribute is what its childs are divided with
    childrens are a dictionery with their class of data in attribute as key and child node as value
    functions:
        is_leaf function returns True whether the node is a leaf node or False if not
    
    """

    name_counter=0
    
    
    def __init__(self,attribute,attr_class,dividing_attribute,labels:pd.Series,parent,gain):
        self.name=Node.name_counter
        self.attribute = attribute
        self.attr_class =attr_class
        self.dividing_attribute=dividing_attribute
        self.labels_count = labels
        self.value = labels.index[0]
        self.parent = parent
        self.children ={}
        self.gain=gain
        Node.name_counter +=1
        
        
    def is_leaf(self):
        if not self.children:
            return not (bool(self.children))
    
    
    
    
    def __str__(self):
        result=f"""attr:{self.attribute}/{self.attr_class} , value:{self.value}
        gain:{round(self.gain,3)} , data_size:{self.labels_count.sum()}
        False_count:{self.labels_count[0]} , True_count:{self.labels_count[1]}
        name:{self.name}
        """
        short_result=f'*{self.name}*attr:{self.attribute}/{self.attr_class} , value:{self.value}'
        
        short_value_data=f'*{self.name}*False_count:{self.labels_count[0]} , True_count:{self.labels_count[1]}'
        
        return short_result
    
class Decision_Tree:
    """
    main decision tree class
    every decision tree instance is a seperate decision tree with its own settings
    max_depth and max_nodes and min_gain is used for stopping criterion
    tree will be stored in root and after training is complete,it will test the trained data and store the result as file
    note:data classification must be done and all attribute in passed data should have classified data
    and last column of data must be label
    functions:
        train==>main function of this class,it will recursively split the data to classes with training data
        gini_index==>used for getting gini value of data
        entropy==> used for getting entropy of data
        info_gain==>use entropy or gini_index to calculate information gain for an attribute
        visualize_tree==> create a graphical network of trained decision tree
        test==> will test the decision tree with given data and store the result in a file
        predict==> used in test function,test each row of data in tree
        stopping_criterion==>a function for stopping the training proccess when a ccondition is met
        
    """
    
    def __init__(self,data:pd.DataFrame,max_depth:int=None,max_node:int=None,minimum_gain:float=0,method="entropy"):
        self.max_depth = max_depth
        self.depth=0
        self.max_node=max_node
        self.current_nodes=0
        self.minimum_gain=minimum_gain
        self.method=method
        self.edges={'from':[],'to':[]}
        self.nodes={'id':[],'value':[],'color':[]}
        self.root = self.train(data,data.columns[:-1])
        self.test(data,'.\\results\\train_result.txt')
        
        
        
    def train(self,data:pd.DataFrame,attributes:pd.Series,parent=None,attr=[' ',' '],current_depth=0):
        if data.empty:
            return None
        if attributes.empty:
            return None
        best_gain=0
        for attribute in attributes:
            current_gain=self._info_gain(data,attribute)
            if current_gain>best_gain:
                best_gain=current_gain
                best_attribute =attribute
        if self._stopping_criteria(best_gain,current_depth):
            return None
        labels=data[data.columns[-1]].value_counts()
        node=Node(attr[0],attr[1],best_attribute,labels,parent,best_gain)
        self.current_nodes+=1
        if str(node) in self.nodes['id']:
            print('repeated_node name detected')
        self.nodes['id'].append(str(node))
        self.nodes['value'].append(labels[0])
        self.nodes['color'].append(str(labels.index[0]))
        attr_classes=data[best_attribute].unique()
        for attr_class in attr_classes:
            child_node=self.train(data[data[best_attribute]==attr_class],attributes.drop(best_attribute),node,[best_attribute,attr_class],current_depth+1)
            if child_node!=None:
                self.edges['from'].append(str(node))
                self.edges['to'].append(str(child_node))
                node.children[attr_class]=child_node
        return node
            
            
            
    def _gini_index(self,data:pd.DataFrame):
        all_data_count=data.shape[0]
        probabilities=data[data.columns[-1]].value_counts()/all_data_count
        gini=1-np.sum(probabilities**2)
        return gini
    
    
    
    def _entropy(self,data:pd.DataFrame):
        all_data_count=data.shape[0]
        probabilities=data[data.columns[-1]].value_counts()/all_data_count
        entropy=-np.sum(probabilities*np.log2(probabilities))
        return entropy
    
    
    
    def _info_gain(self,data:pd.DataFrame,attribute):
        if self.method=='entropy':
            func=self._entropy
        elif self.method=='gini_index':
            func=self._gini_index
        else:
            print('wrong method')
            quit()
        all_data_size=data.shape[0]
        parent_etp_gini=func(data)
        attribute_classes=data[attribute].unique()
        gain=parent_etp_gini
        for attr_class in attribute_classes:
            attr_class_data=data[data[attribute]==attr_class]
            weighted_value=attr_class_data.shape[0]/all_data_size
            gain-=weighted_value*func(attr_class_data)
        return gain
    
    
    
    def visualize_tree(self):
        node_df=pd.DataFrame(self.nodes)
        edge_df=pd.DataFrame(self.edges)
        Jaal(node_df=node_df,edge_df=edge_df).plot()
        
        
        
    def test(self,data:pd.DataFrame,result_file_dir='.\\results\\test_result.txt'):
        result_file=open(result_file_dir,'wt')
        #result_file.write('  result   label\n')
        right_count=0
        count=0
        test_result=[]
        label=data.columns[-1]
        for i in range(data.index[0],data.index[-1]+1):
            row =data.loc[i]
            result=self._predict(row)
            #result_file.write(f'    {result}        {row[label]}\n')
            right_count+=int(result==row[label])
            count+=1
            test_result.append(result)
        try:
            result_file.write(f'Results:\nrights={right_count}\ntotal={count}\npersent={right_count/count}\n')
        except ZeroDivisionError:
            print(data.index[0],data.index[-1]+1)
            quit()
        result_file.close()
        return pd.Series(test_result)
            
            
            
    def _predict(self,row):
        current_node=self.root
        while True:
            if current_node.is_leaf():
                return current_node.value
            else:
                try:
                    current_node=current_node.children[row[current_node.dividing_attribute]]
                except KeyError:
                    return current_node.value
         

    
    def _stopping_criteria(self,gain,current_depth):
        if self.max_depth!=None:
            if current_depth>=self.max_depth:
                return True
        if self.max_node!=None:
            if self.current_nodes>=self.max_node:
                return True
            
        if gain<=self.minimum_gain:
            return True
        return False
        
        
        