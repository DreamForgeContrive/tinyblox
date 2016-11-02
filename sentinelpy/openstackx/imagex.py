__author__ = "Kiran Vemuri"
__email__ = "kiran_vemuri@adaranetworks.com"
__status__ = "Development"
__maintainer__ = "Kiran Vemuri"

import requests


class Image:

    def __init__(self, url, auth_token):
        self.url = url
        self.auth_token = auth_token
        self.request_headers = {"Content-type": "application/json",
                                "X-Auth-Token": self.auth_token}

    def create_image(self):
        # TODO
        pass

    def show_image_details(self, image_uuid):
        response = requests.get(self.url + "/v2/images/{}".format(image_uuid),
                                headers=self.request_headers)
        return response

    def list_images(self):
        response = requests.get(self.url + "/v2/images",
                                headers=self.request_headers)
        return response

    def delete_image(self, image_uuid):
        response = requests.delete(self.url + "/v2/images/{}".format(image_uuid),
                                   headers=self.request_headers)
        return response

    def deactivate_image(self, image_uuid):
        response = requests.post(self.url + "/v2/images/{}/actions/deactivate".format(image_uuid),
                                 headers=self.request_headers)
        return response

    def reactivate_image(self, image_uuid):
        response = requests.post(self.url + "/v2/images{}/actions/reactivate".format(image_uuid),
                                 headers=self.request_headers)
        return response
