# Rope

# to do:
# - insert
# - delete
# - substring
# - concatenation

def to_rope(string):
    return Rope(string)

class Rope:
    def __init__(self, string):
        self.string = string
        
    def __str__(self):
        return "abc"


assert str(to_rope("abc")) == "abc"