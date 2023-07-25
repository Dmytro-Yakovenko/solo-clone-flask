from app.models import db, Board, environment, SCHEMA
from sqlalchemy.sql import text

"American", 
"Mexican",
"Chinese",
"Japanese",
"Korean",
"French",
"Italian",
"Ukrainian",
"Mediterranean",
"Vegetarian"



# Adds a demo user, you can add other users here if you want
def seed_boards():
    board1 = Board(
        user_id = 1,
        title =  "American",
        description = "American cuisine is a diverse and eclectic blend of various influences from around the world, shaped by the country's history of immigration and regional differences. It is characterized by its wide range of flavors, portion sizes, and cultural contributions.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689654276/pexels-robin-stickel-70497_1_ehdkcs.jpg",
        )
    board2 = Board(
        user_id = 1,
        title =  "Mexican",
        description = "Mexican cuisine is known for its bold and vibrant flavors, diverse ingredients, and rich culinary traditions. It is deeply rooted in the country's indigenous heritage, with influences from Spanish colonization and other cultures. Mexican food varies regionally, with each area offering unique dishes and specialties.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689865891/pexels-hana-brannigan-3642718_daru6k.jpg",
        )
    board3 = Board(
        user_id = 1,
        title =  "Chinese",
        description = "Chinese cuisine is one of the most diverse and influential culinary traditions in the world, with a rich history spanning thousands of years. It varies greatly across different regions of China, each offering unique flavors, ingredients, and cooking techniques. Chinese food is known for its balance of flavors, including sweet, sour, salty, bitter, and umami.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689866146/pexels-prince-photos-3054690_bdu2rr.jpg",
        )
    board4 = Board(
        user_id = 2,
        title =  "Japanese",
        description = "Japanese cuisine, known for its simplicity, attention to detail, and emphasis on fresh, high-quality ingredients, has captured the hearts of food enthusiasts worldwide. The art of Japanese cooking revolves around preserving the natural flavors of the ingredients while creating aesthetically pleasing dishes.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689866449/pexels-rajesh-tp-2098085_lylhr7.jpg",
        )
    board5 = Board(
        user_id = 2,
        title =  "Korean",
        description = "Korean cuisine, known for its bold flavors, use of spices, and various side dishes, has gained popularity around the world. Korean food is deeply rooted in the country's history, geography, and cultural traditions.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689867051/pexels-senuscape-2313682_q11qva.jpg",
        )
    
    
    
    
    
    
    board6 = Board(
        user_id = 3,
        title =  "French",
        description = "French cuisine is renowned worldwide for its sophistication, rich flavors, and emphasis on high-quality ingredients. It is often regarded as one of the most influential and iconic culinary traditions globally. French food celebrates the art of cooking and the pleasure of dining, with a focus on balance, presentation, and attention to detail.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689867882/pexels-chevanon-photography-323682_1_jkrutt.jpg",
        )
    board7 = Board(
        user_id = 3,
        title =  "Italian",
        description = "Italian cuisine is beloved worldwide for its simplicity, emphasis on high-quality ingredients, and regional diversity. It is deeply rooted in the country's rich history and cultural traditions. Italian food celebrates the natural flavors of its ingredients, relying on fresh produce, herbs, and olive oil to create delicious and comforting dishes. ",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868810/pexels-vincent-rivaud-2295285_jrjr9q.jpg",
        )
    board8 = Board(
        user_id = 3,
        title =  "Ukrainian",
        description = "Ukrainian cuisine is a reflection of the country's agricultural heritage, incorporating hearty and wholesome dishes that celebrate the abundance of the land. Ukrainian food is known for its use of fresh, seasonal ingredients, and it often features a variety of grains, vegetables, meats, and dairy products. ",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868646/pexels-polina-tankilevitch-8601410_xln2nn.jpg",
        )
    board9 = Board(
        user_id = 4,
        title =  "Mediterranean",
        description = "Mediterranean cuisine encompasses the culinary traditions of the countries surrounding the Mediterranean Sea, including Southern Europe, North Africa, and the Middle East. It is characterized by its emphasis on fresh, locally sourced ingredients such as fruits, vegetables, grains, fish, olive oil, and herbs. Mediterranean food is not only flavorful and healthy but also reflects the region's rich history and cultural diversity.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868414/pexels-max-ravier-10563267_mdgbsj.jpg",
        )
    board10 = Board(
        user_id = 4,
        title =  "Vegetarian",
        description = "Vegetarian food is a type of cuisine that excludes meat, poultry, and seafood from its recipes, focusing instead on plant-based ingredients. Vegetarian diets vary widely, and there are several subcategories, such as lacto-ovo vegetarians who consume dairy and eggs, lacto vegetarians who consume dairy but avoid eggs, ovo vegetarians who consume eggs but avoid dairy, and vegans who avoid all animal products, including dairy and eggs.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868220/pexels-maarten-van-den-heuvel-2284166_i6ptee.jpg",
        )

    
    board11 = Board(
        user_id = 5,
        title =  "American",
        description = "American cuisine is a diverse and eclectic blend of various influences from around the world, shaped by the country's history of immigration and regional differences. It is characterized by its wide range of flavors, portion sizes, and cultural contributions.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689654276/pexels-robin-stickel-70497_1_ehdkcs.jpg",
        )
    board12 = Board(
        user_id = 5,
        title =  "Mexican",
        description = "Mexican cuisine is known for its bold and vibrant flavors, diverse ingredients, and rich culinary traditions. It is deeply rooted in the country's indigenous heritage, with influences from Spanish colonization and other cultures. Mexican food varies regionally, with each area offering unique dishes and specialties.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689865891/pexels-hana-brannigan-3642718_daru6k.jpg",
        )
    board13 = Board(
        user_id = 5,
        title =  "Chinese",
        description = "Chinese cuisine is one of the most diverse and influential culinary traditions in the world, with a rich history spanning thousands of years. It varies greatly across different regions of China, each offering unique flavors, ingredients, and cooking techniques. Chinese food is known for its balance of flavors, including sweet, sour, salty, bitter, and umami.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689866146/pexels-prince-photos-3054690_bdu2rr.jpg",
        )
    board14 = Board(
        user_id = 6,
        title =  "Japanese",
        description = "Japanese cuisine, known for its simplicity, attention to detail, and emphasis on fresh, high-quality ingredients, has captured the hearts of food enthusiasts worldwide. The art of Japanese cooking revolves around preserving the natural flavors of the ingredients while creating aesthetically pleasing dishes.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689866449/pexels-rajesh-tp-2098085_lylhr7.jpg",
        )
    board15 = Board(
        user_id = 6,
        title =  "Korean",
        description = "Korean cuisine, known for its bold flavors, use of spices, and various side dishes, has gained popularity around the world. Korean food is deeply rooted in the country's history, geography, and cultural traditions.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689867051/pexels-senuscape-2313682_q11qva.jpg",
        )
    
   
    
    board16 = Board(
        user_id = 6,
        title =  "French",
        description = "French cuisine is renowned worldwide for its sophistication, rich flavors, and emphasis on high-quality ingredients. It is often regarded as one of the most influential and iconic culinary traditions globally. French food celebrates the art of cooking and the pleasure of dining, with a focus on balance, presentation, and attention to detail.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689867882/pexels-chevanon-photography-323682_1_jkrutt.jpg",
        )
    board17 = Board(
        user_id = 7,
        title =  "Italian",
        description = "Italian cuisine is beloved worldwide for its simplicity, emphasis on high-quality ingredients, and regional diversity. It is deeply rooted in the country's rich history and cultural traditions. Italian food celebrates the natural flavors of its ingredients, relying on fresh produce, herbs, and olive oil to create delicious and comforting dishes. ",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868810/pexels-vincent-rivaud-2295285_jrjr9q.jpg",
        )
    board18 = Board(
        user_id = 7,
        title =  "Ukrainian",
        description = "Ukrainian cuisine is a reflection of the country's agricultural heritage, incorporating hearty and wholesome dishes that celebrate the abundance of the land. Ukrainian food is known for its use of fresh, seasonal ingredients, and it often features a variety of grains, vegetables, meats, and dairy products. ",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868646/pexels-polina-tankilevitch-8601410_xln2nn.jpg",
        )
    board19 = Board(
        user_id = 8,
        title =  "Mediterranean",
        description = "Mediterranean cuisine encompasses the culinary traditions of the countries surrounding the Mediterranean Sea, including Southern Europe, North Africa, and the Middle East. It is characterized by its emphasis on fresh, locally sourced ingredients such as fruits, vegetables, grains, fish, olive oil, and herbs. Mediterranean food is not only flavorful and healthy but also reflects the region's rich history and cultural diversity.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868414/pexels-max-ravier-10563267_mdgbsj.jpg",
        )
    board20 = Board(
        user_id = 8,
        title =  "Vegetarian",
        description = "Vegetarian food is a type of cuisine that excludes meat, poultry, and seafood from its recipes, focusing instead on plant-based ingredients. Vegetarian diets vary widely, and there are several subcategories, such as lacto-ovo vegetarians who consume dairy and eggs, lacto vegetarians who consume dairy but avoid eggs, ovo vegetarians who consume eggs but avoid dairy, and vegans who avoid all animal products, including dairy and eggs.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868220/pexels-maarten-van-den-heuvel-2284166_i6ptee.jpg",
        )
    
    
    board21 = Board(
        user_id = 9,
        title =  "American",
        description = "American cuisine is a diverse and eclectic blend of various influences from around the world, shaped by the country's history of immigration and regional differences. It is characterized by its wide range of flavors, portion sizes, and cultural contributions.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689654276/pexels-robin-stickel-70497_1_ehdkcs.jpg",
        )
    board22 = Board(
        user_id = 9,
        title =  "Mexican",
        description = "Mexican cuisine is known for its bold and vibrant flavors, diverse ingredients, and rich culinary traditions. It is deeply rooted in the country's indigenous heritage, with influences from Spanish colonization and other cultures. Mexican food varies regionally, with each area offering unique dishes and specialties.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689865891/pexels-hana-brannigan-3642718_daru6k.jpg",
        )
    board23 = Board(
        user_id = 9,
        title =  "Chinese",
        description = "Chinese cuisine is one of the most diverse and influential culinary traditions in the world, with a rich history spanning thousands of years. It varies greatly across different regions of China, each offering unique flavors, ingredients, and cooking techniques. Chinese food is known for its balance of flavors, including sweet, sour, salty, bitter, and umami.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689866146/pexels-prince-photos-3054690_bdu2rr.jpg",
        )
    board24 = Board(
        user_id = 10,
        title =  "Japanese",
        description = "Japanese cuisine, known for its simplicity, attention to detail, and emphasis on fresh, high-quality ingredients, has captured the hearts of food enthusiasts worldwide. The art of Japanese cooking revolves around preserving the natural flavors of the ingredients while creating aesthetically pleasing dishes.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689866449/pexels-rajesh-tp-2098085_lylhr7.jpg",
        )
    board25 = Board(
        user_id = 10,
        title =  "Korean",
        description = "Korean cuisine, known for its bold flavors, use of spices, and various side dishes, has gained popularity around the world. Korean food is deeply rooted in the country's history, geography, and cultural traditions.",
        board_image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689867051/pexels-senuscape-2313682_q11qva.jpg",
        )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
  

    db.session.add(board1)
    db.session.add(board2)
    db.session.add(board3)
    db.session.add(board4)
    db.session.add(board5)
    db.session.add(board6)
    db.session.add(board7)
    db.session.add(board8)
    db.session.add(board9)
    db.session.add(board10)
    db.session.add(board11)
    db.session.add(board12)
    db.session.add(board13)
    db.session.add(board14)
    db.session.add(board15)
    db.session.add(board16)
    db.session.add(board17)
    db.session.add(board18)
    db.session.add(board19)
    db.session.add(board20)
    db.session.add(board21)
    db.session.add(board22)
    db.session.add(board23)
    db.session.add(board24)
    db.session.add(board25)
  
    db.session.commit()
    
    
# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_boards():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.boards RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM boards"))
        
    db.session.commit()