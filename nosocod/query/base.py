from nosocod.query.parser import Parser


class Base(object):

    DELIMITER = '/'

    query = ''

    parser = None

    def __init__(self, query):
        self.query = query
        self.parser = self._init_parser()

    def _init_parser(self):
        return Parser(self.DELIMITER)

    def get_chunks(self):
        return self._parse_chunks(self.query)

    def _parse_chunks(self, query):
        return self.parser.parse_query(query)

    @staticmethod
    def build_query(nodes):
        path = ''
        for node in nodes:
            value = node.value
            if value:
                path += Base.DELIMITER
                path += node.value
        return Base(path)
