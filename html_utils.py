import re


def get_element(html: str, name: str = "([a-zA-Z][a-zA-Z0-9]*)") -> tuple:
    return re.search(rf"<{name}\b[^>]*>", html).group()


def remove_element(html: str, name: str = "([a-zA-Z][a-zA-Z0-9]*)") -> tuple:
    if re.match(rf"<{name}\b[^\/>]*\/>", html):
        return re.sub(rf"<{name}\b[^\/>]*\/>", "", html, 1)
    element = get_element(html, name)
    children = get_child(html, name=name)
    return (
        html.replace(element, "", 1)
        .replace(children, "", 1)
        .replace(f"</{name}>", "", 1)
        .strip()
    )


def get_name(html: str) -> str:
    return re.search(r"<([a-zA-Z][a-zA-Z0-9]*)\b", html).group().replace("<", "")


def get_id(html: str) -> str:
    id = re.search(r'id=[\'"]([^\'"]+)[\'"]', html)
    if not id:
        return ""
    return id.group()


def get_attributes(html: str) -> dict:
    attribs = re.search(r"<([a-zA-Z][a-zA-Z0-9]*)\b([^>]*)>", html).group(2).strip()
    attribs_list = re.split(r"(?:[^ ,]+|, )+", attribs)
    attributes = {}
    for attr in attribs_list:
        if attr != "" and attr != "/":
            attr_div = attr.strip().replace("=", ":", 1).split(":")
            key = attr_div[0]
            value = attr_div[1]
            attributes[key] = value
    return attributes


def get_child(html: str, *, name: str) -> str:
    element = get_element(html, name=name)
    if re.match(rf"<{name}\b[^\/>]*\/>", element):
        return None
    children = re.findall(rf"<\/?{name}\b[^>]*>", html)
    children.pop(0)
    element_end = 1
    count = 0
    for element_tag in children:
        if re.match(r"<\/", element_tag):
            element_end -= 1
        else:
            element_end += 1
            count += 1
        if element_end < 1:
            break
    for _ in range(count):
        html = re.sub(rf"<\/{name}>", "<remove>", html, 1)
    (end_index, _) = re.search(rf"<\/{name}>", html).span()
    html = re.sub("<remove>", f"</{name}>", html)
    end_index = end_index - ((5 - len(name)) * count)
    child = html[:end_index].replace(element, "").strip()
    return child


def set_attributes(html: str, *, id: str, attributes: dict) -> str:
    pass


def add_attributes(html: str, *, id: str, attributes: dict) -> str:
    pass


def set_child(html: str, *, id: str, child: str) -> str:
    pass


def add_child(html: str, *, id: str, child: str) -> str:
    pass
