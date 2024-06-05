import pandas as pd


def classify_data(data,balanced=0):
    
    #amount_cut
    data.loc[ data['amount'] <= 0, 'amount'] 						                = 0
    data.loc[(data['amount'] > 0) & (data['amount'] <= 250000), 'amount']           = 1
    data.loc[(data['amount'] > 250000) & (data['amount'] <= 500000), 'amount']      = 2
    data.loc[(data['amount'] > 500000) & (data['amount'] <= 750000), 'amount']      = 3
    data.loc[(data['amount'] > 750000) & (data['amount'] <= 1500000), 'amount']     = 4
    data.loc[(data['amount'] > 1500000) & (data['amount'] <= 2500000), 'amount']    = 5
    data.loc[(data['amount'] > 2500000) & (data['amount'] <= 4000000), 'amount']    = 6
    data.loc[(data['amount'] > 4000000) & (data['amount'] <= 7000000), 'amount']    = 8
    data.loc[(data['amount'] > 7000000) & (data['amount'] <= 10000000), 'amount']   = 9
    data.loc[ data['amount'] > 10000000, 'amount']							        = 10
    data['amount'] = data['amount'].astype(int)



    #nameOrig_cut
    data['nameOrig']=data['nameOrig'].str.slice(0,2)




    #oldbalanceOrg_cut
    data.loc[ data['oldbalanceOrg'] <= 0, 'oldbalanceOrg'] 						                         = 0
    data.loc[(data['oldbalanceOrg'] > 0) & (data['oldbalanceOrg'] <= 100000), 'oldbalanceOrg']           = 1
    data.loc[(data['oldbalanceOrg'] > 100000) & (data['oldbalanceOrg'] <= 500000), 'oldbalanceOrg']      = 2
    data.loc[(data['oldbalanceOrg'] > 500000) & (data['oldbalanceOrg'] <= 750000), 'oldbalanceOrg']      = 3
    data.loc[(data['oldbalanceOrg'] > 500000) & (data['oldbalanceOrg'] <= 2000000), 'oldbalanceOrg']     = 4
    data.loc[(data['oldbalanceOrg'] > 2000000) & (data['oldbalanceOrg'] <= 5000000), 'oldbalanceOrg']    = 5
    data.loc[(data['oldbalanceOrg'] > 5000000) & (data['oldbalanceOrg'] <= 13000000), 'oldbalanceOrg']   = 6
    data.loc[(data['oldbalanceOrg'] > 13000000) & (data['oldbalanceOrg'] <= 20000000), 'oldbalanceOrg']  = 8
    data.loc[(data['oldbalanceOrg'] > 20000000) & (data['oldbalanceOrg'] <= 34000000), 'oldbalanceOrg']  = 9
    data.loc[ data['oldbalanceOrg'] > 34000000, 'oldbalanceOrg']							             = 10
    data['oldbalanceOrg'] = data['oldbalanceOrg'].astype(int)



    #newbalanceOrig_cut
    data.loc[ data['newbalanceOrig'] <= 0, 'newbalanceOrig'] 						                        = 0
    data.loc[(data['newbalanceOrig'] > 0) & (data['newbalanceOrig'] <= 100000), 'newbalanceOrig']           = 1
    data.loc[(data['newbalanceOrig'] > 100000) & (data['newbalanceOrig'] <= 500000), 'newbalanceOrig']      = 2
    data.loc[(data['newbalanceOrig'] > 500000) & (data['newbalanceOrig'] <= 750000), 'newbalanceOrig']      = 3
    data.loc[(data['newbalanceOrig'] > 500000) & (data['newbalanceOrig'] <= 2000000), 'newbalanceOrig']     = 4
    data.loc[(data['newbalanceOrig'] > 2000000) & (data['newbalanceOrig'] <= 5000000), 'newbalanceOrig']    = 5
    data.loc[(data['newbalanceOrig'] > 5000000) & (data['newbalanceOrig'] <= 13000000), 'newbalanceOrig']   = 6
    data.loc[(data['newbalanceOrig'] > 13000000) & (data['newbalanceOrig'] <= 20000000), 'newbalanceOrig']  = 8
    data.loc[(data['newbalanceOrig'] > 20000000) & (data['newbalanceOrig'] <= 33800000), 'newbalanceOrig']  = 9
    data.loc[ data['newbalanceOrig'] > 33800000, 'newbalanceOrig']							                = 10
    data['newbalanceOrig'] = data['newbalanceOrig'].astype(int)



    #nameDest_cut
    data['nameDest']=data['nameDest'].str.slice(0,2)





    #oldbalanceDest_cut
    data.loc[ data['oldbalanceDest'] <= 0, 'oldbalanceDest'] 						                        = 0
    data.loc[(data['oldbalanceDest'] > 0) & (data['oldbalanceDest'] <= 100000), 'oldbalanceDest']           = 1
    data.loc[(data['oldbalanceDest'] > 100000) & (data['oldbalanceDest'] <= 500000), 'oldbalanceDest']      = 2
    data.loc[(data['oldbalanceDest'] > 500000) & (data['oldbalanceDest'] <= 750000), 'oldbalanceDest']      = 3
    data.loc[(data['oldbalanceDest'] > 500000) & (data['oldbalanceDest'] <= 2000000), 'oldbalanceDest']     = 4
    data.loc[(data['oldbalanceDest'] > 2000000) & (data['oldbalanceDest'] <= 5000000), 'oldbalanceDest']    = 5
    data.loc[(data['oldbalanceDest'] > 5000000) & (data['oldbalanceDest'] <= 7500000), 'oldbalanceDest']    = 6
    data.loc[(data['oldbalanceDest'] > 7500000) & (data['oldbalanceDest'] <= 13000000), 'oldbalanceDest']   = 8
    data.loc[(data['oldbalanceDest'] > 13000000) & (data['oldbalanceDest'] <= 34000000), 'oldbalanceDest']  = 9
    data.loc[ data['oldbalanceDest'] > 34000000, 'oldbalanceDest']							                = 10
    data['oldbalanceDest'] = data['oldbalanceDest'].astype(int)





    #newbalanceDest_cut
    data.loc[ data['newbalanceDest'] <= 0, 'newbalanceDest'] 						                        = 0
    data.loc[(data['newbalanceDest'] > 0) & (data['newbalanceDest'] <= 100000), 'newbalanceDest']           = 1
    data.loc[(data['newbalanceDest'] > 100000) & (data['newbalanceDest'] <= 500000), 'newbalanceDest']      = 2
    data.loc[(data['newbalanceDest'] > 500000) & (data['newbalanceDest'] <= 750000), 'newbalanceDest']      = 3
    data.loc[(data['newbalanceDest'] > 500000) & (data['newbalanceDest'] <= 2000000), 'newbalanceDest']     = 4
    data.loc[(data['newbalanceDest'] > 2000000) & (data['newbalanceDest'] <= 5000000), 'newbalanceDest']    = 5
    data.loc[(data['newbalanceDest'] > 5000000) & (data['newbalanceDest'] <= 13000000), 'newbalanceDest']   = 6
    data.loc[(data['newbalanceDest'] > 13000000) & (data['newbalanceDest'] <= 20000000), 'newbalanceDest']  = 8
    data.loc[(data['newbalanceDest'] > 20000000) & (data['newbalanceDest'] <= 34000000), 'newbalanceDest']  = 9
    data.loc[ data['newbalanceDest'] > 34000000, 'newbalanceDest']							                = 10
    data['newbalanceDest'] = data['newbalanceDest'].astype(int)
    data.to_csv()
    if balanced:
        fraud_data=data[data.isFraud==1].sample(frac=1)
        right_data=data[data.isFraud==0].sample(frac=1)
        test_data=pd.concat((fraud_data[:1000],right_data[:2000]),ignore_index=True).sample(frac=1)
        train_data=pd.concat((fraud_data[1000:2000],right_data[2000:4000]),ignore_index=True).sample(frac=1)
    else:
        count=data.shape[0]
        train_data=data[:int(count*0.8)].sample(frac=1)
        test_data=data[int(count*0.8):].sample(frac=1)

    train_data.to_csv('.\\data\\onlinefraud_train.csv',index=False)
    test_data.to_csv('.\\data\\onlinefraud_test.csv',index=False)
    return [train_data,test_data]