class CustomMeta(type):
    def __new__(cls, name, bases, attrs):
        custom_name = f'Custom{name}'
        custom_attrs = {
            key if key.startswith('__') and key.endswith('__') else f'custom_{key}': value
            for key, value in attrs.items()
        }

        return type.__new__(cls, custom_name, bases, custom_attrs)
