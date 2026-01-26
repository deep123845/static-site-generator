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
        new_path = item_path.replace("static", "public", 1)
        if os.path.isfile(item_path):
            shutil.copy(item_path, new_path)
        else:
            os.mkdir(new_path)
            recursive_copy(item_path)


def generate_pages(content_path, template_path):
    items = os.listdir(content_path)

    for item in items:
        item_path = os.path.join(content_path, item)
        new_path = item_path.replace("content", "public", 1)
        new_path = new_path.rsplit(".md", 1)
        new_path = ".html".join(new_path)
        if os.path.isfile(item_path):
            if item[-3:] != ".md":
                continue
            generate_page(item_path, template_path, new_path)
        else:
            os.mkdir(new_path)
            generate_pages(item_path, template_path)


def main():
    basepath = sys.argv[1]
    static_path = os.path.join(basepath, "static")
    content_path = os.path.join(basepath, "content")
    public_path = os.path.join(basepath, "public")
    template_path = os.path.join(basepath, "template.html")
    recursive_copy_static(static_path, public_path)
    generate_pages(content_path, template_path)


main()
