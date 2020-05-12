import transliterate
from transliterate import get_available_language_codes, translit
import os
from slugify import slugify
import fileinput
import shutil

print(get_available_language_codes())

for filename in os.listdir("static/uploads2"):
    title, ext = os.path.splitext(filename)
    slug = slugify(title)
    #os.rename(os.path.join("static/uploads2", filename), os.path.join("static/uploads2", slug + ext))
    for contentname in os.listdir("content2"):
        with open(os.path.join("content2", contentname)) as file:
            lines = file.readlines()
            for line in lines:
                #print(line)
                line.replace(title, slug)
                #print(line)
                file.close()
    #shutil.copyfile(os.path.join("static/uploads2", filename), os.path.join("static/uploads2", slug))