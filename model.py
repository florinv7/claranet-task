import sys, pickle, sklearn
import pandas as pd

def main(argv):
    query = argv[0]
    query = query.replace('\n\t',' ')
    query = query.replace('\n',' ')
    query = query.replace('\t',' ')

    loaded_model = pickle.load(open("./model/model_query_exec_prediction", 'rb'))
    
    X_test = [extract_features_query(query)]
    
    prediction = int(loaded_model.predict(X_test))
    prediction_string = ''

    if(prediction >= 10**6):
        seconds = prediction/(10**6)
        if(seconds > 9):
            seconds = str(seconds)
        else:
            seconds = "0" + str(seconds)
        prediction_string = "00:00:" + seconds + str(prediction%(10**6))
    else:
        prediction_string = "00:00:00." + str(prediction)
    
    print("Execution time for query is\n " + prediction_string)

def extract_features_query(query):
    features_query = []
    
    sql_operations = ['select', 'insert', 'update', 'where', 'join', 
        'order', 'group', 'union', 'count', 'avg', 'sum', 'show', 'set', 
        'ping', 'quit', 'purge', 'flush', 'statistics', 'commit', 'use']
    for sql_op in sql_operations:
        features_query.append(query.count(sql_op))
    
    tables = ['customer','lineitem','nation','orders','part','partsupp','region','supplier']
    for t in tables:
        features_query.append(query.count(t))
    return features_query

if __name__ == "__main__":
   main(sys.argv[1:])