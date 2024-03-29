"""Basic auth server for Virtual Queue Project."""

from base64 import b64decode
import jwt
import datetime


class AuthenticationServer(object):
    """Class creates a server that is callable."""

    def __init__(self):
        """Initialisation."""
        self.private_key = None  # needs to be set by subclass

    def authenticate(self, username, password):
        """Authenticate username with password.

        returns:
            - on success: dict with keys ['id', 'role', 'lastname',
                'firstname', 'title']
            - on failure: None
        """
        raise NotImplementedError()

    def _basic_auth(self, environ):
        auth = environ.get('HTTP_AUTHORIZATION')
        if not auth:
            print("Missing AUTHORIZATION header")
            return
        scheme, data = auth.split(None, 1)
        if scheme.lower() != 'basic':
            raise Exception("Unsupported authorization scheme: {}".format(scheme.lower()))
        username, password = b64decode(data.encode('utf8')).split(b':', 1)
        payload = self.authenticate(
            username.decode('utf8'),
            password.decode('utf8'),
            environ
        )
        if payload is None:
            return
        payload_keyset = set(('id', 'role', 'lastname', 'firstname', 'title'))
        if not payload_keyset == payload.keys():
            raise KeyError(
                'expected dict with keys "{}" but found "{}"'.format(
                    payload_keyset, set(payload.keys()))
            )
        payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(
            days=3)
        encoded = jwt.encode(payload, self.private_key, algorithm='RS256')
        return encoded

    def __call__(self, environ, start_response):
        """Make server callable."""
        token = self._basic_auth(environ)

        if token is None:
            status = '401 Unauthorized'
            headers = [
                ('Content-type', 'text/plain; charset=utf-8'),
                ('WWW-Authenticate', 'Basic realm="Login Required"')
            ]
            start_response(status, headers)
            return ['401 Unauthorized'.encode('utf-8')]
        else:
            status = '200 OK'
            headers = [('Content-type', 'application/jwt; charset=utf-8')]
            start_response(status, headers)
            return [token]
