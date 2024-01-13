from dataclasses import dataclass


@dataclass
class User:
    name: str
    lastname: str
    email: str
    gender: str
    phone: str
    birthday: list
    subjects: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


user = User(name='Sergei',
            lastname='Chu',
            email='ncrs@test.test',
            gender='Male',
            phone='1234567890',
            birthday=['06', 'October', '1983'],
            subjects='English',
            hobby='Reading',
            picture='bar-h.png',
            address='SPB',
            state='Haryana',
            city='Karnal')
