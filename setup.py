from setuptools import setup

setup(name='sentinelpy',
      packages=['sentinelpy'],
      version='0.1.4',
      description='Python Automation Framework',
      author='Kiran Vemuri',
      author_email='kkvemuri@uh.edu',
      url='https://github.com/DreamForgeContrive/sentinelpy',
      download_url='https://github.com/DreamForgeContrive/sentinelpy/tarball/0.1.4',
      keywords=['automation', 'ssh', 'sftp', 'openstack', 'logging', 'cassandra'],
      license='MIT',
      install_reqires=[
          'cassandra-driver',
          'paramiko==1.17.0',
          'requests',
          'pyyaml'],
      classifiers=[],)
