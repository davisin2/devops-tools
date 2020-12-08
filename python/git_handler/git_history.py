import re
import os
import sys
import logging

try:
    from pipeline_utils.pipebase import PipeBase
except ModuleNotFoundError:
    sys.path.append("..")
    from pipeline_utils.pipebase import PipeBase

logging.basicConfig(format='%(asctime)s [%(levelname)s] [{}] %(message)s'.format(
    os.path.basename(__file__)), level=logging.INFO)


class GitHistory(PipeBase):

    def __init__(self, params):
        PipeBase.__init__(self, params)
        if self.debug:
            logging.getLogger().setLevel(logging.DEBUG)

    def generate_git_history(self):
        pass