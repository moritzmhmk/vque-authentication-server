from distutils.core import setup
setup(
    name='vque_authentication_server',
    version='0.0.1',
    description='authentication server for the virtual queueing system',
    author='Moritz Kanemeier',
    author_email='kanemeier@uni-muenster.de',
    url='https://github.com/moritzmhmk/vque-authentication-server',
    py_modules=['server'],
    install_requires=[
        'PyJWT>=1.5.3',
        'cryptography>=2.1.4',
    ],
    license='MIT',
    classifiers=[],
)
