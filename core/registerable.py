
class Registerable:

    @classmethod
    def register_cls(cls):
        raise NotImplementedError('register_cls() method not implemented..!')

    @classmethod
    def unregister_cls(cls):
        raise NotImplementedError('unregister_cls() method not implemented..!')
