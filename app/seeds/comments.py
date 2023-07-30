from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text


def seed_comments():

    comment1_1_10 = Comment(
        comment='This dish looks absolutely delicious!', user_id=9, pin_id=1)
    comment2_1_10 = Comment(
        comment="I can't resist the aroma of freshly baked bread.", user_id=8, pin_id=1)
    comment3_2_10 = Comment(
        comment="Food is not just sustenance; it's an experience.", user_id=7, pin_id=2)
    comment4_2_10 = Comment(
        comment="I'm always in the mood for a mouthwatering steak.", user_id=6, pin_id=2)
    comment5_3_10 = Comment(
        comment="The taste of homemade pasta is unmatched.", user_id=5, pin_id=3)
    comment6_3_10 = Comment(
        comment="I love how food brings people together.", user_id=4, pin_id=3)
    comment7_4_10 = Comment(
        comment="Every bite is a burst of flavors.", user_id=3, pin_id=4)
    comment8_4_10 = Comment(
        comment="I'm a foodie, and I'm proud of it!", user_id=2, pin_id=4)
    comment9_5_10 = Comment(
        comment="Nothing beats a warm bowl of soup on a chilly day.", user_id=1, pin_id=5)
    comment10_5_10 = Comment(
        comment="Food is the ultimate comfort.", user_id=10, pin_id=5)
    comment11_6_10 = Comment(
        comment="I'm on a mission to try every cuisine in the world.", user_id=9, pin_id=6)
    comment12_6_10 = Comment(
        comment="Food is the way to my heart.", user_id=8, pin_id=6)
    comment13_7_10 = Comment(
        comment="Spices and herbs add magic to any dish.", user_id=7, pin_id=7)
    comment14_7_9 = Comment(
        comment="The fusion of flavors in this dish is incredible.", user_id=6, pin_id=7)
    comment15_8_9 = Comment(
        comment="This dessert is pure indulgence.", user_id=5, pin_id=8)
    comment16_8_9 = Comment(
        comment="Cooking is an expression of love.", user_id=4, pin_id=8)
    comment17_9_9 = Comment(
        comment="Food is like a language that everyone understands.", user_id=3, pin_id=9)
    comment18_9_9 = Comment(
        comment="I'm always up for trying new recipes.", user_id=2, pin_id=9)
    comment19_10_9 = Comment(
        comment="Eating good food is a simple pleasure.", user_id=1, pin_id=10)
    comment20_10_9 = Comment(
        comment="I believe in the power of food to heal.", user_id=10, pin_id=10)
    comment21_11_9 = Comment(
        comment="Savoring each bite makes the meal more enjoyable.", user_id=9, pin_id=11)
    comment22_11_9 = Comment(
        comment="Food is the best conversation starter.", user_id=8, pin_id=11)
    comment23_12_9 = Comment(
        comment="Who can say no to a plate of perfectly crispy fries?", user_id=7, pin_id=12)
    comment24_12_9 = Comment(
        comment="This meal takes me back to my childhood.", user_id=6, pin_id=12)
    comment25_13_8 = Comment(
        comment="The secret ingredient is always love.", user_id=5, pin_id=13)
    comment26_13_8 = Comment(
        comment="I could eat this dish every day and never get tired of it.", user_id=4, pin_id=13)
    
    
    
    comment27_14_8 = Comment(
        comment="Wow, this recipe looks delicious! Can't wait to try it!", user_id=3, pin_id=14)
    comment28_14_8 = Comment(
        comment="I love how simple and easy this recipe is to follow.", user_id=2, pin_id=14)
    comment29_15_8 = Comment(
        comment="This is the perfect comfort food for a cozy night in.", user_id=1, pin_id=15)
    comment30_15_8 = Comment(
        comment="My family absolutely loved this recipe! It's going to be a regular in our meal rotation."
, user_id=10, pin_id=15)
    comment31_16_8 = Comment(
        comment="The combination of flavors in this recipe is simply amazing.", user_id=9, pin_id=16)
    comment32_16_8 = Comment(
        comment="I can't believe how flavorful and tasty this dish turned out.", user_id=8, pin_id=16)
    comment33_17_8 = Comment(
        comment="My mouth is watering just looking at this recipe.", user_id=7, pin_id=17)
    comment34_17_8 = Comment(
        comment="I'm always on the lookout for new recipe ideas, and this one is a winner."
, user_id=6, pin_id=17)
    comment35_18_8 = Comment(
        comment="I never knew cooking could be so much fun until I tried this recipe.", user_id=5, pin_id=18)
    comment36_18_8 = Comment(
        comment="The presentation of this dish is so impressive. It's almost too beautiful to eat!", user_id=4, pin_id=18)
    comment37_19_7 = Comment(
        comment="I can't get enough of this recipe. It's addictively delicious.", user_id=3, pin_id=19)
    comment38_19_7 = Comment(
        comment="This recipe is a hit with both kids and adults. Everyone loves it!", user_id=2, pin_id=19)
    comment39_20_7 = Comment(
        comment="I've made this recipe for dinner parties, and it's always a crowd-pleaser."
, user_id=1, pin_id=20)
    
    
    
    
    comment40_20_7 = Comment(
        comment="My kitchen smells amazing while making this recipe.", user_id=10, pin_id=20)
    comment41_21_7 = Comment(
        comment= "I feel like a professional chef when I cook this recipe.", user_id=9, pin_id=21)
    comment42_21_7 = Comment(
        comment="The step-by-step instructions in this recipe are so helpful."
, user_id=8, pin_id=21)
    comment43_22_7 = Comment(
        comment="I'm already planning to make this recipe again next week.", user_id=7, pin_id=22)
    comment44_22_7 = Comment(
        comment="This recipe is perfect for meal prep. It makes great leftovers.", user_id=6, pin_id=22)
    comment45_23_7 = Comment(
        comment="I made this recipe for my friends, and they were impressed with my cooking skills.", user_id=5, pin_id=23)
  
    comment46_23_7 = Comment(
        comment="I can't stop raving about how good this recipe is.", user_id=4, pin_id=23)
    comment47_24_7 = Comment(
        comment="This recipe is a fantastic way to use up leftover ingredients.", user_id=3,pin_id=24)
    comment48_24_6 = Comment(
        comment="I'm adding this recipe to my collection of all-time favorites.", user_id=2, pin_id=24)
    comment49_25_6 = Comment(
        comment="I'm so glad I found this recipe. It's a game-changer!", user_id=1, pin_id=25)
    comment50_25_6 = Comment(
        comment="I can't believe I never tried this recipe before. It's a new favorite.", user_id=10, pin_id=25)
    comment51_26_6 = Comment(
        comment="I love how versatile this recipe is. You can customize it to your taste.", user_id=9, pin_id=26)
    comment52_27_6 = Comment(
        comment="The flavors in this recipe are perfectly balanced.", user_id=8, pin_id=27)
    comment53_27_6 = Comment(
        comment="This recipe is perfect for a quick and easy weeknight dinner.", user_id=7, pin_id=27)
    comment54_28_6 = Comment(
        comment="I made this recipe for my significant other, and they loved it.", user_id=6, pin_id=28)
    comment55_28_6 = Comment(
        comment="My kids are usually picky eaters, but they devoured this recipe.", user_id=5, pin_id=28)
    comment56_29_6 = Comment(
        comment="I'm a beginner cook, and this recipe was so easy to follow."
, user_id=4, pin_id=29)
    comment57_29_6 = Comment(
        comment="This recipe brings back fond memories of my childhood.", user_id=3, pin_id=29)
    comment58_30_6 = Comment(
        comment="I made this recipe for a potluck, and everyone asked for the recipe.", user_id=2, pin_id=30)
    comment59_30_6 = Comment(
        comment="The secret ingredient in this recipe really takes it to the next level.", user_id=1, pin_id=30)
    comment60_31_5 = Comment(
        comment="I can't believe I made something this delicious from scratch.", user_id=10, pin_id=31)
    comment61_31_5 = Comment(
        comment="This recipe is perfect for special occasions and celebrations.", user_id=9, pin_id=31)
    comment62_32_5 = Comment(
        comment="I'm already planning to share this recipe with all my friends."
, user_id=8, pin_id=32)
    comment63_32_5 = Comment(
        comment="I'm so grateful for this recipe. It's become a family tradition.", user_id=7, pin_id=32)
    comment64_33_5 = Comment(
        comment="This recipe is like a taste of heaven. I can't get enough!", user_id=6, pin_id=33)
    comment65_33_5 = Comment(
        comment="I'm going to make this recipe for my next dinner party. It's a showstopper."
, user_id=5, pin_id=33)
    
    
    
    
    comment66_34_5 = Comment(
        comment='this is for yesterday\'s dinner', user_id=5, pin_id=34)
    comment67_34_5 = Comment(
        comment="The flavors in this recipe complement each other so well.", user_id=4, pin_id=34)
    comment68_35_5 = Comment(
        comment="I made this recipe for a date night, and it was a hit.", user_id=3, pin_id=35)
    comment69_35_5 = Comment(
        comment="This recipe is perfect for a cozy night at home with a good movie.", user_id=2, pin_id=35)
    comment70_36_5 = Comment(
        comment="I'm already thinking of variations I can try with this recipe.", user_id=1, pin_id=36)
    comment71_36_5 = Comment(
        comment="I'm impressed by how this recipe manages to be both healthy and indulgent.", user_id=10, pin_id=36)
    comment72_37_4 = Comment(
        comment="I can't believe I made something this tasty with just a few ingredients.", user_id=9, pin_id=37)
    comment73_37_4 = Comment(
        comment="This recipe is like comfort in a bowl. It's so satisfying.", user_id=8, pin_id=37)
    comment74_38_4 = Comment(
        comment="I'm adding this recipe to my cookbook. It's a must-have.", user_id=7, pin_id=38)
    comment75_38_4 = Comment(
        comment="I've made this recipe multiple times, and it never disappoints.", user_id=6, pin_id=38)
    comment76_39_4 = Comment(
        comment="This recipe reminds me of my grandma's cooking. It's nostalgic and delicious.", user_id=5, pin_id=39)
    comment77_39_4 = Comment(
        comment="I'm recommending this recipe to all my foodie friends. They'll love it.", user_id=4, pin_id=39)
    comment78_40_4 = Comment(
        comment="The presentation of this dish is so impressive. It's restaurant-quality.", user_id=3, pin_id=40)
    
    
    
    
    comment79_40_4 = Comment(
        comment="I can't believe I was able to recreate this restaurant dish at home.", user_id=2, pin_id=40)
    comment80_41_4 = Comment(
        comment="I love how this recipe uses fresh, seasonal ingredients.", user_id=1, pin_id=41)
    comment81_41_4 = Comment(
        comment="This recipe is perfect for a romantic dinner for two.", user_id=10, pin_id=41)
    comment82_42_4 = Comment(
        comment="I'm making a double batch of this recipe to freeze for later. It's that good!", user_id=9, pin_id=42)
    comment83_42_4 = Comment(
        comment="The cooking tips in this recipe are so helpful for beginners.", user_id=8, pin_id=42)
    comment84_43_3 = Comment(
        comment="I can't wait to make this recipe for my next family gathering.", user_id=7, pin_id=4)
    comment85_43_3 = Comment(
        comment="I made this recipe for my picky eaters, and they loved it.", user_id=6, pin_id=43)
    comment86_44_3 = Comment(
        comment="This recipe is a great way to introduce new flavors to your palate.", user_id=5, pin_id=44)
    comment87_44_3 = Comment(
        comment="I'm amazed at how well the flavors in this recipe complement each other.", user_id=4, pin_id=44)
    comment88_45_3 = Comment(
        comment="I made this recipe for my book club, and everyone raved about it.", user_id=3, pin_id=45)
    comment89_45_3 = Comment(
        comment="I love how this recipe makes use of pantry staples I already have.", user_id=2, pin_id=45)
    comment90_46_3 = Comment(
        comment="This recipe is perfect for meal prep. It saves me so much time during the week.", user_id=1, pin_id=46)
    comment91_46_3 = Comment(
        comment="I'm impressed by how easy this recipe is to make, yet it tastes so gourmet.", user_id=10, pin_id=46)
    
    
    
    
    comment92_47_3 = Comment(
        comment="I made this recipe for a dinner date, and it was a hit.", user_id=9, pin_id=47)
    comment93_47_3 = Comment(
        comment="I'm so glad I found this recipe. It's a keeper!", user_id=8, pin_id=47)
    comment94_48_3 = Comment(
        comment="I'm excited to experiment with different herbs and spices in this recipe.", user_id=7, pin_id=48)
    comment95_48_3 = Comment(
        comment="This recipe is a great way to use up leftover vegetables.", user_id=6, pin_id=48)
    comment96_49_2 = Comment(
        comment="I made this recipe for a dinner party, and everyone asked for seconds.", user_id=5, pin_id=49)
    comment97_49_2 = Comment(
        comment="This recipe is perfect for those busy weeknights when I need a quick dinner.", user_id=4, pin_id=49)
    comment98_50_2 = Comment(
        comment="I can't believe how much my cooking skills have improved with this recipe.", user_id=3, pin_id=50)
    comment99_50_2 = Comment(
        comment="I made this recipe for a potluck, and it disappeared within minutes.", user_id=2, pin_id=50)
    comment100_51_2 = Comment(
        comment="This recipe is so versatile. You can easily customize it to your liking.", user_id=1, pin_id=51)
    comment101_51_2 = Comment(
        comment="I'm already planning to make this recipe for my next holiday gathering.", user_id=10, pin_id=51)
    comment102_52_2 = Comment(
        comment="I can't get enough of the delicious aroma coming from my kitchen while making this recipe.", user_id=9, pin_id=52)
    comment103_52_2 = Comment(
        comment="This recipe is a delightful combination of sweet and savory flavors.", user_id=8, pin_id=52)
    comment104_53_2 = Comment(
        comment="I made this recipe for my significant other, and they loved it so much.", user_id=7, pin_id=53)
    
    
    
    
    comment105_53_2 = Comment(
        comment="I'm adding this recipe to my list of go-to meals. It's foolproof.", user_id=6, pin_id=53)
    comment106_54_2 = Comment(
        comment="This recipe is like a burst of sunshine on a plate. It's so vibrant and colorful.", user_id=5, pin_id=54)
    comment107_54_2 = Comment(
        comment="I can't believe how easy this recipe is to make. It's perfect for beginners.", user_id=4, pin_id=54)
    comment108_55_1 = Comment(
        comment="I love how this recipe takes me back to my favorite vacation destination.", user_id=3, pin_id=55)
    comment109_55_1 = Comment(
        comment="This recipe is a great way to introduce kids to new and healthy foods.", user_id=2, pin_id=55)
    comment110_56_1 = Comment(
        comment="I made this recipe for my family, and they couldn't stop praising my cooking skills.", user_id=1, pin_id=56)
    comment111_56_1 = Comment(
        comment="I'm so impressed with the level of detail in this recipe's instructions. It's easy to follow.", user_id=10, pin_id=56)
    comment112_57_1 = Comment(
        comment="This recipe is perfect for a quick lunch or dinner option.", user_id=9, pin_id=57)
    comment113_57_1 = Comment(
        comment="I'm already planning to make this recipe for my next potluck with friends.", user_id=8, pin_id=57)
    comment114_58_1 = Comment(
        comment="I love how this recipe uses seasonal produce to create a fresh and flavorful dish.", user_id=7, pin_id=58)
    comment115_58_1 = Comment(
        comment="This recipe is perfect for a cozy night at home with a good book.", user_id=6, pin_id=58)
    comment116_59_1 = Comment(
        comment="I can't get over how delicious this recipe is. It's my new favorite.", user_id=5, pin_id=59)
    comment117_59_1 = Comment(
        comment="I'm adding this recipe to my weekly meal plan. It's a family favorite.", user_id=4, pin_id=59)
    
    
    
    comment118_60_1 = Comment(
        comment="This recipe is perfect for a special occasion or celebration.", user_id=3, pin_id=60)
    comment119_60_1 = Comment(
        comment="I'm so grateful for this recipe. It's a lifesaver on busy days.", user_id=2, pin_id=60)
    comment120_60_1 = Comment(
        comment="This recipe is like a taste of my favorite restaurant at home.", user_id=1, pin_id=60)
   
   
   
   
   

    db.session.add_all([
        comment1_1_10,
        comment2_1_10, 
        comment3_2_10,
        comment4_2_10,
        comment5_3_10, 
        comment6_3_10,
        comment7_4_10,
        comment8_4_10, 
        comment9_5_10, 
        comment10_5_10, 
        comment11_6_10, 
        comment12_6_10,
        comment13_7_10,
        comment14_7_9, 
        comment15_8_9,
        comment16_8_9, 
        comment17_9_9,
        comment18_9_9, 
        comment19_10_9, 
        comment20_10_9, 
        comment21_11_9,
        comment22_11_9,
        comment23_12_9, 
        comment24_12_9,
        comment25_13_8, 
        comment26_13_8, 
        comment27_14_8,
        comment28_14_8,
        comment29_15_8,
        comment30_15_8,
        comment31_16_8, 
        comment32_16_8, 
        comment33_17_8,
        comment34_17_8, 
        comment35_18_8, 
        comment36_18_8,
        comment37_19_7, 
        comment38_19_7,
        comment39_20_7, 
        comment40_20_7,
        comment41_21_7,
        comment42_21_7,
        comment43_22_7, 
        comment44_22_7, 
        comment45_23_7,
        comment46_23_7, 
        comment47_24_7,
        comment48_24_6, 
        comment49_25_6, 
        comment50_25_6, 
        comment51_26_6,
        comment52_27_6,
        comment53_27_6,
        comment54_28_6, 
        comment55_28_6, 
        comment56_29_6, 
        comment57_29_6, 
        comment58_30_6,
        comment59_30_6,
        comment60_31_5,
        comment61_31_5,
        comment62_32_5,
        comment63_32_5, 
        comment64_33_5, 
        comment65_33_5, 
        comment66_34_5,
        comment67_34_5,
        comment68_35_5,
        comment69_35_5, 
        comment70_36_5, 
        comment71_36_5, 
        comment72_37_4, 
        comment73_37_4,
        comment74_38_4, 
        comment75_38_4,
        comment76_39_4, 
        comment77_39_4, 
        comment78_40_4, 
        comment79_40_4, 
        comment80_41_4, 
        comment81_41_4, 
        comment82_42_4, 
        comment83_42_4, 
        comment84_43_3, 
        comment85_43_3, 
        comment86_44_3, 
        comment87_44_3, 
        comment88_45_3, 
        comment89_45_3, 
        comment90_46_3,
        comment91_46_3,
        comment92_47_3,
        comment93_47_3,
        comment94_48_3, 
        comment95_48_3, 
        comment96_49_2, 
        comment97_49_2, 
        comment98_50_2, 
        comment99_50_2,
        comment100_51_2, 
        comment101_51_2,
        comment102_52_2,
        comment103_52_2, 
        comment104_53_2, 
        comment105_53_2, 
        comment106_54_2, 
        comment107_54_2,
        comment108_55_1, 
        comment109_55_1, 
        comment110_56_1,
        comment111_56_1, 
        comment112_57_1,
        comment113_57_1, 
        comment114_58_1,
        comment115_58_1,
        comment116_59_1,
        comment117_59_1,
        comment118_60_1,
        comment119_60_1, 
        comment120_60_1,
    ])
    db.session.commit()


def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()