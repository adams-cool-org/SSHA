### Development process:
Make changes and complete tests on a local dev copy of the repository. When satified with the changes, push to your fork (or main repo if you're Adam):
```
git add .
git commit -m 'commit message here'
git push origin branch_name
```

After pushing your changes, submit a pull request on Github. Adam will review and merge the changes to the master branch.

To update your local version:
```
git remote update

# see what changes exist between your local and the upstream
git diff HEAD origin/master

git pull # merge the changes to your local
```

When satisfied with changes in Adam's dev environment, push to the production environement here
  \\PWDHQR\Data\Planning & Research\Linear Asset Management Program\Water Sewer Projects Initiated\03 GIS Data\Hydraulic Studies\Scripts

by doing:
```
git push production master
```

Note: Git hooks are configured here:
F:\code\sewer_studies\remote
