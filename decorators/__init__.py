__all__ = ['decoratorsSpecial', 'decoratorsBasic']

if __name__ == "__main__":
    print('import')


class Dolm():
    def __inti__(self, prop):
        self.prop = prop

    def __getattribute__(self, name):
        val = super().__getattribute__(name)
        return val + ' Dolm'

d = Dolm("Niklas")
print(d.prop)