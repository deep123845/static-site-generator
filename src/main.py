from textnode import *
from htmlnode import *
from text import *
import shutil
import os


def recursive_copy_static():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")

    recursive_copy("static")


def recursive_copy(path):
    items = os.listdir(path)

    for item in items:
        item_path = os.path.join(path, item)
        new_path = item_path.replace("static", "public", 1)
        if os.path.isfile(item_path):
            shutil.copy(item_path, new_path)
        else:
            os.mkdir(new_path)
            recursive_copy(item_path)


def main():
    recursive_copy_static()


main()
