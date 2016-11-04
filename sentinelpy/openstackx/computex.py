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

    def create_server(self,
                      server_name,
                      image_uuid,
                      flavor_uuid,
                      availability_zone,
                      network_uuid,
                      security_group = None):
        """
        Create a server
        :param server_name: <str> name for the server that is being created
        :param image_uuid: <uuid> UUID of the image that is to be used to boot the server
        :param flavor_uuid: <uuid> UUID of the flavor for the instance
        :param availability_zone: <str> availability_zone to boot the instance in
        :param network_uuid: <uuid> UUID of the network to be associated to the server
        :param security_group: <str> name of the security group to be associated with the instance
        :return: response object returned by the create_Server request
        """
        request_data = json.dumps({
            "server": {
                "name": server_name,
                "imageRef": image_uuid,
                "flavorRef": flavor_uuid,
                "availability_zone": availability_zone,
                "networks": [{
                    "uuid": network_uuid
                }]
            }
        })
        response = requests.post(self.url + "/servers",
                                 headers=self.request_headers,
                                 data=request_data)
        return response

    def create_multiple_servers(self):
        pass
        # TODO

    def show_server(self, server_uuid):
        """
        Show server details
        :param server_uuid: <uuid> UUID of the server
        :return: response object returned by the show_server request
        """
        response = requests.get(self.url + "/servers/{}".format(server_uuid),
                                headers=self.request_headers)
        return response

    def delete_server(self, server_uuid):
        """
        Delete a server
        :param server_uuid: <uuid> UUID of the server
        :return: response object returned by the delete_server request
        """
        response = requests.delete(self.url + "/servers/{}".format(server_uuid),
                                   headers=self.request_headers)
        return response

    def reboot_server(self):
        pass
        # TODO

    def live_migrate_server(self):
        pass
        # TODO

    # Floating IP

    def associate_floatingip(self):
        pass
        # TODO

    def disassociate_floatingip(self):
        pass
        # TODO

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

    def create_flavor(self, flavor_name, ram, vcpu_count, disk):
        """
        Create a flavor
        :param flavor_name: <str> name for the flavor that is being created
        :param ram: <int> RAM Size
        :param vcpu_count: <int> Number of vcpu's
        :param disk: <int> Size of the disk
        :return: response object returned by the create_flavor request
        """
        request_data = json.dumps({
            "flavor": {
                "name": flavor_name,
                "ram": ram,
                "vcpus": vcpu_count,
                "disk": disk
            }
        })
        response = requests.post(self.url + "/flavors",
                                 headers=self.request_headers,
                                 data=request_data)
        return response

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
        """
        Get availability zone info
        :return: response object returned by the availability_zone request
        """
        response = requests.get(self.url + "/os-availability-zone",
                                headers=self.request_headers)
        return response

    def get_availability_zone_info_details(self):
        """
        Get availability zone info with details
        :return: response object returned by the availability_zone_detail request
        """
        response = requests.get(self.url + "/os-availability-zone/detail",
                                headers=self.request_headers)
        return response

    # Ping instances

    def ping_all(self):
        """
        Ping all instances and list the instances that are alive
        :return: response object returned by the ping_all request
        """
        response = requests.get(self.url + "/os-fping",
                                headers=self.request_headers)
        return response

    def ping_instance(self, instance_uuid):
        """
        Ping a specific instance and return the status of the instance
        :param instance_uuid: <uuid> UUID of the instance to be pinged
        :return: response object returned by the ping_instance request
        """
        response = requests.get(self.url + "/os-fping/{}".format(instance_uuid),
                                headers=self.request_headers)
        return response

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
        # TODO

    def show_security_group(self):
        pass
        # TODO

    def update_security_group(self):
        pass
        # TODO

    def delete_security_group(self):
        pass
        # TODO

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
        # TODO

    def delete_security_group_rule(self):
        pass
        # TODO
