"""
Heap Data Structure
"""

def create_heap(values):

    def create_node(value):
        return {"value": value, "right": None, "left": None}
    
    def _insert(new_node, parent):
        nnd = new_node["value"]
        prt = parent["value"]
        rprt = parent["right"]["value"] if parent["right"] else None
        lprt = parent["left"]["value"] if parent["left"] else None
        if nnd >= prt:
            new_node["left"] = parent
            parent = new_node
        elif lprt is None:
            parent["left"] = new_node
        elif rprt is None:
            parent["right"] = new_node
        elif lprt < nnd and lprt > rprt: 
            new_node["left"] = parent["left"]
            parent["left"] = new_node
        elif rprt < nnd and rprt > lprt: 
            new_node["left"] = parent["right"]
            parent["right"] = new_node
        else:
            _insert(new_node, parent["right"])
        return parent

    def insert(values, root):
        if not values:
            return root

        return insert(values[1:], _insert(create_node(values[0]), root))

    if not values:
        return None

    return insert(values[1:], create_node(values[0]))
