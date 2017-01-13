__author__ = "Kiran Vemuri"
__email__ = "kkvemuri@uh.edu"
__status__ = "Development"
__maintainer__ = "Kiran Vemuri"

from remotex import Connection


class Ovs:
    """
    Class to facilitate interactions with ovs running on a remote server
    """
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.port = 22
        self.conn = None

    def _rconn_open(self):
        self.conn = Connection(self.host, self.port, self.username, self.password)

    def _rconn_close(self):
        self.conn.close()
        self.conn = None

    def _rconn_handle(foo):
        def conn_exec_close(inst, *args, **kwargs):
            inst._rconn_open()
            res = foo(inst, *args, **kwargs)
            inst._rconn_close()
            return res
        return conn_exec_close

    # OVS-VSCTL commands
    @_rconn_handle
    def list_bridges(self):
        """
        Method to list all the bridges on the node
        :return: output of list-br command
        """
        return self.conn.execute('ovs-vsctl list-br')

    @_rconn_handle
    def get_controller(self, br):
        """
        Method to get the current controller of a bridge
        :param br: <str> bridge name
        :return output of the get-controller command
        """
        return self.conn.execute('ovs-vsctl get-controller {}'.format(br), sudo=True)

    @_rconn_handle
    def set_controller(self, br, ctrl_ip):
        """
        Method to set a controller to a bridge
        :param br: <str> bridge name
        :param ctrl_ip: <str> IP address of the controller
        :return output of the set-controller command
        """
        return self.conn.execute('ovs-vsctl set-controller {} tcp:{}:6633'.format(br, ctrl_ip), sudo=True)

    @_rconn_handle
    def del_controller(self, br):
        """
        Method to delete the current controller on a bridge
        :param br: <str> bridge name
        :return output of the del-controller command
        """
        return self.conn.execute('ovs-vsctl del-controller {}'.format(br), sudo=True)

    @_rconn_handle
    def set_protocols(self, br, protocol_str="OpenFlow13"):
        """
        Method to set protocols on a bridge
        :param br: <str> bridge name
        :param protocol_str: <str> string with protocols separated by ','
        :return output of the set protocols command
        """
        return self.conn.execute('ovs-vsctl set bridge {} protocols={}'.format(br, protocol_str), sudo=True)

    @_rconn_handle
    def get_protocols(self, br):
        """
        Method to get current protocols on the bridge
        :param br: <str> bridge name
        :return output of the get protocols command
        """
        return self.conn.execute('ovs-vsctl get bridge {} protocols'.format(br), sudo=True)

    @_rconn_handle
    def add_bridge(self, br):
        """
        Method to add a new ovs bridge
        :param br: <str> bridge name
        :return output of the add bridge command
        """
        return self.conn.execute('ovs-vsctl add-br {}'.format(br), sudo=True)

    @_rconn_handle
    def del_bridge(self, br):
        """
        Method to delete an ovs bridge
        :param br: <str> bridge name
        :return output of the del bridge command
        """
        return self.conn.execute('ovs-vsctl del-br {}'.format(br), sudo=True)

    # OVS-OFCTL Commands
    @_rconn_handle
    def mod_port(self, br, port, state, protocol_str='OpenFlow13'):
        """
        Method to modify port state on a bridge
        :param br: <str> bridge name
        :param port: <str> port number/name
        :param state: <str> up/down
        :param protocol_str: <str> protocols separated by ','. default= OpenFlow13
        :return output of mod-port command
        """
        return self.conn.execute('ovs-ofctl -O {} mod-port {} {} {}'.format(protocol_str, br, port, state), sudo=True)

    @_rconn_handle
    def dump_flows(self, br, protocol_str="OpenFlow13"):
        """
        Method to fetch current flows on the specified bridge
        :param br: <str> bridge name
        :param protocol_str: <str> protocols separated by ',' ; default = OpenFlow13
        :return: output of dump-flows command
        """
        return self.conn.execute('ovs-ofctl -O {} dump-flows {}'.format(protocol_str, br), sudo=True)

    @_rconn_handle
    def dump_groups(self, br, protocol_str="OpenFlow13"):
        """
        Method to fetch current groups on the specified bridge
        :param br: <str> bridge name
        :param protocol_str: <str> protocols separated by ',' ; default = OpenFlow13
        :return: output of dump-groups command
        """
        return self.conn.execute('ovs-ofctl -O {} dump-groups {}'.format(protocol_str, br), sudo=True)

    @_rconn_handle
    def show_switch(self, br, protocol_str="OpenFlow13"):
        """
        Method to get the details of a specified bridge
        :param br: <str> bridge name
        :param protocol_str: <str> protocols separated by ',' ; default = OpenFlow13
        :return: output of show switch command
        """
        return self.conn.execute('ovs-ofctl -O {} show {}'.format(protocol_str, br), sudo=True)
