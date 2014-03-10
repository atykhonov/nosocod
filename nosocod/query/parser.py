class Parser(object):

    delimiter = ''

    def __init__(self, delimiter=' '):
        self.delimiter = delimiter

    def parse_query(self, query):
        return query.split(self.delimiter)
