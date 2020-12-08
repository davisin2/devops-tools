import os
import shutil
import git
import sys
import logging
import traceback

try:
    from pipeline_utils.pipebase import PipeBase
except ModuleNotFoundError:
    sys.path.append("..")
    from pipeline_utils.pipebase import PipeBase

logging.basicConfig(format='%(asctime)s [%(levelname)s] [{}] %(message)s'.format(
    os.path.basename(__file__)), level=logging.INFO)

class GitRepo(PipeBase):

    def __init__(self, params):
        PipeBase.__init__(self, params)
        if self.debug:
            logging.getLogger().setLevel(logging.DEBUG)
        self.params = params

    def clone(self, repo_name, local_repo_name=None, branch="master"):
        self.repo_name = repo_name

        print(branch)
        print(repo_name)
        print(local_repo_name)

        if local_repo_name is None:
            self.local_repo_name = repo_name
        else:
            self.local_repo_name = local_repo_name

        self.branch = branch
        try:
            if os.path.isdir(self.local_repo_name):
                logging.info(f"Removing {self.local_repo_name} from %s" % os.getcwd())
                shutil.rmtree(self.local_repo_name, ignore_errors=True)

            logging.info(f"Cloning {self.local_repo_name} in %s" % os.getcwd())
            self.repo = git.Repo.clone_from(self.repo_name, self.local_repo_name, branch = self.branch)
            return self.repo
        except Exception as e:
            logging.error("Unable to clone repo: " + str(e))
            traceback.print_exc()

    def checkout(self, branch: str):
        try:
            if branch in self.repo.git.branch():
                print(f"Branch {branch} Exist")
            else:
                self.repo.git.branch(branch)

            self.repo.git.checkout(branch)
            print(self.repo.git.branch())
            self.branch = branch
            logging.info(f"Branch switched to {branch}")
        except Exception as e:
            logging.error("Unable to clone repo: " + str(e))
            traceback.print_exc()

    def status(self):
        print(self.repo.git.status())
        return self.repo.git.status()

    def commit(self, list_of_changed_files: list, message="Commiting through Jenkins"):
        for file in list_of_changed_files:
            # print(self.repo.git.add(file ))
            logging.info(f"Commiting file {file}")
            self.repo.git.add(file)
            self.repo.git.commit( m=message)

    def push(self):
        logging.info(f"Pushing to origin from branch {self.branch}")
        self.repo.git.push("origin", self.branch)
