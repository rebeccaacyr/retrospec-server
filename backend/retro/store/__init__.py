import uuid

from retro.chain.node_chain import ColumnHeaderNode, ContentNode, BoardNode


class Store(object):
    node_types = {BoardNode.NODE_TYPE: BoardNode,
                  ContentNode.NODE_TYPE: ContentNode,
                  ColumnHeaderNode.NODE_TYPE: ColumnHeaderNode}

    def next_node_id(self):
        return str(uuid.uuid4())

    def transaction(self, board_id, func):
        raise NotImplementedError

#    def keys(self, board):
#        raise NotImplementedError

    def create_board(self, board_node):
        raise NotImplementedError

    def get_node(self, node_id):
        raise NotImplementedError

    def node_from_dict(self, node_dict):
        cls = self.node_types.get(node_dict['type'])
        if not cls:
            raise Exception("Unknown node type: %s" % node_dict['type'])

        d = node_dict.copy()
        d.pop('type')
        return cls(**d)
