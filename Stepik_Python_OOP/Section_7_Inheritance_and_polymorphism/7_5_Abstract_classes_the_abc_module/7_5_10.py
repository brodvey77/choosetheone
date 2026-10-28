from abc import ABC, abstractmethod

class Middle(ABC):
    @abstractmethod
    def get_correct_user_votes(self):
        pass

    @abstractmethod
    def get_correct_expert_votes(self):
        pass

    @abstractmethod
    def get_average(self, users=True):
        pass


class Average(Middle):
    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes                   # пользовательские оценки
        self.expert_votes = expert_votes               # оценки критиков

    def get_correct_user_votes(self):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.user_votes if 10 < vote < 90]

    def get_correct_expert_votes(self):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.expert_votes if 5 < vote < 95]

    def get_average(self, users=True):
        """Возвращает среднее арифметическое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = self.get_correct_user_votes()
        else:
            votes = self.get_correct_expert_votes()

        return sum(votes) / len(votes)

class Median(Middle):
    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes                   # пользовательские оценки
        self.expert_votes = expert_votes               # оценки критиков

    def get_correct_user_votes(self):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.user_votes if 10 < vote < 90]

    def get_correct_expert_votes(self):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.expert_votes if 5 < vote < 95]

    def get_average(self, users=True):
        """Возвращает медиану пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = sorted(self.get_correct_user_votes())
        else:
            votes = sorted(self.get_correct_expert_votes())

        return votes[len(votes) // 2]

class Harmonic(Middle):
    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes                   # пользовательские оценки
        self.expert_votes = expert_votes               # оценки критиков

    def get_correct_user_votes(self):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.user_votes if 10 < vote < 90]

    def get_correct_expert_votes(self):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.expert_votes if 5 < vote < 95]

    def get_average(self, users=True):
        """Возвращает среднее гармоническое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = self.get_correct_user_votes()
        else:
            votes = self.get_correct_expert_votes()

        return len(votes) / sum(map(lambda vote: 1 / vote, votes))



print(type(Middle))



from abc import ABC, abstractmethod


class Middle(ABC):
    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes  # пользовательские оценки
        self.expert_votes = expert_votes  # оценки критиков

    def get_correct_user_votes(self, to_sort=False):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        votes = [vote for vote in self.user_votes if 10 < vote < 90]
        return sorted(votes) if to_sort else votes

    def get_correct_expert_votes(self, to_sort=False):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        votes = [vote for vote in self.expert_votes if 5 < vote < 95]
        return sorted(votes) if to_sort else votes

    @abstractmethod
    def get_average(self, users=True, to_sort=False):
        """Возвращает среднее арифметическое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = self.get_correct_user_votes(to_sort)
        else:
            votes = self.get_correct_expert_votes(to_sort)
        return votes


class Average(Middle):
    def get_average(self, users=True):
        votes = super().get_average(users)
        return sum(votes) / len(votes)


class Median(Middle):
    def get_average(self, users=True):
        votes = super().get_average(users, to_sort=True)
        return votes[len(votes) // 2]


class Harmonic(Middle):
    def get_average(self, users=True):
        votes = super().get_average(users)
        return len(votes) / sum(map(lambda vote: 1 / vote, votes))