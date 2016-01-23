Version control so simple your mom can do it.

The movtiation behind this attempt at creating a version control method is to create a very, very simple way to track the history of files. The work-flow of pyver is something I do anyway when working on something simple that uses binary files, especially ones that are linked through the software that is required to read them (eg CAD designs). I will create multiple directories, eg v1, v2 and copy the entire contents of my in-progress files in it that I want to preserve the history.

The basic operation of this program goes like this
1) create some files
2) run pyver and make a revision
3) make as many revisions as you want
4) if you want to revert back to an older revision, checkout an older one or copy the files from ./.pyver/vx and put them in your current diretory

Notes
* all the files in the directory are stored when a revision is made. Although this is inefficient for large files, it keeps it dead simple and users can always just copy and paste their revision somewhere else. There is no learning curve with syntax.

Criteria for design
* cannot rename files to track versions. This accomplishes this by putting the files in different directories
* Can be used over a network drive. Does not require a central server. 
* Be OS agnostic (written in Python)
* know when the changes were made, with a comment and who did it