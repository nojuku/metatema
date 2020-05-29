import transliterate
from transliterate import get_available_language_codes, translit
import os
from slugify import slugify
import fileinput
import shutil
import regex as re
#from fuzzywuzzy import fuzz

def fixNames():

#     for filename in os.listdir("static/uploads"):
#         title, ext = os.path.splitext(filename)
        #slug = title.replace("khoreografiyi", "khoreografii")
#         if "yi" in title:
#             print(title)


        #slug = slugify(title)
        #os.rename(os.path.join("static/uploads", filename), os.path.join("static/uploads", slug + ext))

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
                    nameslug = slugify(name)
                    nametofuzz = nameslug + ext2
                    for filename in os.listdir("static/uploads"):
                        if fuzz.ratio(filename, nametofuzz) > 90:
                            print("MATCH")
                            nameslugcomp = "(" + "/uploads/" + filename + ")"

                        else: nameslugcomp = "(" + "/uploads/" + nametofuzz + ")"

                    nametoreplace = item[1]

                    line = line.replace(nametoreplace, nameslugcomp)

                print(line, end='')

            else:
                print(line, end='')

def fuzzymatch(name):

    for filename in os.listdir("static/uploads"):

        if fuzz.ratio(filename, name) > 60:
            os.rename(os.path.join("static/uploads", filename), os.path.join("static/uploads", name))

        else:
            os.rename(os.path.join("static/uploads", filename), os.path.join("static/uploads", "HEH.jpg"))

if __name__ == "__main__":
    fixNames()