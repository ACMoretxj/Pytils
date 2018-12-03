def readonly(obj, name, value):
    func_name: str = '__readonly_%s' % name
    setattr(obj, func_name, value)
    setattr(obj.__class__, name, property(lambda x: x.__dict__[func_name]()))
