__author__ = "Kiran Vemuri"
__email__ = "kiran_vemuri@adaranetworks.com"
__status__ = "Development"
__maintainer__ = "Kiran Vemuri"

import requests
import json


class Identity:
    """
    Interface to interact with keystone service using REST
    """
    def __init__(self, url, username, password, domain='default'):
        self.url = url
        self.username = username
        self.password = password
        self.domain = domain
        self.unscoped_token = self.fetch_unscoped_token()
        self.user_id = self.unscoped_token.json()['token']['user']['id']
        self.project_json = self.fetch_user_projects().json()

    # Authentication and Token Management

    def fetch_unscoped_token(self):
        """
        Fetch token from keystone server
        :return: <tuple> token_json, auth_json from response returned by tokens request
        """

        request_data = json.dumps({"auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": self.username,
                        "domain": {
                            "name": "Default"
                        },
                        "password": self.password
                    }
                }
            }
        }
        })
        request_headers = {"Content-type": "application/json"}
        response = requests.post(self.url + "auth/tokens",
                                 data=request_data,
                                 headers=request_headers)

        return response

    def fetch_scoped_token(self):
        """
        Fetch service endpoints from the keystone server
        :return: json response returned by endpoints request
        """
        request_data = json.dumps({"auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": self.username,
                        "domain": {
                            "name": "Default"
                        },
                        "password": self.password
                    }
                }
            },
            "scope": {
                "project": {
                    "id": self.project_json['projects'][0]['id']
                }
            }
        }
        })
        request_headers = {"Content-type": "application/json"}
        response = requests.post(self.url + "/auth/tokens",
                                 headers=request_headers,
                                 data=request_data)
        return response

    # Users
    def fetch_user_projects(self):
        """
        Fetch project details
        :return: json response returned by projects request
        """
        request_headers = {
            "Content-type": "application/json",
            "X-Auth-Token": self.unscoped_token.headers['X-Subject-Token']
        }
        response = requests.get(self.url + "/users/" + self.user_id + "/projects",
                                headers=request_headers)

        return response