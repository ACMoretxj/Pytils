class IPTransformException(ValueError):
    def __init__(self, *args, **kwargs):
        if 'ip' in kwargs:
            self.ip = kwargs['ip']
        super().__init__(*args, **kwargs)
