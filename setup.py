from setuptools import setup

setup(name='sentinelpy',
      version='0.1',
      description='Python Automation Framework',
      author='Kiran Vemuri',
      author_email='kkvemuri@uh.edu',
      packages=['sqaSentinel'],
      install_requires=['cassandra-driver','paramiko', 'requests'],
      zip_safe=False)

