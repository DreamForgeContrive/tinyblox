__author__ = "Kiran Vemuri"
__email__ = "kkvemuri@uh.edu"
__status__ = "Development"
__maintainer__ = "Kiran Vemuri"

from identityx import Identity
from computex import Compute
from networkingx import Networking
from imagex import Image


class Openstack:

    def __init__(self, openstack_ip, username, password, domain='default'):
        """

        :param openstack_ip: <str> IP address of the OpenStack control node running keystone service
        :param username: <str> openstack login username
        :param password: <str> openstack login password
        :param domain: <str> name of the domain. defaults to 'default'
        """
        self.openstack_ip = openstack_ip
        self.username = username
        self.password = password
        self.domain = domain
        self.identity_url = 'http://' + openstack_ip + ':5000/v3/'
        self.compute_url = None
        self.image_url = None
        self.networking_url = None

        self.Identity = Identity(self.identity_url, self.username, self.password, domain='default')
        self.scoped_token = self.Identity.fetch_scoped_token()
        self.auth_token = self.scoped_token.headers['X-Subject-Token']
        self.catalog = self.scoped_token.json()['token']['catalog']
        self.fetch_endpoint_urls()

        self.Compute = Compute(self.compute_url, self.auth_token)
        self.Networking = Networking(self.networking_url, self.auth_token)
        self.Image = Image(self.image_url, self.auth_token)

    def fetch_endpoint_urls(self):
        for endpoint in self.catalog:
            if endpoint['name'] == 'nova':
                for detail in endpoint['endpoints']:
                    if detail['interface'] == 'public':
                        self.compute_url = detail['url']
            elif endpoint['name'] == 'glance':
                for detail in endpoint['endpoints']:
                    if detail['interface'] == 'public':
                        self.image_url = detail['url']
            elif endpoint['name'] == 'neutron':
                for detail in endpoint['endpoints']:
                    if detail['interface'] == 'public':
                        self.networking_url = detail['url']
            elif endpoint['name'] == 'glance':
                for detail in endpoint['endpoints']:
                    if detail['interface'] == 'public':
                        self.image_url = detail['url']
