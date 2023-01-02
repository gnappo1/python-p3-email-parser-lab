import re

class EmailAddressParser:
    def __init__(self, string):
        self.sentence = string
    
    def parse(self):
        # import ipdb; ipdb.set_trace()
        return re.split(r"\s|,\s*", self.sentence)

parser = EmailAddressParser("talk@talk.com john.jones@flatironschool.com alexa@amazon.com")
parser.parse()