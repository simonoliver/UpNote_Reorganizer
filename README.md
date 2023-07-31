# UpNote To Obsidian
Put an Upnote export back into a folder heirarchy, and move images to the folder matching the Markdown Note. Forked from [Adams141's UpNoteReorganizer](https://github.com/adams141/UpNote_Reorganizer) to be a bit more Obsidian Specific.

### Need
When you export your notes in markdown format, they are all in one folder. This puts them back into the folder structure you had in UpNote. *note: if you have a note in multiple notebooks, you will end up with multiple copies*

### Requirements
uses [python-frontmatter](https://github.com/eyeseast/python-frontmatter)

    pip install python-frontmatter

### Usage
- From upnote, export all notes to a folder.  
- Put UpNote_Reorganizer.py in that folder  
- Run `python UpNote_Reorganizer.py`
