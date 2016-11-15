__author__ = "Kiran Vemuri"
__email__ = "kiran_vemuri@adaranetworks.com"
__status__ = "Development"
__maintainer__ = "Kiran Vemuri"

from tinyblox.openstackx import OSSession
from tinyblox.logx import Log
import pytest
import random
import string

osx = OSSession('10.11.86.3', 'admin', 'password')
logging = Log('./unit_test.log')
logger = logging.log_handler()


def random_string(str_len):
    """
    Generate a random string of the given length
    :param str_len: <int> length of the string to be generated
    :return: <str> random string of given length
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(str_len))


# Unit Tests

# Image


def test_create_image():
    """
    Create image and validate
    """
    pytest.skip("TODO")


def test_list_images():
    """
    List images and validate
    """
    logger.info("***starting test_list_images***")

    image_list = osx.Image.list_images()
    logger.info("Image list {}".format(image_list.json()))
    assert image_list.status_code == 200


def test_show_image_details():
    """
    Show image details and validate
    """
    logger.info("***starting test_show_image_details***")

    image_list = osx.Image.list_images()
    if len(image_list.json()['images']) > 0:
        show_image = osx.Image.show_image_details(image_list.json()['images'][0]['id'])
        logger.info("Image details {}".format(show_image.json()))
        assert show_image.status_code == 200
    else:
        logger.info("No registered images available for show_image_details request")
        pytest.skip("No registered images available for show_image_details request")


def test_delete_image():
    pytest.skip("TODO")


def test_deactivate_image():
    """
    Deactivate image and validate
    """
    logger.info("***starting test_deactivate_image***")

    image_list = osx.Image.list_images()
    if len(image_list.json()['images']) > 0:
        deactivate_image = osx.Image.deactivate_image(image_list.json()['images'][0]['id'])
        logger.info("Deactivate image status {}".format(deactivate_image.status_code))

        show_image = osx.Image.show_image_details(image_list.json()['images'][0]['id'])
        logger.info("Image status: {}".format(show_image.json()['status']))
        assert deactivate_image.status_code == 204 and show_image.json()['status'] == 'deactivated'
    else:
        logger.info("No registered images available for deactivate_image request")
        pytest.skip("No registered images available for deactivate_image request")


def test_reactivate_image():
    """
    Reactivate image and validate
    """
    logger.info("***starting test_reactivate_image***")

    image_list = osx.Image.list_images()
    if len(image_list.json()['images']) > 0:
        reactivate_image = osx.Image.reactivate_image(image_list.json()['images'][0]['id'])
        logger.info("Reactivate image status {}".format(reactivate_image.status_code))

        show_image = osx.Image.show_image_details(image_list.json()['images'][0]['id'])
        logger.info("Image status: {}".format(show_image.json()['status']))
        assert reactivate_image.status_code == 204 and show_image.json()['status'] == 'active'
    else:
        logger.info("No registered images available for deactivate_image request")
        pytest.skip("No registered images available for deactivate_image request")


# Networking

# Overlay Networks

def test_create_network():
    """
    Create a network and validate [admin_state=True, shared=False, external=False]
    """
    logger.info("***starting test_create_network***")

    net_name = random_string(10)
    net_create = osx.Networking.create_network(net_name, admin_state=True, shared=False, external=False)
    logger.info("New network : {}".format(net_create.json()))
    net_delete = osx.Networking.delete_network(net_create.json()['network']['id'])
    assert net_create.status_code == 201 and net_delete.status_code == 204


def test_create_network_shared():
    """
    Create a network and validate [admin_state=True, shared=True, external=False]
    """
    logger.info("***starting test_create_network_shared***")

    net_name = random_string(10)
    net_create = osx.Networking.create_network(net_name, admin_state=True, shared=True, external=False)
    logger.info("New network : {}".format(net_create.json()))
    net_delete = osx.Networking.delete_network(net_create.json()['network']['id'])
    assert net_create.status_code == 201 and net_delete.status_code == 204


def test_list_networks():
    """
    List existing networks and validate
    """
    logger.info("***starting test_list_networks***")

    net_list = osx.Networking.list_networks()
    logger.info("Network list: {}".format(net_list.json()))
    assert net_list.status_code == 200


def test_show_network():
    """
    Show network details and validate
    """
    logger.info("***starting test_show_networks***")

    net_list = osx.Networking.list_networks()
    if len(net_list.json()['networks']) > 0:
        net_show = osx.Networking.show_network(net_list.json()['networks'][0]['id'])
        logger.info("Network details : {}".format(net_show.json()))
        assert net_show.status_code == 200
    else:
        logger.info("No networks available")
        pytest.skip("No networks available")


def test_update_network():
    """
    Update the network name and validate
    """
    logger.info("***starting test_update_network***")

    net_name = random_string(10)
    net_create = osx.Networking.create_network(net_name, admin_state=True, shared=False, external=False)
    logger.info("Net network : {}".format(net_create.json()))

    if net_create.status_code == 201:
        rand_name = random_string(10)
        net_update = osx.Networking.update_network(net_create.json()['network']['id'], rand_name)
        logger.info("Random name : {} Network details : {}".format(rand_name, net_update.json()))
        osx.Networking.delete_network(net_create.json()['network']['id'])
        assert net_update.status_code == 200 and net_update.json()['network']['name'] == rand_name
    else:
        logger.info("Network create failed")
        pytest.skip("Network create failed")

# Overlay Subnets


def test_list_subnets():
    """
    List subnets and validate
    """
    logger.info("***starting test_list_subnets***")

    subnet_list = osx.Networking.list_subnets()
    logger.info("subnet_list: {}".format(subnet_list.json()))
    assert subnet_list.status_code == 200


def test_subnet_ops():
    """
    Validate subnet operations: create_subnet, show_subnet, delete_subnet
    """
    # TODO add update_subnet to testcase
    logger.info("***starting test_subnet_ops***")

    net_name = random_string(10)
    net_create = osx.Networking.create_network(net_name, admin_state=True, shared=False, external=False)
    logger.info("New network : {}".format(net_create.json()))

    subnet_create = osx.Networking.create_subnet(net_create.json()['network']['id'], '12.12.12.0/24')
    logger.info("New subnet : {}".format(subnet_create.json()))

    show_subnet = osx.Networking.show_subnet(subnet_create.json()['subnet']['id'])
    logger.info("Show subnet : {}".format(subnet_create.json()))

    subnet_delete = osx.Networking.delete_subnet(subnet_create.json()['subnet']['id'])
    osx.Networking.delete_network(net_create.json()['network']['id'])

    assert subnet_create.status_code == 201 and show_subnet.status_code == 200 and subnet_delete.status_code == 204


# vPorts


def test_list_ports():
    """
    List ports and validate
    """
    logger.info("***starting test_list_ports***")

    port_list = osx.Networking.list_ports()
    logger.info("Port list: {}".format(port_list.json()))
    assert port_list.status_code == 200


def test_port_ops():
    # TODO - add test case for create port, show port and delete port operations
    pytest.skip("Incomplete testcase")

# vRouters


def test_list_routers():
    """
    List routers and validate
    """
    logger.info("***starting test_list_routers***")

    router_list = osx.Networking.list_routers()
    logger.info("Router list: {}".format(router_list.json()))
    assert router_list.status_code == 200


def test_router_ops():
    """
    Validate router operations: create_router, show_router, delete_router
    """
    # TODO - add_router_interface and delete_router_interface ops
    logger.info("***starting test_router_ops***")

    router_name = random_string(10)
    router_create = osx.Networking.create_router(router_name)
    logger.info("New router: {}".format(router_create.json()))

    router_show = osx.Networking.show_router(router_create.json()['router']['id'])
    logger.info("Router details: {}".format(router_show.json()))

    router_delete = osx.Networking.delete_router(router_create.json()['router']['id'])

    assert router_create.status_code == 201 and router_show.status_code == 200 and router_delete.status_code == 204
