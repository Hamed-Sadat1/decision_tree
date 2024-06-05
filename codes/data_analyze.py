
import pandas as pd
import matplotlib.pyplot as plt
def analyze_mean(raw_data:pd.DataFrame,attribute:str):
    """analyze the mean of label over given atribute"""
    label=raw_data.columns[-1]
    data=raw_data[[attribute, label]].groupby([attribute], as_index=False).mean()
    x=data[attribute]
    y=data[label]
    plt.xlabel(attribute)
    plt.ylabel(label)
    plt.plot(x,y)
    plt.show()
    return None