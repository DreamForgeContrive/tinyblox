__author__ = "Kiran Vemuri"
__email__ = "kkvemuri@uh.edu"
__status__ = "Development"
__maintainer__ = "None"

from tinyblox import remotex
from tinyblox import logx
import yaml
import datetime

with open('./config_vars.yaml', 'r') as stream:
    try:
        test_config = yaml.load(stream)
        lgx = logx.Log(test_config['Log']['path'])
        lh = lgx.log_handler()
        lh.info("\n ***** \n Starting test_connect execution \
                 | {} \n ***** \n".format(datetime.datetime.now()))
        lh.info("Downgrading paramiko to 1.17.0 to execute test_connect unit tests because of the following issue: "
                "http://stackoverflow.com/questions/443387/why-does-paramiko-hang-if-you-use-it-while-loading-a-module/"
                "450895#450895")

        connx = remotex.Connection(test_config['Connect']['IP'],
                                   test_config['Connect']['port'],
                                   test_config['Connect']['username'],
                                   test_config['Connect']['password'])
    except yaml.YAMLError as exc:
        print exc


def test_connect_1():
    """
    Execute a command and validate
    """
    lh.info("*test_connect_1: execute a command and validate")
    command_out = connx.execute("ifconfig eth0 | grep inet\ addr")
    lh.info("command output: {}".format(command_out))
    assert test_config['Connect']['IP'] in command_out['out'][0]


def test_connect_2():
    """
    Execute a command with sudo and validate
    """
    lh.info("*test_connect_2: execute a command with sudo and validate")
    command_out = connx.execute("ifconfig eth0 | grep inet\ addr")
    lh.info("command output: {}".format(command_out))
    assert test_config['Connect']['IP'] in command_out['out'][0]
