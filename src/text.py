from textnode import *
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.Plain:
            new_nodes.append(old_node)
            continue
        text_segments = old_node.text.split(delimiter)
        if len(text_segments) % 2 == 0:
            raise Exception("Invalid makdown syntax")
        for i in range(len(text_segments)):
            if text_segments[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text_segments[i], TextType.Plain))
            else:
                new_nodes.append(TextNode(text_segments[i], text_type))

    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.Plain:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)

        for image in images:
            image_text = f"![{image[0]}]({image[1]})"
            segments = old_node.text.split(image_text)
            prev_text = segments[0]
            old_node.text = image_text.join(segments[1:])
            if prev_text != "":
                new_nodes.append(TextNode(prev_text, TextType.Plain))
            new_nodes.append(TextNode(image[0], TextType.Image, image[1]))

        if old_node.text != "":
            new_nodes.append(old_node)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.Plain:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)

        for link in links:
            link_text = f"[{link[0]}]({link[1]})"
            segments = old_node.text.split(link_text)
            prev_text = segments[0]
            old_node.text = link_text.join(segments[1:])
            if prev_text != "":
                new_nodes.append(TextNode(prev_text, TextType.Plain))
            new_nodes.append(TextNode(link[0], TextType.Link, link[1]))

        if old_node.text != "":
            new_nodes.append(old_node)

    return new_nodes
