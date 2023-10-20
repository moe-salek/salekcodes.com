from salekcodes.settings import *  # noqa
from salekcodes.settings import SECRET_KEY

del SECRET_KEY

SECRET_KEY = 'super_secret_key'  # pragma: allowlist secret
