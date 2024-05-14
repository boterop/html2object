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
        self.parent = parent
        if html:
            self._parse(html)
            return
        self.id = id
        self.name = name
        self.attributes = attributes
        self.children = children

    def _parse(self, html: str):
        element = html_u.get_element(html)
        self.name = html_u.get_name(element)
        self.attributes = html_u.get_attributes(element)
        self.id = self.attributes.get("id")
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
        except Exception as e:
            self.children.append(html)
