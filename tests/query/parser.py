from satvika.query.parser import Parser
import unittest


class ParserTest(unittest.TestCase):

    def init_parser(self, delimiter):
        return Parser(delimiter)

    def test_parse_query_space_delimiter(self):
        parser = self.init_parser(' ')
        query_parts = ['simple', 'test', 'query']
        query = ' '.join(query_parts)
        self.assertEquals(parser.parse_query(query), query_parts)

    def test_parse_query_slash_delimiter(self):
        parser = self.init_parser('/')
        query_parts = ['simple', 'test', 'query']
        query = '/'.join(query_parts)
        self.assertEquals(parser.parse_query(query), query_parts)
