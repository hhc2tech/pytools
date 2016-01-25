# pyver 
Version control so simple your mom can do it.

The movtiation behind this attempt at creating a version control method is to create a very, very simple way to track the history of files. The work-flow of pyver is something I do anyway when working on something simple that uses binary files, especially ones that are linked through the software that is required to read them (eg CAD designs). I will create multiple directories, eg v1, v2 and copy the entire contents of my in-progress files in it that I want to preserve the history.

## The basic operation of this program goes like this
1) create some files
2) run pyver and make a revision
3) make as many revisions as you want
4) if you want to revert back to an older revision, checkout an older one or copy the files from .pyver/folderversion and put them in your current diretory

### Criteria for design
* It is unacceptable to rename files to track versions. This accomplishes this by putting the files in different directories and keep your current file with the desired, persistent filename
* Can be used over a network drive. Does not require a central server. 
* Be OS agnostic (written in Python)
* know when the changes were made, with a comment and who did it

# Tutorial
To get started, lets do a quick demo in windows. In your current directory, open a command line with ```shift+right_click``` and select ```Open command window here```

Now type 
```
pv
```

Done. We have created a pyver repository and made a backup of all the files in our current directory in an archive naming year-month-day-hour-minute-second. Anytime we need to make another backup, just repeat the last step.

There are a few built in commands to interrogate the repository. The first is log, which shows the contents of a text file that keeps track of the commits that are made
```
pv log
```

The next is tree, which shows all the files in the repo.
```
pv tree
```


We also have some flags we can use to customize our commits. This commit adds only the files file1.txt and file2.docx and adds a comment. Note-none of the flag inputs can have spaces, so files are seperated by ```|``` and comments are written without spaces using ```-```

```
pv -f file1.txt|file2.docx -c added-figures-to-docx-and-updated-text-with-numbers
```


I used pyinstaller to build my own windows executable
```
pyinstaller pyver.py --onefile
```