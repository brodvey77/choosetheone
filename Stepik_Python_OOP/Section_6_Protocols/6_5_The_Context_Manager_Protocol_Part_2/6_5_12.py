import copy

class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep
        self._copy = None

    def __enter__(self):
        # Сохраняем копию исходного состояния
        if self.deep:
            self._copy = copy.deepcopy(self.data)
        else:
            # Поверхностная копия в зависимости от типа
            if isinstance(self.data, list):
                self._copy = self.data[:]
            elif isinstance(self.data, dict):
                self._copy = self.data.copy()
            elif isinstance(self.data, set):
                self._copy = self.data.copy()
            else:
                # На случай других типов (не предусмотрены условием)
                self._copy = self.data
        # Возвращаем саму коллекцию для работы внутри блока
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Если возникло исключение, откатываем изменения
        if exc_type is not None:
            if isinstance(self.data, list):
                self.data[:] = self._copy
            elif isinstance(self.data, dict):
                self.data.clear()
                self.data.update(self._copy)
            elif isinstance(self.data, set):
                self.data.clear()
                self.data.update(self._copy)
            # Подавляем исключение, как требуется в примерах
            return True
        # Если исключений не было, ничего не делаем





import copy


class Atomic:
    def __init__(self, data, deep=False):
        self.original = data
        self.copy = copy.deepcopy if deep else copy.copy

        if isinstance(data, list):
            self.original_update = self.original.extend
        elif isinstance(data, (set, dict)):
            self.original_update = self.original.update

    def __enter__(self):
        self.data = self.copy(self.original)
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.original.clear()
            self.original_update(self.data)
        return True
