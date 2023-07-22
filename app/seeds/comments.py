from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text


def seed_comments():

    comment1_1_10 = Comment(
        comment='This dish looks absolutely delicious!', user_id=10, pin_id=1)
    comment2_1_10 = Comment(
        comment="I can't resist the aroma of freshly baked bread.", user_id=10, pin_id=1)
    comment3_2_10 = Comment(
        comment="Food is not just sustenance; it's an experience.", user_id=10, pin_id=2)
    comment4_2_10 = Comment(
        comment="I'm always in the mood for a mouthwatering steak.", user_id=10, pin_id=2)
    comment5_3_10 = Comment(
        comment="The taste of homemade pasta is unmatched.", user_id=10, pin_id=3)
    comment6_3_10 = Comment(
        comment="I love how food brings people together.", user_id=10, pin_id=3)
    comment7_4_10 = Comment(
        comment="Every bite is a burst of flavors.", user_id=10, pin_id=4)
    comment8_4_10 = Comment(
        comment="I'm a foodie, and I'm proud of it!", user_id=10, pin_id=4)
    comment9_5_10 = Comment(
        comment="Nothing beats a warm bowl of soup on a chilly day.", user_id=10, pin_id=5)
    comment10_5_10 = Comment(
        comment="Food is the ultimate comfort.", user_id=10, pin_id=5)
    comment11_6_10 = Comment(
        comment="I'm on a mission to try every cuisine in the world.", user_id=10, pin_id=6)
    comment12_6_10 = Comment(
        comment="Food is the way to my heart.", user_id=10, pin_id=6)
    comment13_7_10 = Comment(
        comment="Spices and herbs add magic to any dish.", user_id=10, pin_id=7)
    
    
    
    
    
    
    comment14_7_9 = Comment(
        comment="The fusion of flavors in this dish is incredible.", user_id=9, pin_id=7)
    comment15_8_9 = Comment(
        comment="This dessert is pure indulgence.", user_id=9, pin_id=8)
    comment16_8_9 = Comment(
        comment="Cooking is an expression of love.", user_id=9, pin_id=8)
    comment17_9_9 = Comment(
        comment="Food is like a language that everyone understands.", user_id=9, pin_id=9)
    comment18_9_9 = Comment(
        comment="I'm always up for trying new recipes.", user_id=9, pin_id=9)
    comment19_10_9 = Comment(
        comment="Eating good food is a simple pleasure.", user_id=9, pin_id=10)
    comment20_10_9 = Comment(
        comment="I believe in the power of food to heal.", user_id=9, pin_id=10)
    comment21_11_9 = Comment(
        comment="Savoring each bite makes the meal more enjoyable.", user_id=9, pin_id=11)
    comment22_11_9 = Comment(
        comment="Food is the best conversation starter.", user_id=9, pin_id=11)
    comment23_12_9 = Comment(
        comment="Who can say no to a plate of perfectly crispy fries?", user_id=9, pin_id=12)
    comment24_12_9 = Comment(
        comment="This meal takes me back to my childhood.", user_id=9, pin_id=12)
    comment25_13_8 = Comment(
        comment="The secret ingredient is always love.", user_id=8, pin_id=13)
    comment26_13_8 = Comment(
        comment="I could eat this dish every day and never get tired of it.", user_id=8, pin_id=13)
    
    
    
    comment27_14_8 = Comment(
        comment='this is for yesterday\'s dinner', user_id=8, pin_id=14)
    comment28_14_8 = Comment(
        comment='will send it over soon!', user_id=8, pin_id=14)
    comment29_15_8 = Comment(
        comment='no problem, no rush', user_id=8, pin_id=15)
    comment30_15_8 = Comment(
        comment='the snacks were yummy', user_id=8, pin_id=15)
    comment31_16_8 = Comment(
        comment='i agree, they were the best', user_id=8, pin_id=16)
    comment32_16_8 = Comment(
        comment='i enjoyed them, too!', user_id=8, pin_id=16)
    comment33_17_8 = Comment(
        comment='disneyland was so fun', user_id=8, pin_id=17)
    comment34_17_8 = Comment(
        comment='happiest place on earth, absolutely!', user_id=8, pin_id=17)
    comment35_18_8 = Comment(
        comment='so expensive tho, i\'ll send the $$ in a month or so', user_id=8, pin_id=18)
    comment36_18_8 = Comment(
        comment='was this juice it up or jamba juice', user_id=8, pin_id=18)
    comment37_19_7 = Comment(
        comment='neither, we went to pressed', user_id=7, pin_id=19)
    comment38_19_7 = Comment(
        comment='spotify plan fees', user_id=7, pin_id=19)
    comment39_20_7 = Comment(
        comment='when was this??', user_id=7, pin_id=20)
    
    
    
    
    comment40_20_7 = Comment(
        comment='this is for yesterday\'s dinner', user_id=7, pin_id=20)
    comment41_21_7 = Comment(
        comment='will send it over soon!', user_id=7, pin_id=21)
    comment42_21_7 = Comment(
        comment='no problem, no rush', user_id=7, pin_id=21)
    comment43_22_7 = Comment(
        comment='the snacks were yummy', user_id=7, pin_id=22)
    comment44_22_7 = Comment(
        comment='i agree, they were the best', user_id=7, pin_id=22)
    comment45_23_7 = Comment(
        comment='i enjoyed them, too!', user_id=7, pin_id=23)
  
    comment46_23_7 = Comment(
        comment='disneyland was so fun', user_id=7, pin_id=23)
    comment47_24_7 = Comment(
        comment='happiest place on earth, absolutely!', user_id=7,pin_id=24)
    comment48_24_6 = Comment(
        comment='so expensive tho, i\'ll send the $$ in a month or so', user_id=6, pin_id=24)
    comment49_25_6 = Comment(
        comment='was this juice it up or jamba juice', user_id=6, pin_id=25)
    comment50_25_6 = Comment(
        comment='neither, we went to pressed', user_id=6, pin_id=25)
    comment51_26_6 = Comment(
        comment='spotify plan fees', user_id=6, pin_id=26)
    comment52_27_6 = Comment(
        comment='when was this??', user_id=6, pin_id=27)
    
    
    
    
    
    
    comment53_27_6 = Comment(
        comment='this is for yesterday\'s dinner', user_id=6, pin_id=27)
    comment54_28_6 = Comment(
        comment='will send it over soon!', user_id=6, pin_id=28)
    comment55_28_6 = Comment(
        comment='no problem, no rush', user_id=6, pin_id=28)
    comment56_29_6 = Comment(
        comment='the snacks were yummy', user_id=6, pin_id=29)
    comment57_29_6 = Comment(
        comment='i agree, they were the best', user_id=6, pin_id=29)
    comment58_30_6 = Comment(
        comment='i enjoyed them, too!', user_id=6, pin_id=30)
    comment59_30_6 = Comment(
        comment='disneyland was so fun', user_id=6, pin_id=30)
    comment60_31_5 = Comment(
        comment='happiest place on earth, absolutely!', user_id=5, pin_id=31)
    comment61_31_5 = Comment(
        comment='so expensive tho, i\'ll send the $$ in a month or so', user_id=5, pin_id=31)
    comment62_32_5 = Comment(
        comment='was this juice it up or jamba juice', user_id=5, pin_id=32)
    comment63_32_5 = Comment(
        comment='neither, we went to pressed', user_id=5, pin_id=32)
    comment64_33_5 = Comment(
        comment='spotify plan fees', user_id=5, pin_id=33)
    comment65_33_5 = Comment(
        comment='when was this??', user_id=5, pin_id=33)
    
    
    
    
    comment66_34_5 = Comment(
        comment='this is for yesterday\'s dinner', user_id=5, pin_id=34)
    comment67_34_5 = Comment(
        comment='will send it over soon!', user_id=5, pin_id=34)
    comment68_35_5 = Comment(
        comment='no problem, no rush', user_id=5, pin_id=35)
    comment69_35_5 = Comment(
        comment='the snacks were yummy', user_id=5, pin_id=35)
    comment70_36_5 = Comment(
        comment='i agree, they were the best', user_id=5, pin_id=36)
    comment71_36_5 = Comment(
        comment='i enjoyed them, too!', user_id=5, pin_id=36)
    comment72_37_4 = Comment(
        comment='disneyland was so fun', user_id=4, pin_id=37)
    comment73_37_4 = Comment(
        comment='happiest place on earth, absolutely!', user_id=4, pin_id=37)
    comment74_38_4 = Comment(
        comment='so expensive tho, i\'ll send the $$ in a month or so', user_id=4, pin_id=38)
    comment75_38_4 = Comment(
        comment='was this juice it up or jamba juice', user_id=4, pin_id=38)
    comment76_39_4 = Comment(
        comment='neither, we went to pressed', user_id=4, pin_id=39)
    comment77_39_4 = Comment(
        comment='spotify plan fees', user_id=4, pin_id=39)
    comment78_40_4 = Comment(
        comment='when was this??', user_id=4, pin_id=40)
    
    
    
    
    comment79_40_4 = Comment(
        comment='this is for yesterday\'s dinner', user_id=4, pin_id=40)
    comment80_41_4 = Comment(
        comment='will send it over soon!', user_id=4, pin_id=41)
    comment81_41_4 = Comment(
        comment='no problem, no rush', user_id=4, pin_id=41)
    comment82_42_4 = Comment(
        comment='the snacks were yummy', user_id=4, pin_id=42)
    comment83_42_4 = Comment(
        comment='i agree, they were the best', user_id=4, pin_id=42)
    comment84_43_3 = Comment(
        comment='i enjoyed them, too!', user_id=3, pin_id=4)
    comment85_43_3 = Comment(
        comment='disneyland was so fun', user_id=3, pin_id=43)
    comment86_44_3 = Comment(
        comment='happiest place on earth, absolutely!', user_id=3, pin_id=44)
    comment87_44_3 = Comment(
        comment='so expensive tho, i\'ll send the $$ in a month or so', user_id=3, pin_id=44)
    comment88_45_3 = Comment(
        comment='was this juice it up or jamba juice', user_id=3, pin_id=45)
    comment89_45_3 = Comment(
        comment='neither, we went to pressed', user_id=3, pin_id=45)
    comment90_46_3 = Comment(
        comment='spotify plan fees', user_id=3, pin_id=46)
    comment91_46_3 = Comment(
        comment='when was this??', user_id=3, pin_id=46)
    
    
    
    
    comment92_47_3 = Comment(
        comment='this is for yesterday\'s dinner', user_id=3, pin_id=47)
    comment93_47_3 = Comment(
        comment='will send it over soon!', user_id=3, pin_id=47)
    comment94_48_3 = Comment(
        comment='no problem, no rush', user_id=3, pin_id=48)
    comment95_48_3 = Comment(
        comment='the snacks were yummy', user_id=3, pin_id=48)
    comment96_49_2 = Comment(
        comment='i agree, they were the best', user_id=2, pin_id=49)
    comment97_49_2 = Comment(
        comment='i enjoyed them, too!', user_id=2, pin_id=49)
    comment98_50_2 = Comment(
        comment='disneyland was so fun', user_id=2, pin_id=50)
    comment99_50_2 = Comment(
        comment='happiest place on earth, absolutely!', user_id=2, pin_id=50)
    comment100_51_2 = Comment(
        comment='so expensive tho, i\'ll send the $$ in a month or so', user_id=2, pin_id=51)
    comment101_51_2 = Comment(
        comment='was this juice it up or jamba juice', user_id=2, pin_id=51)
    comment102_52_2 = Comment(
        comment='neither, we went to pressed', user_id=2, pin_id=52)
    comment103_52_2 = Comment(
        comment='spotify plan fees', user_id=2, pin_id=52)
    comment104_53_2 = Comment(
        comment='when was this??', user_id=2, pin_id=53)
    
    
    
    
    comment105_53_2 = Comment(
        comment='this is for yesterday\'s dinner', user_id=2, pin_id=53)
    comment106_54_2 = Comment(
        comment='will send it over soon!', user_id=2, pin_id=54)
    comment107_54_2 = Comment(
        comment='no problem, no rush', user_id=2, pin_id=54)
    comment108_55_1 = Comment(
        comment='the snacks were yummy', user_id=1, pin_id=55)
    comment109_55_1 = Comment(
        comment='i agree, they were the best', user_id=1, pin_id=55)
    comment110_56_1 = Comment(
        comment='i enjoyed them, too!', user_id=1, pin_id=56)
    comment111_56_1 = Comment(
        comment='disneyland was so fun', user_id=1, pin_id=56)
    comment112_57_1 = Comment(
        comment='happiest place on earth, absolutely!', user_id=1, pin_id=57)
    comment113_57_1 = Comment(
        comment='so expensive tho, i\'ll send the $$ in a month or so', user_id=1, pin_id=57)
    comment114_58_1 = Comment(
        comment='was this juice it up or jamba juice', user_id=1, pin_id=58)
    comment115_58_1 = Comment(
        comment='neither, we went to pressed', user_id=1, pin_id=58)
    comment116_59_1 = Comment(
        comment='spotify plan fees', user_id=1, pin_id=59)
    comment117_59_1 = Comment(
        comment='when was this??', user_id=1, pin_id=59)
    
    
    
    comment118_60_1 = Comment(
        comment='this is for yesterday\'s dinner', user_id=1, pin_id=60)
    comment119_60_1 = Comment(
        comment='will send it over soon!', user_id=2, pin_id=60)
    comment120_60_1 = Comment(
        comment='no problem, no rush', user_id=1, pin_id=60)
   
   
   
   
   

    db.session.add_all([
        comment1_1_10,
        comment2_1_10, 
        comment3_2_10,
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