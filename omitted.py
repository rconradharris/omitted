class _OmittedType(object):
    """
    Omitted represents a Do Not Care value, useful when None won't work
    because it's a valid value.
    """
    __slots__ = tuple()

    def __repr__(self):
        return 'Omitted'


Omitted = _OmittedType()  # Singleton


def truthy(x):
    return bool(x) and x is not Omitted
