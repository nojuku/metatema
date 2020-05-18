import transliterate
from transliterate import get_available_language_codes, translit
import os
from slugify import slugify
import fileinput
import shutil
import regex as re


def fixNames():

    for filename in os.listdir("static/uploads"):
        title, ext = os.path.splitext(filename)
        slug = slugify(title)
        os.rename(os.path.join("static/uploads", filename), os.path.join("static/uploads", slug + ext))

    for contentname in os.listdir("content"):
        if contentname is ".DS_Store":
            continue

        """ iterate lines """
        for line in fileinput.input(os.path.join("content", contentname), inplace=True):

            regex = re.compile("(\!\[\])(\((?:[^)(]*(?2)?)*+\))")
            """ look for image ref in line """
            resu = re.search(regex, line)
            if resu is not None:
                resu = re.findall(regex, line)
                for item in resu:
                    name = item[1]
                    name = name[10:-1]
                    name, ext2 = os.path.splitext(name)
                    nameslug = "(" + "/uploads/" + slugify(name) + ext2 + ")"
                    nametoreplace = item[1]
                    line = line.replace(nametoreplace, nameslug)

                print(line, end='')

            else:
                print(line, end='')

if __name__ == "__main__":
    fixNames()
