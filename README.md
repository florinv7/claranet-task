# claranet-task

## the jupyter notebook named Data Analytics contains the plots for the Data Analytics visualization tasks and some data exploration/cleaning for the further step of model training

## the file model.py is in charge of making predictions given the query
## to make a prediction just run in a terminal: 'model.py "query"' where "query" can be substituted with a SQL query (ex: "SELECT 1").
## be careful to not mix ' and ". Use always " " to delimit the entire query,
## while use ' ' for strings inside the query

## the output will be the predicted execution time 

## example of execution: 

## python model.py "select\n\tl_orderkey,\n\tsum(l_extendedprice * (1 - l_discount)) as revenue,\n\to_orderdate,\n\to_shippriority\nfrom\n\tcustomer,\n\torders,\n\tlineitem\nwhere\n\tc_mktsegment = 'MACHINERY'\n\tand c_custkey = o_custkey\n\tand l_orderkey = o_orderkey\n\tand o_orderdate < date '1995-03-11'\n\tand l_shipdate > date '1995-03-11'\ngroup by\n\tl_orderkey,\n\to_orderdate,\n\to_shippriority\norder by\n\trevenue desc,\n\to_orderdate"