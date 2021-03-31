from data import db_session
from data.jobs import Jobs
from data.users import User

db_session.global_init('sempal.sqlite')
session = db_session.create_session()

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
user.hashed_password = "cap"
session.add(user)

session.commit()
