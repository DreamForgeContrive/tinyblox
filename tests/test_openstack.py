from sentinelpy.openstackx import openstackx
from sentinelpy.logx import Log

osx = openstackx.Openstack('10.10.86.3', 'admin', 'password')
logger = Log('./unit_test.log')

# Unit Tests

# Networking

# Internal Network


def test_create_int_network():
    """
    network_name = "TestNetwork"
    new_network = osx.Networking.create_network(network_name)
    """
    pass


def test_list_int_networks():
    pass


def test_show_int_network():
    pass


def test_update_network():
    pass


def test_delete_network():
    pass