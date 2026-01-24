def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line[:2] == "# ":
            line = line[2:].strip()
            return line

    raise Exception("Error, No title found")
