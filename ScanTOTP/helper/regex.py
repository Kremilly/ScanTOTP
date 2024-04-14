#!/usr/bin/python3

import re

class Regex:
    
    @classmethod
    def get(cls, data, regex, group=1):
        match = re.search(regex, data)
        return match.group(group)
