

class Processor(object):

    def process(self, register):
        try:
            self._do_process(register)
        except Exception as e:
            print(str(e), " processor class")
            raise NameError(e)

    def _do_process(self, register):
        """Save the register in DB"""
        raise NotImplementedError()

    @staticmethod
    def _update_instance_with_dict(instance, data, ignore_fields=()):
        for key, value in data.items():
            if key not in ignore_fields:
                setattr(instance, key, value)

