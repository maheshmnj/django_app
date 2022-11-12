### Configuration

- `python3 manage.py makemigrations`
- `python3 manage.py migrate`

Installation

```
pip install -r requirements.txt
```

Run

```
python manage.py runserver
```



### Code Versioning

 Version control files have a notation
  M- Modified (Existing file)
  U- Untracked (New File)

- We should not track any sensitive information like passwords, database, cache, keys, etc.

- `git init`: Initialize a local git repository
- `git add .`: Add all files to the staging area, ready to be committed. Staging means that you are preparing your files to be committed to the repository. To stage a specific file, use `git add <filename>`.
- `git commit -m "commit message"`: Commit the files that are in the staging area with a message describing the changes.
- `git log`: View the commit history (all time) for the current branch. To view the commit history for all branches, use `git log --all`.
- `git status`: View the status of the working directory and the staging area.
- `git remote add <name> <remote repository URL>`: Add a remote repository to the local repository.
- `git remote -v`: View the remote repositories that are connected to the local repository.
- `git remote remove origin`: Remove the remote repository from the local repository.
- `git branch`: View the branches that are available locally.
- `git branch <branch name>`: Creates a new branch. This branch is a copy of the current branch.
- `git checkout <branch name>`: Switch to the specified branch and update the working directory.
- `git checkout -b <branch name>`: Create a new branch and switch to it. (shortform for above two commands)


    ### commit messages
    v0 Initial commit
    |
    |
    |
    v1 created migration
    | Readme change (changes)
    |
    main = master
    |
    |--- feature (remote)
    |    |
    |    |
         updated readme
        