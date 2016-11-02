__author__ = "Kiran Vemuri"
__email__ = "kiran_vemuri@adaranetworks.com"
__status__ = "Development"
__maintainer__ = "Kiran Vemuri"

from identityx import Identity
from computex import Compute
from networkingx import Networking


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

        self.Compute = None
        self.Networking = None
        self.enable_networking()
        self.enable_compute()

    def enable_networking(self):
        self.Networking = Networking(self.networking_url, self.auth_token)

    def enable_compute(self):
        self.Compute = Compute(self.compute_url, self.auth_token)

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


if __name__ == '__main__':
    osx = Openstack('10.10.86.3', 'admin', 'password')
    # print osx.Compute.list_servers()
    # print "====\n===="
    # print osx.Compute.list_flavors()
    # print "====\n===="
    # print osx.Compute.list_images()
    # print "====\n===="
    # print osx.Compute.list_keypairs()
    # print "====\n===="
    # print osx.Compute.list_secutity_groups()
    # print "====\n===="
    print osx.Networking.list_networks().json()
    # print "====\n===="
    # print osx.Networking.list_subnets()
    # print "====\n===="
    # print osx.Networking.list_ports()
    # print "====\n===="
    # print osx.Networking.list_routers()

    print "====\n===="
    new_net = osx.Networking.create_network('test_net')
    print new_net.json()
    print osx.Networking.show_network(new_net.json()['network']['id']).json()
    new_sub = osx.Networking.create_subnet(new_net.json()['network']['id'], cidr="2.2.2.0/24")
    print new_sub
    print new_sub.json()
    print osx.Networking.delete_subnet(new_sub.json()['subnet']['id'])
    print osx.Networking.delete_network(new_net.json()['network']['id'])
    print osx.Networking.create_router('test_router').json()



