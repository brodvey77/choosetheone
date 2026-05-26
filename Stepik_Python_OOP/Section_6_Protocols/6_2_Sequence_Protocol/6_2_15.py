class HistoryDict:
    """
    Класс HistoryDict — словарь с историей изменений значений по каждому ключу.
    Запоминает все значения, которые когда-либо присваивались ключу.
    """

    def __init__(self, data=None):
        """
        Инициализация HistoryDict.

        :param data: начальный словарь (если None — пустой)
        """
        if data is None:
            data = {}

        # Текущее состояние словаря
        self._data = dict(data)  # копия, чтобы не зависеть от исходного словаря

        # История значений: ключ -> список всех значений в хронологическом порядке
        self._history = {}

        # Заполняем начальную историю
        for key, value in self._data.items():
            self._history[key] = [value]

    def __getitem__(self, key):
        """Получение значения по ключу."""
        return self._data[key]

    def __setitem__(self, key, value):
        """
        Установка значения по ключу.
        Если ключ новый — создаём историю.
        Если ключ существует — добавляем новое значение в историю.
        """
        self._data[key] = value

        if key in self._history:
            self._history[key].append(value)
        else:
            self._history[key] = [value]

    def __delitem__(self, key):
        """
        Удаление ключа.
        Удаляется как текущее значение, так и вся история ключа.
        """
        del self._data[key]
        del self._history[key]

    def __len__(self):
        """Возвращает количество текущих элементов."""
        return len(self._data)

    def __iter__(self):
        """Итерация по ключам (как у обычного dict)."""
        return iter(self._data)

    def keys(self):
        """Возвращает итерируемый объект с ключами."""
        return self._data.keys()

    def values(self):
        """Возвращает итерируемый объект со значениями."""
        return self._data.values()

    def items(self):
        """Возвращает итерируемый объект с парами (ключ, значение)."""
        return self._data.items()

    def history(self, key):
        """
        Возвращает историю значений для указанного ключа.
        Если ключ отсутствует — возвращает пустой список.

        :param key: ключ
        :return: список всех значений, которые когда-либо были у ключа
        """
        return self._history.get(key, []).copy()

    def all_history(self):
        """
        Возвращает полную историю для всех текущих ключей.

        :return: словарь {ключ: [все_значения]}
        """
        # Возвращаем копию, чтобы внешний код не мог изменить историю
        return {key: history.copy() for key, history in self._history.items()}



historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['ducks'] = 100
print(historydict.history('ducks'))
print(historydict.history('cats'))
print(historydict.history('dogs'))



