__author__ = "Kiran Vemuri"
__email__ = "kkvemuri@uh.edu"
__status__ = "Development"
__maintainer__ = "Kiran Vemuri"

import requests
import json


class Compute:
    """
    Interface to interact with nova service using REST
    """

    def __init__(self, url, auth_token):
        """

        :param url: <str> URL to reach the compute service
        :param auth_token: <str> auth_token to authorize the compute requests
        """
        self.url = url
        self.auth_token = auth_token
        self.request_headers = {"Content-type": "application/json",
                                "X-Auth-Token": self.auth_token}

    # Servers

    def list_servers(self):
        """
        List existing servers(instances)
        :return: response object returned by the list_servers request
        """
        response = requests.get(self.url + "/servers",
                                headers=self.request_headers)
        return response

    def create_server(self):
        pass

    def create_multiple_servers(self):
        pass

    def show_server(self, server_uuid):
        response = requests.get(self.url + "/servers/{}".format(server_uuid),
                                headers=self.request_headers)
        return response

    def delete_server(self, server_uuid):
        """
        Delete a server
        :param server_uuid: <uuid> UUID of the server
        :return:
        """
        response = requests.delete(self.url + "/servers/{}".format(server_uuid),
                                   headers=self.request_headers)
        return response

    def reboot_server(self):
        pass

    def live_migrate_server(self):
        pass

    # Floating IP

    def associate_floatingip(self):
        pass

    def disassociate_floatingip(self):
        pass

    # Flavors

    def list_flavors(self):
        """
        List existing flavors
        :return: response object returned by the list_flavors request
        """
        response = requests.get(self.url + "/flavors",
                                headers=self.request_headers)
        return response

    def list_flavors_detail(self):
        """
        List flavors with details
        :return: response object returned by the list_flavors_detail request
        """
        response = requests.get(self.url + "/flavors/detail",
                                headers=self.request_headers)
        return response

    def create_flavor(self):
        pass

    def delete_flavor(self, flavor_uuid):
        """
        Delete a flavor
        :param flavor_uuid: <uuid> UUID of the flavor that is to be deleted
        :return: response object returned by the delete_flavor request
        """
        response = requests.delete(self.url + "/flavors/{}".format(flavor_uuid),
                                   headers=self.request_headers)
        return response

    def show_flavor_details(self, flavor_uuid):
        """
        Show flavor details
        :param flavor_uuid: <uuid> UUID of the flavor whose details are being requested
        :return: response object returned by the show_flavor_details request
        """
        response = requests.get(self.url + "/flavors/{}".format(flavor_uuid),
                                headers=self.request_headers)
        return response

    # Key pairs

    def list_keypairs(self):
        """
        List existing keypairs
        :return: response object returned by the list_keypairs request
        """
        response = requests.get(self.url + "/os-keypairs",
                                headers=self.request_headers)
        return response

    def delete_keypair(self, keypair_name):
        """
        Delete a keypair
        :param keypair_name: <str> name of the keypair that is to be created
        :return: response object returned by the delete_keypair request
        """
        response = requests.delete(self.url + "/os-keypairs/{}".format(keypair_name),
                                   headers=self.request_headers)
        return response

    def create_import_keypair(self, keypair_name, public_key=None):
        """
        Create/Import a keypair
        :param keypair_name: <str> Name for the keypair that is being created
        :param public_key: <str> public_key for the keypair that is being imported. Default = None
        :return: response object returned by the create_import_keypair request
        """
        if public_key:
            request_data = json.dumps({
                "keypair": {
                    "name": keypair_name,
                    "public_key": public_key
                }
            })
        else:
            request_data = json.dumps({
                "keypair": {
                    "name": keypair_name
                }
            })

        response = requests.post(self.url + "/os-keypairs",
                                 headers=self.request_headers,
                                 data=request_data)
        return response

    # Images

    def list_images(self):
        """
        List existing images
        :return: response object returned by the list_images request
        """
        response = requests.get(self.url + "/images",
                                headers=self.request_headers)
        return response

    def list_images_detail(self):
        """
        List images with details
        :return: response object returned by the list_images_detail request
        """
        response = requests.get(self.url + "/images/detail",
                                headers=self.request_headers)
        return response

    def show_image_details(self, image_uuid):
        """
        Show image details
        :param image_uuid: <uuid> UUID of the image whose details are being requested
        :return: response object returned by the show_image_details request
        """
        response = requests.get(self.url + "/images/{}".format(image_uuid),
                                headers=self.request_headers)
        return response

    def delete_image(self, image_uuid):
        """
        Delete image
        :param image_uuid: <uuid> UUID of the image that is to be deleted
        :return: response object returned by the delete_image request
        """
        response = requests.delete(self.url + "/images/{}".format(image_uuid),
                                   headers=self.request_headers)
        return response

    # Availability zones

    def get_availability_zone_info(self):
        pass

    def get_availability_zone_info_details(self):
        pass

    # Ping instances

    def ping_all(self):
        pass

    def ping_instance(self):
        pass

    # Security groups

    def list_secutity_groups(self):
        """
        List existing security groups
        :return: response object returned by the list_security_groups request
        """
        response = requests.get(self.url + "/os-security-groups",
                                headers=self.request_headers)
        return response

    def create_security_group(self):
        pass

    def show_security_group(self):
        pass

    def update_security_group(self):
        pass

    def delete_security_group(self):
        pass

    # Default security group rules | Not currently supported by neutron driver

    """
    def list_default_security_group_rules(self):
        request_headers = {"Content-type": "application/json",
                           "X-Auth-Token": self.auth_token}
        response = requests.get(self.url + "/os-security-group-default-rules",
                                headers=request_headers)
        return response.json()

    def create_default_security_group_rule(self):
        pass

    def delete_default_security_group_rule(self):
        pass

    """
    # Rules for security group

    def create_security_group_rule(self):
        pass

    def delete_security_group_rule(self):
        pass
