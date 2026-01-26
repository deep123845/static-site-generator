from textnode import *
from htmlnode import *
from text import *
import shutil
import os
from pagegen import *
import sys


def recursive_copy_static(static_path, public_path):
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)

    recursive_copy(static_path)


def recursive_copy(path):
    items = os.listdir(path)

    for item in items:
        item_path = os.path.join(path, item)
        new_path = item_path.replace("static", "docs", 1)
        if os.path.isfile(item_path):
            shutil.copy(item_path, new_path)
        else:
            os.mkdir(new_path)
            recursive_copy(item_path)


def generate_pages(content_path, template_path, basepath):
    items = os.listdir(content_path)

    for item in items:
        item_path = os.path.join(content_path, item)
        new_path = item_path.replace("content", "docs", 1)
        new_path = new_path.rsplit(".md", 1)
        new_path = ".html".join(new_path)
        if os.path.isfile(item_path):
            if item[-3:] != ".md":
                continue
            generate_page(item_path, template_path, new_path, basepath)
        else:
            os.mkdir(new_path)
            generate_pages(item_path, template_path, basepath)


def main():
    basepath = "./"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    recursive_copy_static("./static", "./docs")
    generate_pages("./content", "./template.html", basepath)


main()
