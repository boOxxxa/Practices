from CommonUtils import CommonUtils
class SlugConvertor():
    def __init__(self):
        self.file_name=input("Введите имя файла ")
        self.slug_list=[]
        self.run()
    def run(self):
        while True:
            name = input("Введите имя (для завершения введите пустую строку): ")
            if not name:
                break
            else:
                slug = CommonUtils.translit_to_eng(name)
                self.slug_list.append(slug)
        CommonUtils.save_to_file(self.file_name, self.slug_list)

    @property
    def file_name(self) -> str:
        return self.__file_name

    @file_name.setter
    def file_name(self, new_file_name: str):
        self.__file_name = new_file_name

    @property
    def slug_list(self) -> list:
        return self.__slug_list

    @slug_list.setter
    def slug_list(self, new_slug_list: list):
        self.__slug_list = new_slug_list