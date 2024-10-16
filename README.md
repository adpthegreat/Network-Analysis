# This is a repo to demonstrate blockchain network analysis in python using pandas, networkx and plotly

We get the data from the queries dune api in csv format, then use the output flag `-o` to save the csv data in .csv files from the curl command

To get the data from the queries you need to sign up to dune , then get an `api_key` that will be used in the api queries , note that the `api_key` is only view once so copy it to another place an edit it into your curl commands

Note that there is an option to download .csv files from the dune dashboard directly but it is not available on a free tier

Run these in your terminal to get the .csv data
curl -H "X-Dune-API-Key:<api_key>" "https://api.dune.com/api/v1/query/1753177/results/csv?limit=1000" -o graph_raw_relation.csv
curl -H "X-Dune-API-Key:<api_key>" "<https://api.dune.com/api/v1/query/2430347/results/csv?limit=1000>" -o graph_raw_label.csv
