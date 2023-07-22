from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='DemoL',
        email='demo@aa.io',
        password='password',
        first_name = "Demo",
        last_name= "Lition",
        user_image ="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689863122/pexels-andrea-piacquadio-842811_mmq4rb.jpg"
        )
    dmytro = User(
        username='DmytroY',
        email='dmytro@aa.io',
        password='password',
        first_name = "Dmytro",
        last_name= "Yakovenko",
        user_image ="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1686975650/348650858_1637501866663074_4165871404603428938_n_1_yogwph.ico"
        )
    david = User(
        username='DavidD',
        email='david@aa.io',
        password='password',
        first_name = "David",
        last_name= "Dolan",
        user_image="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689863116/pexels-andrea-piacquadio-3799790_yuuvwm.jpg"
        )
    john = User(
        username='JohnS',
        email='john@aa.io',
        password='password',
        first_name = "John",
        last_name= "Smith",
        user_image="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689863108/pexels-rein-krijgsman-3139612_p7bqra.jpg"
        )
    mary = User(
        username='MaryJ',
        email='mary@aa.io',
        password='password',
        first_name = "Mary",
        last_name= "Jane",
        user_image="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689863112/pexels-maryia-plashchynskaya-3615455_jgscpq.jpg"
        )
    moura = User(
        username='MouraB',
        email='moura@aa.io',
        password='password',
        first_name = "Moura",
        last_name= "Borisova",
        user_image="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689863136/pexels-daniel-xavier-1239291_yjnmd8.jpg"
        )
    james = User(
        username='JamesT',
        email='james@aa.io',
        password='password',
        first_name = "James",
        last_name= "Thompson",
        user_image="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689863699/pexels-gabriel-lima-1852083_vf2xur.jpg"
        )
    alex = User(
        username='AlexG',
        email='alex@aa.io',
        password='password',
        first_name = "Alex",
        last_name= "Gomes",
        user_image="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689863665/pexels-jonas-svidras-713829_ne1orl.jpg"
        )
    bruce= User(
        username='BruceL',
        email='bruce@aa.io',
        password='password',
        first_name = "Bruce",
        last_name= "Lee",
        user_image="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689863656/pexels-mike-greer-1327281_dw2qhu.jpg"
        )
    bob = User(
        username='BobM',
        email='bob@aa.io',
        password='password',
        first_name = "Bob",
        last_name= "Marley",
        user_image="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1673016570/samples/people/kitchen-bar.jpg"
        )
  

    db.session.add(demo)
    db.session.add(dmytro)
    db.session.add(david)
    db.session.add(john)
    db.session.add(mary)
    db.session.add(moura)
    db.session.add(james)
    db.session.add(alex)
    db.session.add(bruce)
    db.session.add(bob)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()