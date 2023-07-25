from app.models import db, PinBoard, environment, SCHEMA
from sqlalchemy.sql import text



def seed_pins_boards():
    #user 1
    #board 1
    pin1_1 = PinBoard(
        pin_id=1, board_id=1)
    pin2_1 = PinBoard(
        pin_id=2, board_id=1)
    #board 2
    pin3_2 = PinBoard(
        pin_id=3, board_id=1)
    pin4_2 = PinBoard(
        pin_id=4, board_id=2)
    pin5_2 = PinBoard(
        pin_id=5, board_id=2)
    #board 3
    pin6_3 = PinBoard(
        pin_id=6, board_id=3)
    
    
    #user 2
    pin7_4 = PinBoard(
        pin_id=7, board_id=4)
    pin8_4 = PinBoard(
        pin_id=8, board_id=4)
    
    pin9_4 = PinBoard(
        pin_id=9, board_id=4)
    pin10_5 = PinBoard(
        pin_id=10, board_id=5)
    
    pin11_5 = PinBoard(
        pin_id=11, board_id=5)
    pin12_5 = PinBoard(
        pin_id=12, board_id=5)
    
    
    #user 3
    pin13_1 = PinBoard(
        pin_id=13, board_id=6)
    pin14_1 = PinBoard(
        pin_id=14, board_id=7)
    
    pin15_2 = PinBoard(
        pin_id=15, board_id=7)
    pin16_2 = PinBoard(
        pin_id=16, board_id=7)
    pin17_1 = PinBoard(
        pin_id=17, board_id=8)
    pin18_1 = PinBoard(
        pin_id=18, board_id=8)
    
    #user 4
    
    pin19_2 = PinBoard(
        pin_id=19, board_id=10)
    pin20_2 = PinBoard(
        pin_id=20, board_id=9)
    
    pin21_1 = PinBoard(
        pin_id=21, board_id=10)
    pin22_1 = PinBoard(
        pin_id=22, board_id=9)
    
    pin23_2 = PinBoard(
        pin_id=23, board_id=10)
    pin24_2 = PinBoard(
        pin_id=24, board_id=9)
    
    
    #user 5
    pin25_1 = PinBoard(
        pin_id=25, board_id=11)
    pin26_1 = PinBoard(
        pin_id=26, board_id=11)
    
    pin27_2 = PinBoard(
        pin_id=27, board_id=12)
    pin28_2 = PinBoard(
        pin_id=28, board_id=12)
    pin29_1 = PinBoard(
        pin_id=29, board_id=12)
    pin30_1 = PinBoard(
        pin_id=30, board_id=13)
    
    #user 6
    
    pin31_2 = PinBoard(
        pin_id=31, board_id=14)
    pin32_2 = PinBoard(
        pin_id=32, board_id=14)
    
    pin33_1 = PinBoard(
        pin_id=33, board_id=14)
    pin34_1 = PinBoard(
        pin_id=34, board_id=16)
    
    pin35_2 = PinBoard(
        pin_id=35, board_id=15)
    pin36_2 = PinBoard(
        pin_id=36, board_id=15)
    
    
    #user 7
    pin37_1 = PinBoard(
        pin_id=37, board_id=17)
    pin38_1 = PinBoard(
        pin_id=38, board_id=17)
    
    pin39_2 = PinBoard(
        pin_id=39, board_id=18)
    pin40_2 = PinBoard(
        pin_id=40, board_id=18)
    pin41_1 = PinBoard(
        pin_id=41, board_id=18)
    pin42_1 = PinBoard(
        pin_id=42, board_id=18)
    
    
    
    #user 8
    pin43_2 = PinBoard(
        pin_id=43, board_id=19)
    pin44_2 = PinBoard(
        pin_id=44, board_id=9)
    
    pin45_1 = PinBoard(
        pin_id=45, board_id=19)
    pin46_1 = PinBoard(
        pin_id=46, board_id=20)
    
    pin47_2 = PinBoard(
        pin_id=47, board_id=20)
    pin48_2 = PinBoard(
        pin_id=48, board_id=20)
    
    
    #user 9
    pin49_1 = PinBoard(
        pin_id=49, board_id=21)
    pin50_1 = PinBoard(
        pin_id=50, board_id=21)
    
    pin51_2 = PinBoard(
        pin_id=51, board_id=22)
    pin52_2 = PinBoard(
        pin_id=52, board_id=22)
    pin53_1 = PinBoard(
        pin_id=53, board_id=23)
    pin54_1 = PinBoard(
        pin_id=54, board_id=23)
    
    
    #user 10
    pin55_2 = PinBoard(
        pin_id=55, board_id=24)
    pin56_2 = PinBoard(
        pin_id=56, board_id=24)
    
    pin57_1 = PinBoard(
        pin_id=57, board_id=25)
    pin58_1 = PinBoard(
        pin_id=58, board_id=25)
    
    pin59_2 = PinBoard(
        pin_id=59, board_id=25)
    pin60_2 = PinBoard(
        pin_id=60, board_id=25)
    
    
    
    

    db.session.add_all([
        pin1_1 ,
        pin2_1, 
        pin3_2,
        pin4_2,
        pin5_2,
        pin6_3,
        pin7_4,
        pin8_4,
        pin9_4,
        pin10_5, 
        pin11_5,
        pin12_5,
        pin13_1,
        pin14_1,
        pin15_2,
        pin16_2,
        pin17_1,
        pin18_1,
        pin19_2,
        pin20_2,  
        pin21_1, 
        pin22_1, 
        pin23_2,
        pin24_2,
        pin25_1, 
        pin26_1,
        pin27_2, 
        pin28_2, 
        pin29_1,
        pin30_1, 
        pin31_2, 
        pin32_2,
        pin33_1, 
        pin34_1, 
        pin35_2, 
        pin36_2, 
        pin37_1, 
        pin38_1,
        pin39_2, 
        pin40_2, 
        pin41_1,
        pin42_1, 
        pin43_2,
        pin44_2, 
        pin45_1,
        pin46_1, 
        pin47_2, 
        pin48_2, 
        pin49_1,
        pin50_1, 
        pin51_2, 
        pin52_2, 
        pin53_1, 
        pin54_1, 
        pin55_2, 
        pin56_2, 
        pin57_1, 
        pin58_1, 
        pin59_2, 
        pin60_2, 
    ])
    db.session.commit()


def undo_pins_boards():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.pins_boards RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM pins_boards"))

    db.session.commit()