class Line:
    def __init__(self, content, name, number):
        self.content = content
        self.name = name
        self.number = number

    def get_location(self) -> str:
        return f'{self.name}, line {self.number + 1}'

    def __repr__(self):
        return str(self.__dict__)
