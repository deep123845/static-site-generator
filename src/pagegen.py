from html_convert import *


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line[:2] == "# ":
            line = line[2:].strip()
            return line

    raise Exception("Error, No title found")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()

    with open(template_path) as f:
        template = f.read()

    title = extract_title(markdown)
    html_node = markdown_to_html_node(markdown)
    content = html_node.to_html()

    template_with_title = template.replace("{{ Title }}", title)
    page = template_with_title.replace("{{ Content }}", content)

    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')

    with open(dest_path, "w") as f:
        f.write(page)
