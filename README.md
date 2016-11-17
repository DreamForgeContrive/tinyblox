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

To install sentinelpy:
`pip install tinyblox`