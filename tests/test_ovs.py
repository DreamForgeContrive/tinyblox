__author__ = "Kiran Vemuri"
__email__ = "kiran_vemuri@adaranetworks.com"
__status__ = "Development"
__maintainer__= "None"

from sqaSentinel import ovsx
from sqaSentinel import logx
import datetime
import yaml

with open('./config_vars.yaml', 'r') as stream:
    try:
        test_config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print exc

lgx = logx.LogX(test_config['Log']['path'])
lh = lgx.log_handler()
lh.info("\n ***** \n Starting test_cassandra execution \
         | {} \n ***** \n".format(datetime.datetime.now()))

lh.info("Downgrading paramiko to 1.17.0 to execute test_ovs unit tests because of the following issue: http://stackoverflow.com/questions/443387/why-does-paramiko-hang-if-you-use-it-while-loading-a-module/450895#450895")

ovx = ovsx.OvsX(test_config['Ovs']['IP'],
                test_config['Ovs']['username'],
                test_config['Ovs']['password'])

def test_ovs_1():
    """
    get controller and validate
    """
    pass

def test_ovs_2():
    """
    set controller and validate
    """
    pass

def test_ovs_3():
    """
    del controller and validate
    """
    pass

def test_ovs_4():
    """
    set bridge protocols and validate
    """
    pass

def test_ovs_5():
    """
    get bridge protocols and validate
    """
    pass

def test_ovs_6():
    """
    add bridge and validate
    """
    pass

def test_ovs_7():
    """
    del bridge and validate
    """
    pass

def test_ovs_8():
    """
    mod port and validate
    """
    pass
