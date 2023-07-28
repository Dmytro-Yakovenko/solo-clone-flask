from app.models import db, Pin, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_pins():
    pin1 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=1,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690067475/pexels-kamila-bairam-12123657_bplmhe.jpg"
    )
    pin2 = Pin(
        title='Hot Dog',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 tablespoon olive oil\n 1 small red onion, thinly sliced\n 1 small red bell pepper, cored and sliced\n 1 small green bell pepper, cored and sliced \n Kosher salt and freshly ground black pepper \n 1 package APPLEGATE ORGANICS® THE GREAT ORGANIC UNCURED BEEF HOT DOG™ \n 6 hot dog buns \n6 slices American cheese \n',
        time="40 minutes",
        user_id=1,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin3 = Pin(
        title='Tacos',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='Meat /n 1 1/2 lbs Skirt steak /n Produce /n  1/2 cup Cilantro, fresh leaves /n  3 cloves Garlic /n  1 Lime, wedges /n  1 tsp Oregano, dried /n  3/4 cup Red onion /n Condiments /n  2 tbsp Lime juice, freshly squeezed/n  2 tbsp Soy sauce, reduced sodium, /n Baking & Spices  /n  2 tsp Chili powder /n Oils & Vinegars /n  2 tbsp Canola oil /n Nuts & Seeds /n  1 tsp Cumin, ground /n Bread & Baked Goods /n  12 Flour tortillas, mini',
        time="45 minutes",
        user_id=1,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690513127/854208a4b053bd13f651c919a198b251_qf95yh.jpg"
    )
    pin4 = Pin(
        title='Burrito',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=1,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690513313/a00406d2ca909de27457a9f416d463e0_ku5e8r.jpg"
    )
    pin5 = Pin(
        title='Kung Pao Chicken',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=1,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690513417/6353477103d26a73315e157b508bb248_yu2lpz.jpg"
    )
    pin6 = Pin(
        title='Peking Duck',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=1,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690513542/ef24648a867b29d00736e53940fa3a03_v9bkxn.jpg"
    )
    pin7 = Pin(
        title='Kimchi ',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin8 = Pin(
        title='Bulgogi',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin9 = Pin(
        title='Sushi',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin10 = Pin(
        title='Ramen',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin11 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin12 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin13 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin14 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin15 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin16 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin17 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin18 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin19 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin20 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin21 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin22 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin23 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin24 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin25 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin26 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin27 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin28 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin29 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin30 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    
    
    
    
    
    
    pin31 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin32 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin33 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin34 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin35 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin36 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin37 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin38 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin39 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin40 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin41 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin42 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin43 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin44 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin45 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin46 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin47 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin48 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin49 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin50 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin51 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin52 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin53 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin54 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin55 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin56 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin57 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin58 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin59 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin60 = Pin(
        title='Cheeseburger',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )

    db.session.add(pin1)
    db.session.add(pin2)
    db.session.add(pin3)
    db.session.add(pin4)
    db.session.add(pin5)
    db.session.add(pin6)
    db.session.add(pin7)
    db.session.add(pin8)
    db.session.add(pin9)
    db.session.add(pin10)
    
    
    db.session.add(pin11)
    db.session.add(pin12)
    db.session.add(pin13)
    db.session.add(pin14)
    db.session.add(pin15)
    db.session.add(pin16)
    db.session.add(pin17)
    db.session.add(pin18)
    db.session.add(pin19)
    db.session.add(pin20)
    
    db.session.add(pin21)
    db.session.add(pin22)
    db.session.add(pin23)
    db.session.add(pin24)
    db.session.add(pin25)
    db.session.add(pin26)
    db.session.add(pin27)
    db.session.add(pin28)
    db.session.add(pin29)
    db.session.add(pin30)
    
    db.session.add(pin31)
    db.session.add(pin32)
    db.session.add(pin33)
    db.session.add(pin34)
    db.session.add(pin35)
    db.session.add(pin36)
    db.session.add(pin37)
    db.session.add(pin38)
    db.session.add(pin39)
    db.session.add(pin40)
    
    db.session.add(pin41)
    db.session.add(pin42)
    db.session.add(pin43)
    db.session.add(pin44)
    db.session.add(pin45)
    db.session.add(pin46)
    db.session.add(pin47)
    db.session.add(pin48)
    db.session.add(pin49)
    db.session.add(pin50)
    
    db.session.add(pin51)
    db.session.add(pin52)
    db.session.add(pin53)
    db.session.add(pin54)
    db.session.add(pin55)
    db.session.add(pin56)
    db.session.add(pin57)
    db.session.add(pin58)
    db.session.add(pin59)
    db.session.add(pin60)
  
    db.session.commit()



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_pins():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.pins RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM pins"))
        
    db.session.commit()