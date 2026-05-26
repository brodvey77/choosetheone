from collections import defaultdict


class Grouper:
    """
    Класс Grouper группирует элементы по ключу, вычисляемому с помощью ключевой функции.
    Поддерживает добавление новых элементов и различные способы доступа к группам.
    """

    def __init__(self, iterable, key):
        """
        Инициализация группировщика.

        :param iterable: итерируемый объект с элементами
        :param key: функция, определяющая ключ группы
        """
        self._key = key  # сохраняем ключевую функцию
        self._groups = defaultdict(list)  # ключ -> список элементов (в порядке добавления)

        # Добавляем все элементы из исходного iterable
        for item in iterable:
            self.add(item)

    def add(self, obj):
        """
        Добавляет объект в соответствующую группу.

        :param obj: добавляемый объект
        """
        group_key = self._key(obj)
        self._groups[group_key].append(obj)

    def group_for(self, obj):
        """
        Возвращает ключ группы, в которую попадёт переданный объект.

        :param obj: объект
        :return: ключ группы
        """
        return self._key(obj)

    def __len__(self):
        """Возвращает количество групп."""
        return len(self._groups)

    def __iter__(self):
        """
        Итерация по группам.
        Каждая группа представлена кортежем: (ключ_группы, список_элементов)
        """
        # Можно использовать items(), порядок групп при этом произвольный (как и требуется)
        for key, elements in self._groups.items():
            yield (key, elements)

    def __contains__(self, key):
        """
        Проверка наличия группы с указанным ключом.
        Поддерживает оператор: `key in grouper`
        """
        return key in self._groups

    def __getitem__(self, key):
        """
        Возвращает список элементов группы по ключу.
        Элементы возвращаются в порядке их добавления.
        """
        if key not in self._groups:
            raise KeyError(key)

        # Возвращаем копию списка для безопасности
        return self._groups[key][:]







class Grouper:
    def __init__(self, iterable, key):
        self._iterable = list(iterable)
        self._key = key
        self._make_groups(self._iterable)

    def _make_groups(self, iterable):
        self._groups = {}
        for item in iterable:
            self.add(item)

    def add(self, item):
        self._groups.setdefault(self._key(item), []).append(item)

    def group_for(self, item):
        return self._key(item)

    def __len__(self):
        return len(self._groups)

    def __iter__(self):
        return iter(self._groups.items())

    def __contains__(self, item):
        return item in self._groups

    def __getitem__(self, key):
        return self._groups[key]