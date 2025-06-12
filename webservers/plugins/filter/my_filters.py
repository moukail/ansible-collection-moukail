def my_uppercase(value):
    return value.upper()

class FilterModule(object):
    def filters(self):
        return {
            'my_uppercase': my_uppercase,
        }