__author__ = "Kiran Vemuri"
__email__ = "kiran_vemuri@adaranetworks.com"
__status__ = "Development"
__maintainer__= "None"

from Sentinel import cassandrax
from Sentinel import logx
import datetime
import yaml

with open('./config_vars.yaml', 'r') as stream:
    try:
        test_config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print exc

csx = cassandrax.CassandraX(test_config['Cassandra']['IP'])

lgx = logx.LogX(test_config['Log']['path'])
lh = lgx.log_handler()
lh.info("\n ***** \n Starting test_cassandra execution \
         | {} \n ***** \n".format(datetime.datetime.now()))

def test_cassandra_1():
    """
    Fetch keyspaces and validate
    """
    lh.info("*test_cassandra_1: fetch keyspaces and validate")
    keyspace_list = csx.fetch_keyspaces()
    lh.info("Retrieved keyspace list {}".format(keyspace_list))
    assert 'system' in keyspace_list

def test_cassandra_2():
    """
    Run query and validate
    """
    lh.info("*test_cassandra_2: run query and validate")
    query_result = csx.run_query("select keyspace_name from system.schema_keyspaces")
    result_list = [xdict["keyspace_name"] for xdict in query_result]
    lh.info("Query result: {} and result_list: {}".format(query_result, result_list))
    assert 'system' in result_list


def test_cassandra_3():
    """
    Run query with keyspace and validate
    """
    lh.info("*test_cassandra_3: run query with keyspace and validate")
    query_result = csx.run_query("select keyspace_name from schema_keyspaces", keyspace='system')
    result_list = [xdict["keyspace_name"] for xdict in query_result]
    lh.info("Query result: {}, result_list: {}".format(query_result,result_list))
    assert 'system' in result_list
