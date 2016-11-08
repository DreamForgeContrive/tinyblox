from sentinelpy.openstackx import openstackx
from sentinelpy.logx import Log
import pytest
import random
import string

osx = openstackx.Openstack('10.11.86.3', 'admin', 'password')
logging = Log('./unit_test.log')
logger = logging.log_handler()

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

def test_create_network():
    """
    Create a network and validate [admin_state=True, shared=False, external=False]
    """
    logger.info("***starting test_create_network***")

    net_name = "TestNetwork0"
    net_create = osx.Networking.create_network(net_name, admin_state=True, shared=False, external=False)
    logger.info("New network : {}".format(net_create.json()))
    net_delete = osx.Networking.delete_network(net_create.json()['network']['id'])
    assert net_create.status_code == 201 and net_delete.status_code == 204


def test_create_network_shared():
    """
    Create a network and validate [admin_state=True, shared=True, external=False]
    """
    logger.info("***starting test_create_network_shared***")

    net_name = "TestNetwork1"
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

    net_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(10))
    net_create = osx.Networking.create_network(net_name, admin_state=True, shared=False, external=False)
    logger.info("Net network : {}".format(net_create.json()))

    if net_create.status_code == 201:
        rand_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(10))
        net_update = osx.Networking.update_network(net_create.json()['network']['id'], rand_name)
        logger.info("Random name : {} Network details : {}".format(rand_name,net_update.json()))
        osx.Networking.delete_network(net_create.json()['network']['id'])
        assert net_update.status_code == 200 and net_update.json()['network']['name'] == rand_name
    else:
        logger.info("Network create failed")
        pytest.skip("Network create failed")


