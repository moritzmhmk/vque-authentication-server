"""Basic auth server for Virtual Queue Project.

This is the setup file.
"""

from setuptools import setup

version = '0.0.2'
url = 'https://github.com/moritzmhmk/vque-authentication-server'
# download_url = '{}/archive/v{}.tar.gz'.format(url, version)

setup(
    name='vque-authentication-server',
    py_modules=['vque_authentication_server'],
    version=version,
    description='authentication server for the virtual queueing system',
    author='Moritz Kanemeier',
    author_email='kanemeier@uni-muenster.de',
    url=url,
    install_requires=[
        'PyJWT>=1.5.3',
        'cryptography>=2.1.4',
    ],
    license='MIT',
    classifiers=[],
)
