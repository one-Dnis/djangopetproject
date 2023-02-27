class Tools:
    @staticmethod
    def create_slug(slug: str):
        # если символа нет в словаре он пропустит его

        lowered_slug = str(slug)
        lowered_slug = lowered_slug.lower()
        new_slug = ''

        SLUG_DICTIONARY = {
            '0': '0',
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
            '-': '-',
            ' ': '-',
            'a': 'a',
            'b': 'b',
            'c': 'c',
            'd': 'd',
            'e': 'e',
            'f': 'f',
            'g': 'g',
            'h': 'h',
            'i': 'i',
            'j': 'j',
            'k': 'k',
            'l': 'l',
            'm': 'm',
            'n': 'n',
            'o': 'o',
            'p': 'p',
            'q': 'q',
            's': 's',
            't': 't',
            'u': 'u',
            'v': 'v',
            'w': 'w',
            'x': 'x',
            'y': 'y',
            'z': 'z',
            'а': 'a',
            'б': 'b',
            'в': 'v',
            'г': 'g',
            'д': 'd',
            'е': 'e',
            'ё': 'yo',
            'ж': 'zh',
            'з': 'z',
            'и': 'i',
            'й': 'y',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'ф': 'f',
            'х': 'h',
            'ц': 'ts',
            'ч': 'ch',
            'ш': 'sh',
            'щ': 'shch',
            'ъ': '',
            'ы': 'i',
            'ь': '',
            'э': 'e',
            'ю': 'yu',
            'я': 'ya',
        }

        for i in lowered_slug:
            if i in SLUG_DICTIONARY.keys():
                new_slug += (SLUG_DICTIONARY.get(i))

        return new_slug
