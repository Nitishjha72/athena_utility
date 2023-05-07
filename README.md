This is an AWS Athena utility project. This starter kit will be helpful when there is need to query athena and get result programatically.

**The aws_access_key_id and aws_secret_access_key are kept as env variable. Before running this project, please set these 2 as evironment variables or set the aws_profile in local at .aws/credentials.**


athena_utility.py - This file contains query_results(), delete_output() and read_config() function. 
                    The query_results() function is used for getting the output of a query in json format.
                    The delete_output() function is used for deleting the query result saved in s3. This is just a clean up function.
                    The read_config() function is used for reading the .conf file where configuration like datbase, bucket, etc are present.
                    
athena_config.conf - This is the config file where all the config related to database and athena are present.
** The aws_access_key_id and aws_secret_access_key are kept as env variable. Before running this, please set these 2 as evironment variables

main.py - This is the starter file which calls all the necessary function to achieve the functionality. 

Command to run: python3 main.py
