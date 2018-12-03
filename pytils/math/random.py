from uuid import uuid4

from ..net import localhost


def uid(namespace=None):
    if namespace is None:
        return str(uuid4())
    return '%s-%s-%s' % (localhost(), namespace, uuid4())
