class filterable:
    def __init__(self, prop: property):
        self.prop: property = prop

    def __get__(self, obj, objtype=None):
        if obj is None:

            class comp:
                def __init__(self, prop_name):
                    self.prop_name = prop_name

                def __lt__(self, other):
                    return (objtype, self.prop_name, "lt", other)

                def __gt__(self, other):
                    return (objtype, self.prop_name, "gt", other)

                def __le__(self, other):
                    return (objtype, self.prop_name, "le", other)

                def __ge__(self, other):
                    return (objtype, self.prop_name, "ge", other)

            return comp(self.prop.fget.__name__)

        return self.prop.fget(obj)

    def __set__(self, obj, value):
        if not self.prop.fset:
            raise AttributeError(f"can't set attribute '{self.prop.fget.__name__}'")

        return self.prop.fset(obj, value)
