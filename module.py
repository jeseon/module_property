class Prop(object):
    def call(self):
        print('moduleProperty')


class Proxy(object):
    def __init__(self, local):
        self.local = local

    def __getattr__(self, name):
        return getattr(self.local(), name)

module_property = Proxy
@module_property
def prop():
    return Prop()
