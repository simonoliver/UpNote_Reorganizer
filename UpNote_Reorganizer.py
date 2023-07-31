import os
import shutil
import frontmatter #pip install python-frontmatter
import re

baseDir = "Notes"
## Pattern is  (Files/XXX)
regex = r"(?:[!]\[(?P<caption>.*?)\])\((?P<image>.*?)(?P<description>\".*?\")?\)"

if not os.path.isdir(baseDir):
    os.mkdir(baseDir)


for file in os.listdir(os.getcwd()):
    if file.endswith(".md"):

        note = frontmatter.load(file)

        ## Copy any images
        post_content=note.content
       
        if 'categories' in note:
            for c in note['categories']:

                directory = c.replace(" / ","/")

                dest = os.path.join(baseDir, directory)

                if not os.path.isdir(dest):
                    os.makedirs(dest)
        
                ## shutil.copy(file, dest)
        else:
            dest=baseDir   
            ## shutil.copy(file, baseDir)

        print("Processing note "+file)
        # Find all file matches
        matches = re.finditer(regex, post_content, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            image_path = match.group(2)
            # Only local refs
            if "Files" in image_path:
                from urllib.parse import unquote
                converted_path=unquote(image_path)
                print("Found image "+converted_path+" in file "+ file+"  moving to "+dest)
            
                # Copy to destination
                shutil.copy(converted_path, dest)
            
        # Remove file path ref
        post_content=post_content.replace("Files/","")


        fullpath= os.path.join(dest, file)
        outfile = open(fullpath, "w", encoding="utf-8")
        outfile.write(post_content)
    