import uuid
import json
import bin.utils.html_utils.html_utils as html_u


class HtmlElement:
    def __init__(
        self,
        html: str = "",
        id: str = "",
        name: str = "",
        attributes: dict = {},
        parent: object | None = None,
        children: list = [],
    ):
        self.uuid = str(uuid.uuid4())
        self.parent = parent
        if html:
            self._parse(html)
            return
        self.id = id
        self.name = name
        self.attributes = attributes
        self.children = children

    def find_element_by_id(self, id: str, pile: list = []) -> object | None:
        if self.id == id:
            return self
        if self.uuid in pile:
            return
        pile.append(self.uuid)

        result = None
        if self.parent:
            result = self.parent.find_element_by_id(id, pile)
        if self.children and not result:
            for child in self.children:
                result = (
                    None if type(child) == str else child.find_element_by_id(id, pile)
                )
                if result:
                    break
        return result

    def __str__(self) -> str:
        children_html = ""
        children = self.children if self.children else []
        for child in children:
            if type(child) is str:
                children_html += child
            else:
                children_html += str(child)
            children_html += "\n"
        children_html = children_html.strip()
        attributes = (
            json.dumps(self.attributes, separators=(" ", "="))
            .replace("{", " ")
            .replace("}", "")
            .replace("'", "<single_quote>")
            .replace('\\"', "<quote>")
            .replace('"', "")
            .replace("<single_quote>", "'")
            .replace("<quote>", '"')
            .rstrip()
        )
        end = "/>" if children_html == "" else ">"
        block_end = "" if children_html == "" else f"</{self.name}>"
        return f"<{self.name}{attributes}{end}{children_html}{block_end}".strip()

    def _parse(self, html: str):
        html = html.replace("\n", " ")
        element = html_u.get_element(html)
        self.name = html_u.get_name(element)
        self.attributes = html_u.get_attributes(element)
        self.id = self.attributes.get("id")
        if self.id:
            self.id = self.id.replace('"', "")
        children_html = html_u.get_child(html, name=self.name)
        if children_html == None:
            self.children = None
        else:
            self.children = []
            self._add_children(children_html)

    def _add_children(self, html: str):
        if html == "":
            return
        try:
            element = html_u.get_element(html)
            name = html_u.get_name(element)
            self.children.append(HtmlElement(html=html, parent=self))
            self._add_children(html_u.remove_element(html, name))
        except AttributeError as e:
            self.children.append(html)
