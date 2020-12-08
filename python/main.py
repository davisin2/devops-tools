#!/usr/bin/env python3
import os
import json
import logging
import argparse
from git_handler.git_repo import GitRepo

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                    level=logging.DEBUG)

class PipelineLibrary(object):
    """
    main.py --action <ACTION> [<args>]

    Supported actions are:
       GIT_UPDATE                    Add new files thorugh code
    """
    def __init__(self):

        parser = argparse.ArgumentParser(
            description='Pipeline Python Library',
            usage=PipelineLibrary.__doc__)

        parser.add_argument(
            '--debug',
            help='Print Debug Logs',
            action='store_true')

        parser.add_argument(
            '--action',
            dest='action',
            help="Perform a pipeline action",
            required=True)

        parser.add_argument(
            '--params',
            action="append",
            dest='params',
            nargs="+",
            help="adding optional parameters -e foo=bar")

        args = parser.parse_args()
        self.jparams_dict = {}
        # process all the -e options
        if args.params:
            for item in args.params:
                it = item[0].split('=')
                if args.verbose:
                    logging.info("adding %s to jparams", it[0])
                self.jparams_dict[it[0]] = it[1]

        # process debug
        self.jparams_dict['py-debug'] = True if args.debug else False

        action_to_perform = args.action.lower()
        self.jparams_dict['action'] = action_to_perform

        # is it defined?
        if not hasattr(self, action_to_perform):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        # Use dispatch pattern to invoke method with same name
        # For example:
        # Command: GIT_HISTORY calls member function git_history()
        getattr(self, action_to_perform)()
    
    def git_update(self):
        """
            Check git history for master branch and get commit ID and Merge Date between two commits
        """
        params = {"key1": "value1"}
        repo = GitRepo(params)
        repo.clone("https://github.com/davisin2/devops-tools.git", "devops", branch = "main")
        # repo.clone("git@github.com:davisin2/devops-tools.git", "devops", branch = "main")
        os.chdir(os.getcwd() + "/devops")
        with open("new-file.txt", "w") as f:
            f.write(json.dumps(params))
        repo.commit(["new-file.txt"])
        repo.push()
        # git_history.GitHistory(self.jparams_dict).generate_git_history()

if __name__ == "__main__":
    """
    Main Function - Entry point to the library
    """
    PipelineLibrary()
