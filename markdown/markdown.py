import re


def parse(markdown):
    lines = markdown.split("\n")
    result = ""
    in_list = False  # True when the first line with list (* ) is matched

    for line in lines:
        # Can check for multiple headings(h1, h2,...) by looping through all markdown heading syntax ("#" * h)
        for h in range(6, 0, -1):
            if re.match(f"{'#' * h} (.+)", line):
                line = f"<h{h}>{line[h+1:]}</h{h}>"

        # re.match() returns None if no match found, so no need to check if its value is None explicitely in if statements
        line_has_list = re.match(r"\* (.*)", line)
        if line_has_list:
            line = f"<li>{line_has_list.group(1)}</li>"
            if not in_list:
                # Excecuted only when the first list element is found so we know we are inside <ul>
                in_list = True
                line = f"<ul>{line}"
        else:
            if in_list:
                # Line that is not a list element found, means the list we were inside till last line has ended
                result += "</ul>"
                in_list = False

        line_has_bold = re.match("(.*)__(.*)__(.*)", line)
        if line_has_bold:
            line = f"{line_has_bold.group(1)}<strong>{line_has_bold.group(2)}</strong>{line_has_bold.group(3)}"

        line_has_italic = re.match("(.*)_(.*)_(.*)", line)
        if line_has_italic:
            line = f"{line_has_italic.group(1)}<em>{line_has_italic.group(2)}</em>{line_has_italic.group(3)}"

        # If till now the line has not been parsed, means it must be a paragraph
        already_parsed = re.match("<h|<ul|<li", line)
        if not already_parsed:
            line = f"<p>{line}</p>"

        result += line
    if in_list:
        result += "</ul>"  # If last line in lines was a list element, append "</ul>" as we are still not out of list
    return result
