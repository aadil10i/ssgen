class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        node = self.props.items()
        for key, value in node:
            return f"{key}={value} "

    def __repr__(self):
        return f"HTMLNddode({self.tag}, {self.value}, {self.children}, {self.props})"
