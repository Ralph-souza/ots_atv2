class Category:
    __id: int
    __name: str
    __id_mother: int

    def set_id(self, id: int) -> None:
        self.__id = int(id)

    def get_id(self) -> int:
        return self.__id

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_id_mother(self, id_mother: int) -> None:
        self.__id_mother = id_mother

    def get_id_mother(self) -> int:
        return self.__id_mother

    def __str__(self):
        return f'''
                    - ID: {self.get_id()}
                    - Name: {self.get_name()}
                    - ID_Mother: 
                '''


class SubCategory(Category):

    def __init__(self, id: int, name: str, parent: Category):
        self.parent = parent
        super().__init__(id, name)

    def get_parent(self) -> Category:
        return self.parent

    def set_parent(self, parent: Category):
        self.parent = parent

    def get_parent_name(self) -> str:
        return self.get_parent().get_name()

    def __str__(self):
        return f'''
                    - ID: {self.get_id()}
                    - Name: {self.get_name()}
                    - Mother: {self.get_parent_name()}
                '''
