'''
parsers.py

Author:     Yujeonja <hardboiled65@gmail.com>
Created:    2019. 11. 02. 15:32
Copyright (c) 2019 Yujeonja. All rights reserved.

Parsers module for specific types.
'''

class BaseParser:
    def __init__(self):
        self._parse_function = None

    def _remove_comment(line):
        '''Remove comment of given line'''
        splitted = line.split('#')
        return splitted[0].rstrip()

    def parse(self, data):
        return self._parse_function(data)


class SimpleKeyValueParser(BaseParser):
    def __init__(self):
        super().__init__()

        self._parse_function = SimpleKeyValueParser.parse_function

    def parse_function(data):
        '''e.g. PropertyAliases.txt'''
        d = {}
        lines = data.split('\n')
        for line in lines:
            line = BaseParser._remove_comment(line)
            if line.strip() == '':
                continue
            strings = tuple(map(lambda x: x.strip(), line.split(';')))
            k = strings[0]
            v = strings[1]
            d[k] = v
        return d


class GroupedSimpleKeyValueParser(SimpleKeyValueParser):
    def __init__(self):
        super().__init__()

        self._parse_function = self.parse_function

    @staticmethod
    def parse_function(data):
        '''e.g. PropertyValueAliases.txt'''
        d = {}
        lines = data.split('\n')
        for line in lines:
            line = BaseParser._remove_comment(line)
            if line.strip() == '':
                continue
            strings = tuple(map(lambda x: x.strip(), line.split(';')))
            g = strings[0]
            k = strings[1]
            v = strings[2]
            if g not in d.keys():
                d[g] = {}
            d[g][k] = v
        return d

class GroupedRangeParser(BaseParser):
    def __init__(self):
        super().__init__()

        self._parse_function = self.parse_function

    @staticmethod
    def parse_function(data):
        '''e.g. PropList.txt'''
        d = {}
        lines = data.split('\n')
        for line in lines:
            line = BaseParser._remove_comment(line)
            if line.strip() == '':
                continue
            strings = tuple(map(lambda x: x.strip(), line.split(';')))
            k = strings[0]
            v = strings[1]
            if v not in d.keys():
                d[v] = []
            d[v].append(k)
        return d


class RangeValueParser(BaseParser):
    def __init__(self):
        super().__init__()

        self._parse_function = self.parse_function

    @staticmethod
    def parse_function(data):
        '''e.g. Blocks.txt'''
        d = {}
        lines = data.split('\n')
        for line in lines:
            line = BaseParser._remove_comment(line)
            if line.strip() == '':
                continue
            strings = tuple(map(lambda x: x.strip(), line.split(';')))
            k = strings[0]
            v = strings[1]
            d[k] = v
        return d


class UnicodeDataParser(BaseParser):
    def __init__(self):
        super().__init__()

        self._parse_function = self.parse_function

    @staticmethod
    def parse_function(data):
        '''Only for UnicodeData.txt'''
        d = {}
        lines = data.split('\n')
        for line in lines:
            line = BaseParser._remove_comment(line)
            if line.strip() == '':
                continue
            strings = tuple(map(lambda x: x.strip(), line.split(';')))
            props = {
                'na': strings[1],
                'gc': strings[2],
                'ccc': strings[3],
                'bc': strings[4],
                'dm': strings[5], # Also contains dt.
            }
            d[strings[0]] = props
        return d

