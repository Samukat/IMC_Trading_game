How to commit:
    1. git add .
    2. git commit -m "Add existing file"
    3. git push origin branch-name OR git push -u origin main

How to pull:
    1. Git stash
    2. git pull 'remote_name' 'branch_name'

How to retreive stash:
    - View code in terminal: 
        1. git stash list
        2. git stash apply

        optional. git stash show -p stash@{NUMBER SEEN IN STASH LIST}


        to remove all stash:
        git stash clear