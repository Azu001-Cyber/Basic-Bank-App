# non-default param
def app(name: str, age: int) -> str:
    return f'{name} {age}'


user = app('sybil', 23)
print(user)


# default param
def app(name: str = 'Sybil', age: int = 21) -> str:
    return f'{name} {age}'


user = app('Jennifer', 18)
print(user)


# args param -> tuple object


#kwargs param -> dict

def app(*args: tuple) -> tuple:
    return args


user = app('Sybil', 23, 'Female', 'Lagos')
print(user)


# kwargs param -> dict
def app(**kwargs: dict):
    return kwargs


user = app(name="Sybil", age=23, gender='Female', location='Lagos')
print(user)


def user_app(age, gender='Male', *location, **name):
    return 'Params'
