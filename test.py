class Dolm():
    def __init__(self, prop, alter):
        self.prop = prop
        self.alter = alter

    def __getattribute__(self, name):
        val = super().__getattribute__(name)
        if name == "prop":
            return val + ' Dolm'
        return val

d = Dolm("Niklas", 8)
print(d.prop)
print(d.alter)
