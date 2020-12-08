
class PipeBase(object):
    """
    Pipeline Base Class for common routines for every command.
    """

    def __init__(self, params):
        self.debug = False
        if 'py-debug' in params.keys():
            self.debug = params['py-debug']

    def fprint(self, msg):
        """ print with automatic flush (for Jenkins console sake) """
        print(msg, flush=True)
