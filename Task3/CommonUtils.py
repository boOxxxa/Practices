class CommonUtils:
    @staticmethod
    def translit_to_eng(s):
        translit_dict = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
            'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '',
            'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': '-'
        }

        s = s.lower()
        slug = ''
        for char in s:
            if char in translit_dict:
                slug += translit_dict[char]
            else:
                slug += char
        return slug

    @staticmethod
    def save_to_file(file_name, slug_list):
        with open(file_name, 'w') as file:
            for slug in slug_list:
                file.write(slug + '\n')