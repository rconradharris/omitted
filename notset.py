class _NotSetType(object):
    """
    NotSet represents a do-not-care value, useful when None won't work because
    it's a valid value.
    """
    __slots__ = tuple()

    def __repr__(self):
        return 'NotSet'


NotSet = _NotSetType()  # Singleton
