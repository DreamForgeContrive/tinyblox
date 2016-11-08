from setuptools import setup

requires = [
    'cassandra-driver',
    'paramiko==1.17.0',
    'requests',
    'pyyaml'
]


packages = [
    'sentinelpy',
    'sentinelpy.openstackx',
]

setup(name='sentinelpy',
      packages=packages,
      version='0.1.6',
      description='Python Automation Framework',
      author='Kiran Vemuri',
      author_email='kkvemuri@uh.edu',
      url='https://github.com/DreamForgeContrive/sentinelpy',
      download_url='https://github.com/DreamForgeContrive/sentinelpy/tarball/0.1.6',
      keywords=['automation', 'ssh', 'sftp', 'openstack', 'logging', 'cassandra'],
      license='MIT',
      install_requires=requires,
      setup_requires=requires,
      classifiers=[],)
