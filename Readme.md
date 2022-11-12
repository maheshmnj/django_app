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

    ### commit messages
    0 Initial commit
    |

    |
    |