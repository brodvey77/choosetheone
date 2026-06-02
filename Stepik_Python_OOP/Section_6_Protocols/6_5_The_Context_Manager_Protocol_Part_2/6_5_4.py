class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True






print('start')

with SuppressAll():
    print('Python generation!')

print('end')
