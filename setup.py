try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='sentinelpy',
      packages=['sentinelpy'],
      version='0.1.1',
      description='Python Automation Framework',
      author='Kiran Vemuri',
      author_email='kkvemuri@uh.edu',
      url='https://github.com/DreamForgeContrive/sentinelpy',
      download_url='https://github.com/DreamForgeContrive/sentinelpy/tarball/0.1.1',
      keywords=['automation', 'ssh', 'sftp', 'openstack', 'logging', 'cassandra'],
      install_reqires=[
          'cassandra-driver',
          'paramiko==1.17.0',
          'requests',
          'pyyaml'],
      classifiers=[],)
