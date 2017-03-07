## Development process:
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

## Testing Procedure
Note: This testing process needs to be streamlined and automated.
1. Backup your development .mxd and geodatabase
2. Copy and paste the production mxd and geodatabase to your dev environment.
3. Point the StudiedSewers and DrainageArea layers to your dev environment. Remove all the DA Indicies layers from the map except one (the project id to be tested on).
4. Point the Small_Sewer_Calcs script tools to the scripts in your dev environment.
5. In the map, select the studied sewers with the Project_ID that will be tested on (I've tested previously on Project_ID: 40935). Copy the rows and paste into this spreadhseet in the existing_ss tab:
  - L:\Water Sewer Projects Initiated\03 GIS Data\Hydraulic Studies\Resources\ToolTests\test_tables.xlsx
6. Do the same for the DA Index layer for you particular test Project_ID (paste into the existing_da_index tab).
7. Delete the selected StudiedSewers from the map.
8. Rerun the tools:
   - Associated Sewers to DAs
   - assign the TC_Path and StudySewer tags appropriately in the newly associated sewers.
   - Run H&H Calcs
9. Select the newly associated sewers and paste into the testing spreadhseet in the new_ss tab. Check if there are discrepancies.
10. Copy the DA Index table from the map and paste into the spreadsheet in the new_da_index tab. Check if there are discrepancies.
11. If there are no discrepancies, approve the changes.
