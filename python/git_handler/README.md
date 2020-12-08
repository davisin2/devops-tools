This is **personal code**, used for refernece      

- git_repo -> Used for doing all git operations through Python using GitPython, install gitpython before using this      
```
pip install gitpython
```
- git_history -> To get Git history through Python     


# Personal Notes:    
## Process to rename default  branch     

1. Rename your local branch.     
```     
git branch -m master main     
```
2. Push renamed branch upstream and set remote tracking branch.     
```
git push -u origin main     
```
3. Log into the upstream repository host (GitHub, GitLab, Bitbucket, etc.) and change the "default branch".     

4. Delete the old branch upstream.     
```
git push origin --delete master     
```
5. Update the upstream remote's HEAD.     
```
git remote set-head origin -a     
```

Full article: https://dev.to/rhymu8354/git-renaming-the-master-branch-137b