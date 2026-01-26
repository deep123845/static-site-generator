from textnode import *
from htmlnode import *
from text import *
import shutil
import os
from pagegen import *


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


def generate_pages(path):
    template = "template.html"
    items = os.listdir(path)

    for item in items:
        item_path = os.path.join(path, item)
        new_path = item_path.replace("content", "public", 1)
        new_path = new_path.rsplit(".md", 1)
        new_path = ".html".join(new_path)
        if os.path.isfile(item_path):
            if item[-3:] != ".md":
                continue
            generate_page(item_path, template, new_path)
        else:
            os.mkdir(new_path)
            generate_pages(item_path)


def main():
    recursive_copy_static()
    generate_pages("content")


main()
