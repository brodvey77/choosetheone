from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    try:
        file = open(filename, mode)
    except Exception as error:
        yield None, error
    else:
        try:
            yield file, None
        finally:
            file.close()


Теперь разберём построчно и очень подробно, потому что здесь есть важная конструкция try / except / else / finally.

1. Импортируем contextmanager
from contextlib import contextmanager

Импортируем декоратор, который позволяет использовать функцию в конструкции:

with safe_open(...) as file:
2. Декорируем функцию
@contextmanager

Теперь safe_open() становится контекстным менеджером.

3. Создаём функцию
def safe_open(filename, mode='r'):

Функция принимает два аргумента:

filename

— имя файла.

И:

mode='r'

— режим открытия.

По умолчанию:

'r'

Например:

safe_open('test.txt')

означает:

open('test.txt', 'r')

Можно передать другой режим:

safe_open('test.txt', 'w')

или:

safe_open('test.txt', 'a')
4. Пытаемся открыть файл
try:
    file = open(filename, mode)

Здесь происходит реальное открытие файла.

Например:

file = open('Ellies_jokes.txt', 'r')

Если файл существует — всё хорошо.

В переменной:

file

находится файловый объект.

5. Что если файл не существует?

Например:

with safe_open('Ellies_jokes_2.txt') as file:

А такого файла нет.

Тогда:

open(filename, mode)

возбудит:

FileNotFoundError

Но нам не нужно, чтобы программа завершилась с ошибкой.

По условию задачи мы должны вернуть:

(None, исключение)

Поэтому:

except Exception as error:

перехватывает исключение.

6. Что находится в error

Если произошло:

FileNotFoundError

то:

error

будет содержать объект этого исключения.

Например, при:

open('Ellies_jokes_2.txt')

примерно:

error

содержит:

[Errno 2] No such file or directory: 'Ellies_jokes_2.txt'
7. yield None, error
yield None, error

Это одна из самых важных строк.

По условию нужно вернуть:

(None, исключение)

Поэтому:

yield None, error

передаёт в as file кортеж:

(None, error)

Например:

(None, FileNotFoundError(...))
8. Как это выглядит для пользователя

Пользователь пишет:

with safe_open('Ellies_jokes_2.txt') as file:
    file, error = file

После:

yield None, error

получается:

file == (None, FileNotFoundError(...))

Затем:

file, error = file

распаковывает кортеж:

file  → None
error → FileNotFoundError(...)

Поэтому:

print(file)

выведет:

None

А:

print(error)

выведет сообщение об ошибке:

[Errno 2] No such file or directory: 'Ellies_jokes_2.txt'
9. Зачем здесь else?

Теперь самая интересная конструкция:

try:
    file = open(filename, mode)
except Exception as error:
    yield None, error
else:

else у try выполняется только если в try не произошло исключение.

То есть:

try
 │
 ├── ошибка ──→ except
 │
 └── нет ошибки ──→ else

В нашем случае это идеально подходит.

Если файл открылся:

else:

и мы должны вернуть:

(file, None)
10. Почему нельзя просто сделать yield file, None после try/except?

Можно было бы написать что-то вроде:

try:
    file = open(filename, mode)
except Exception as error:
    yield None, error

yield file, None

Но это неправильно.

Почему?

Если open() завершился ошибкой, переменная:

file

может вообще не существовать.

А после except мы всё равно дошли бы до:

yield file, None

Поэтому используем else.

11. Успешное открытие

В else:

try:
    yield file, None

Передаём кортеж:

(file, None)

Например:

(
    <_io.TextIOWrapper name='Ellies_jokes.txt' mode='r'>,
    None
)
12. Почему yield, а не return?

Потому что мы используем:

@contextmanager

А функция-контекстный менеджер должна содержать:

yield

yield передаёт значение в:

as file

Поэтому:

yield file, None

означает:

as file получает (file, None)
13. Теперь самая важная часть — finally
finally:
    file.close()

finally выполняется в любом случае.

То есть неважно:

всё прошло нормально;
внутри with возникла ошибка;
пользователь сделал return;
пользователь сделал break и т. д.

Когда управление покидает блок, finally выполнится.

14. Зачем закрывать файл?

По условию:

контекстный менеджер должен закрывать открытый им файл после выполнения кода внутри блока with.

Поэтому:

file.close()

закрывает файл.

Например:

with safe_open('test.txt') as file:
    file, error = file
    print(file.read())

После выхода из with:

file.close()

будет выполнен автоматически.

15. Важный момент: почему finally находится именно здесь?

У нас:

else:
    try:
        yield file, None
    finally:
        file.close()

Это означает:

Файл успешно открылся
        ↓
yield file, None
        ↓
пользователь работает с файлом
        ↓
пользователь закончил
        ↓
finally
        ↓
file.close()

Если внутри пользовательского кода произойдёт ошибка:

with safe_open('test.txt') as file:
    file, error = file
    raise ValueError

finally всё равно выполнится:

file.close()
16. Но почему ошибка пользователя не перехватывается?

Обрати внимание на структуру:

try:
    file = open(filename, mode)
except Exception as error:
    yield None, error
else:
    try:
        yield file, None
    finally:
        file.close()

Первый try/except отвечает только за открытие файла.

То есть:

open(filename, mode)

Если здесь ошибка → except.

А код пользователя находится после yield.

И мы специально не делаем:

except Exception:

вокруг yield file, None.

Поэтому исключение пользователя продолжает распространяться наружу.

Это соответствует условию задачи: нужно обработать ошибку открытия файла, а не любые ошибки внутри with.

17. Полная работа при успешном открытии

Допустим:

with safe_open('Ellies_jokes.txt') as file:
    file, error = file
    print(error)
    print(file.read())

Файл существует.

Происходит:

safe_open()
     ↓
open(filename, 'r')
     ↓
успешно
     ↓
else
     ↓
yield file, None
     ↓
as file
     ↓
file = (файловый объект, None)
     ↓
file, error = file
     ↓
file  = файловый объект
error = None
     ↓
print(error)
     ↓
None
     ↓
file.read()
     ↓
содержимое файла
     ↓
выход из with
     ↓
finally
     ↓
file.close()
18. Работа при отсутствии файла

Теперь:

with safe_open('Ellies_jokes_2.txt') as file:
    file, error = file
    print(file)
    print(error)

Файла нет.

Происходит:

safe_open()
     ↓
open(filename, 'r')
     ↓
FileNotFoundError
     ↓
except Exception as error
     ↓
yield None, error
     ↓
as file
     ↓
file = (None, FileNotFoundError)
     ↓
file, error = file
     ↓
file  = None
error = FileNotFoundError

Получаем:

None
[Errno 2] No such file or directory: 'Ellies_jokes_2.txt'
19. Очень полезная схема для запоминания

Всю задачу можно свести к такой логике:

             safe_open()
                  │
                  ▼
            пытаемся open()
                  │
          ┌───────┴───────┐
          │               │
       ошибка          успешно
          │               │
          ▼               ▼
  yield None, error   yield file, None
          │               │
          │               ▼
          │        пользовательский код
          │               │
          │               ▼
          │          file.close()
          │
          ▼
    продолжаем работу
20. А вот ещё более простой вариант

Можно написать и немного иначе:

from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    try:
        file = open(filename, mode)
    except Exception as error:
        yield None, error
        return

    try:
        yield file, None
    finally:
        file.close()

Здесь после:

yield None, error

мы пишем:

return

чтобы сразу закончить функцию.

Этот вариант тоже корректен.

Мне для обучения больше нравится первый вариант с else, потому что он очень хорошо показывает смысл конструкции:

try:
    # пробуем открыть
except:
    # открытие не удалось
else:
    # открытие удалось
finally:
    # обязательно закрываем
Главное, что нужно вынести из этой задачи

У safe_open есть две совершенно разные ошибки/ситуации:

Ошибка при open()

Например:

open('несуществующий.txt')

Мы её перехватываем:

except Exception as error:
    yield None, error
Ошибка внутри пользовательского with

Например:

with safe_open('test.txt') as file:
    file, error = file
    raise ValueError

Мы её не перехватываем, но файл всё равно закроем благодаря:

finally:
    file.close()

Это очень важное отличие от предыдущей задачи safe_write.

safe_write → перехватывал ошибку пользователя и откатывал файл.

safe_open → перехватывает только ошибку открытия, а открытый файл гарантированно закрывает.


