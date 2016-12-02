# TinyBlox - collection of api blocks written in python to help speedup automation

## Modules:
* cassandrax - Facilitate cassandra interactions to a cassandra cluster
* remotex - Facilitate SSH and SFTP interactions to a remote host
* logx - Facilitate writing logs to a specified file on the local host
* ovsx - Facilitate interaction with instances of Open vSwitch deployed on remote hosts
* openstackx - Facilitate OpenStack interactions
    * computex
    * identityx
    * imagex
    * networkingx
* toolx - collection of generic tools
    * random_string - Random string generation with combination of lower and upper case alphabets, digits, special characters and white space
    * random_ip - random IP address object generation with CIDR bit and subnet address generation

## Installation:

Please install the following dependencies:
`pip install cassandra-driver paramiko==1.17.0 requests pyyaml`

or you could copy the Requirements.txt file and run:
`pip install -r Requirements.txt`

To install sentinelpy:
`pip install tinyblox`


## Sample:

### openstackx

* Starting a session
```
from tinyblox.openstackx import OSSession
osx = OSSession('Keystone_IP', 'Keystone_User', 'Keystone_Password')
```

* Compute - sample usage
```
# list_servers
>>> osx.Compute.list_servers().json()
{u'servers': []}
```

* Networking - sample usage
```
# list networks and subnets
>>> osx.Networking.list_networks().json()
{u'networks': []}
>>> osx.Networking.list_subnets().json()
{u'subnets': []}
```

* Image - sample usage
```
# list existing images
>>> osx.Image.list_images().json()
{u'images': [{u'status': u'active', u'schema': u'/v2/schemas/image', u'name': u'ubuntu', u'tags': [], u'container_format': u'bare', u'created_at': u'2016-08-22T18:10:40Z', u'disk_format': u'qcow2', u'updated_at': u'2016-11-10T23:42:15Z', u'visibility': u'public', u'id': u'6bc6dab8-e907-4b4e-8a3a-44ce4ec95e63', u'owner': u'9a7a62c2389d42e1a9941f915360f4de', u'protected': False, u'min_ram': 0, u'file': u'/v2/images/6bc6dab8-e907-4b4e-8a3a-44ce4ec95e63/file', u'checksum': u'0f630dc54fe212b28dedf2a662a74198', u'min_disk': 0, u'virtual_size': None, u'self': u'/v2/images/6bc6dab8-e907-4b4e-8a3a-44ce4ec95e63', u'size': 260375040}, {u'status': u'active', u'schema': u'/v2/schemas/image', u'name': u'cirros', u'tags': [], u'container_format': u'bare', u'created_at': u'2016-08-04T00:00:43Z', u'disk_format': u'qcow2', u'updated_at': u'2016-08-04T00:00:43Z', u'visibility': u'public', u'id': u'ffeb4798-5495-43d7-a57c-72355befd1af', u'owner': u'9a7a62c2389d42e1a9941f915360f4de', u'protected': False, u'min_ram': 0, u'file': u'/v2/images/ffeb4798-5495-43d7-a57c-72355befd1af/file', u'checksum': u'ee1eca47dc88f4879d8a229cc70a07c6', u'min_disk': 0, u'virtual_size': None, u'self': u'/v2/images/ffeb4798-5495-43d7-a57c-72355befd1af', u'size': 13287936}], u'first': u'/v2/images', u'schema': u'/v2/schemas/images'}
```

### toolx

* Generate a random string
```
>>> from tinyblox import toolx
>>> rand_str = toolx.random_string(str_len=20, special_char=True, white_space=False)
>>> rand_str
'NhD=WXbzs8+QGpqk=7y4'
```

* Generate random ip and cidr
```
>>> random_ip = toolx.random_ip(ip_class='B')
>>> random_ip
IPNetwork('185.38.123.250/29')
>>> random_ip.cidr
IPNetwork('185.38.123.248/29')
>>> str(random_ip.cidr)
'185.38.123.248/29'
```

### logx

* log to a specific file
```
>>> from tinyblox import logx
>>> logfile = logx.Log('./test_log_file.log')
>>> logfile
<tinyblox.logx.Log instance at 0x10d7c0fc8>
>>> loghandler = logfile.log_handler()
>>> loghandler
<logging.Logger object at 0x10e819950>
>>> loghandler.info('Writing test log into log file')
```

* Checking the log written to file
```
> cat ./test_log_file.log
2016-12-02 15:04:53,390 - tinyblox.logx - INFO - Writing test log into log file
```

### cassandrax

* Establish a session to a single cassandra node
```
>>> from tinyblox import cassandrax
>>> csx = cassandrax.Cassandra(['<cassandra_node_IP>'])
```

* Establish a session to a cluster of cassandra nodes
```
>>> from tinyblox import cassandrax
>>> csx = cassandrax.Cassandra(['cassandra_node1_ip','cassandra_node2_ip','cassandra_node3_ip'])
```

* Fetch existing keyspaces
```
>>> csx.fetch_keyspaces()
[u'system_auth', u'system_distributed', u'system', u'system_traces']
```

* Run query without explicitly binding to a specific keyspace
```
>>> csx.run_query(in_query='select keyspace_name from system.schema_keyspaces')
[{u'keyspace_name': u'system_auth'}, {u'keyspace_name': u'system_distributed'}, {u'keyspace_name': u'system'}, {u'keyspace_name': u'system_traces'}]
```

* Run query against a specific keyspace
```
>>> csx.run_query(in_query='select keyspace_name from schema_keyspaces', keyspace='system')
[{u'keyspace_name': u'system_auth'}, {u'keyspace_name': u'system_distributed'}, {u'keyspace_name': u'system'}, {u'keyspace_name': u'system_traces'}]
```

### ovsx

* Connect to remote machine running Open vSwitch and interact
```
>>> from tinyblox import ovsx
>>> ovs_session = ovsx.Ovs('<machine IP>','<machine username>','<machine password>')
>>> ovs_session.get_controller('br0')
{'retval': 0, 'err': [], 'out': [u'tcp:2.2.2.1:6633\n']}
>>> ovs_session.get_protocols('br0')
{'retval': 0, 'err': [], 'out': [u'["OpenFlow10", "OpenFlow11", "OpenFlow12", "OpenFlow13"]\n']}
```

### remotex

* Create a session object to connect to a remote machine
```
>>> from tinyblox import remotex
>>> rconn = remotex.Connection('<remote_machine_ip>',22, '<remote_machine_username', '<remote_machine_password')
>>> rconn
<tinyblox.remotex.Connection instance at 0x10e8807a0>
```

* Execute a command on a remote machine without sudo
```
>>> rconn.execute(command='pwd')
{'retval': 0, 'err': [], 'out': [u'/root\n']}
```

* Execute a command on a remote machine with sudo
```
>>> rconn.execute(command='uname -r', sudo=True)
{'retval': 0, 'err': [], 'out': [u'4.2.0-42-generic\n']}
```

* Upload a file(sftp put) to the remote server
```
rconn.upload(local_path='./test_log_file.log',remote_path='/tmp/test_log_file.log')
```

* Download a file(sftp get) from the remote server
```
rconn.download(remote_path='/tmp/test_log_file.log',local_path='./test_log1.log')
```
