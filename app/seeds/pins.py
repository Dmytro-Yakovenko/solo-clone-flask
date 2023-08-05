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
        description="Boil the hot dogs in water for 5 minutes. Preheat oven to 350°F (175°C), toast buns for 3-5 minutes. Place hot dogs in toasted buns. Add favorite toppings. Serve and enjoy!",
        ingredients='Hot dog buns. Hot dogs (beef, pork, or a mix). Your favorite toppings: ketchup, mustard, relish, chopped onions, sauerkraut, cheese, etc.',
        time="30 minutes",
        user_id=1,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690650186/c023e26e6d00b5b8d37c7aebb6b4111c_joqtef.jpg"
    )
    pin3 = Pin(
        title='Tacos',
        description="Cook onions and garlic. Add ground beef, cook until browned. Drain excess fat. Add taco seasoning and water, simmer. Prepare taco toppings. Warm taco shells. Fill shells with meat, add toppings.",
        ingredients=' 1 lb (450g) ground beef. 1 small onion (finely chopped). 2 cloves garlic (minced). 1 packet taco seasoning mix. 1/2 cup water. Salt and pepper to taste. Taco shells or soft tortillas. Shredded lettuce. Diced tomatoes. Shredded cheese. Sour cream (optional). Salsa (optional). Sliced jalapenos (optional).',
        time="45 minutes",
        user_id=1,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691254933/9434ad0f6de508d27e8f3cea42d51376_fcp8pv.jpg"
    )
    pin4 = Pin(
        title='Burrito',
        description=" Cook onions and garlic. Add ground beef, cook until browned. Drain excess fat. Add taco seasoning and water, simmer. Warm flour tortillas. Add rice, beans, meat, cheese, sour cream, salsa, guacamole (if using), lettuce, tomatoes, jalapenos (if desired), and cilantro. Fold and roll the tortillas to make burritos. Serve and enjoy!",
        ingredients='1 lb (450g) ground beef, 1 small onion (finely chopped), 2 cloves garlic (minced), 1 packet taco seasoning mix, 1/2 cup water, Salt and pepper to taste, Flour tortillas (burrito-sized), Cooked white rice, Cooked black beans (or refried beans), Shredded cheese, Sour cream, Salsa, Guacamole (optional), Chopped lettuce, Diced tomatoes, Sliced jalapenos (optional), Chopped cilantro (optional).',
        time="45 minutes",
        user_id=1,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690513313/a00406d2ca909de27457a9f416d463e0_ku5e8r.jpg"
    )
    pin5 = Pin(
        title='Kung Pao Chicken',
        description="In a wok or large skillet, heat the vegetable oil over medium-high heat. Add the chicken pieces and stir-fry until they are browned and cooked through. Remove the chicken from the wok and set it aside. In the same wok, add a bit more oil if needed, and stir-fry the dried red chilies until they become fragrant. Be careful not to burn them. Add the minced garlic, ginger, and the white parts of the green onions. Stir-fry for a minute until aromatic. Return the cooked chicken to the wok and add the unsalted peanuts. Toss everything together. In a small bowl, mix the soy sauce, dark soy sauce, Chinese rice wine, vinegar, hoisin sauce, sugar, and cornstarch slurry. Pour the sauce mixture over the chicken and peanuts in the wok. Stir-fry for a couple of minutes until the sauce thickens and coats the ingredients evenly. Add the green parts of the sliced green onions and give it a final toss. Serve the Kung Pao Chicken over steamed white rice. Enjoy your delicious Kung Pao Chicken!",
        ingredients='1 lb (450g) boneless, skinless chicken breasts (cut into bite-sized pieces). 2 tablespoons vegetable oil. 1/2 cup unsalted peanuts. 3-4 dried red chilies (or more for spicier, deseeded and cut into halves). 3 cloves garlic (minced). 1-inch piece of fresh ginger (minced). 3 green onions (sliced, white and green parts separated). 2 tablespoons soy sauce. 1 tablespoon dark soy sauce (or substitute with more regular soy sauce). 1 tablespoon Chinese rice wine or dry sherry. 1 tablespoon vinegar (rice vinegar or Chinese black vinegar). 1 tablespoon hoisin sauce. 1 teaspoon sugar. 1 teaspoon cornstarch (mixed with 2 tablespoons water to make a slurry). Steamed white rice (for serving).',
        time="45 minutes",
        user_id=1,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690513417/6353477103d26a73315e157b508bb248_yu2lpz.jpg"
    )
    pin6 = Pin(
        title='Peking Duck',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 whole duck (about 5-6 pounds). 2 tablespoons maltose or honey. 2 tablespoons soy sauce. 1 tablespoon Chinese five-spice powder. 1 tablespoon rice wine or dry sherry. 2 teaspoons sesame oil. 2 inches ginger (sliced). 4 green onions (cut into halves). 1 tablespoon white vinegar. Hoisin sauce (for serving). Thinly sliced cucumber and green onions (for serving). Pancakes or steamed buns (for serving).',
        time="45 minutes",
        user_id=1,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690513542/ef24648a867b29d00736e53940fa3a03_v9bkxn.jpg"
    )
    pin7 = Pin(
        title='Sushi',
        description="Rinse the sushi rice in cold water until the water runs clear. Drain the rice. In a saucepan, combine the rice and water, and bring it to a boil. Reduce the heat to low, cover, and cook for 15 minutes. Remove from heat and let it rest for another 10 minutes. In a small bowl, mix the rice vinegar, sugar, and salt until dissolved. Heat the mixture in the microwave for a few seconds to warm it. Transfer the cooked rice to a large bowl and drizzle the vinegar mixture over it. Gently fold and mix the rice to evenly coat it with the vinegar seasoning. Lay a bamboo sushi rolling mat on a clean surface. Place a sheet of plastic wrap on the mat to prevent sticking. Lay a sheet of nori on the plastic wrap with the shiny side down. Wet your fingers to prevent the rice from sticking and spread a thin, even layer of sushi rice over the nori, leaving a small border at the top. Arrange the fish, avocado, and cucumber in a line across the center of the rice. Using the bamboo mat, start rolling the sushi away from you, using gentle pressure to shape it. Moisten the border of the nori sheet with water to seal the roll. Continue rolling until the entire nori sheet is wrapped around the fillings. Slice the sushi roll into bite-sized pieces using a sharp knife. Serve the sushi with pickled ginger, wasabi paste, and soy sauce for dipping. Enjoy your homemade sushi!",
        ingredients='2 cups sushi rice (short-grain Japanese rice). 2 1/2 cups water. 1/3 cup rice vinegar. 2 tablespoons sugar. 1 teaspoon salt. Nori sheets (seaweed sheets). Fresh fish (salmon, tuna, etc.), sliced into strips. Avocado, sliced. Cucumber, sliced into thin strips. Pickled ginger (gari). Wasabi paste. Soy sauce (for dipping).',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690649338/efca2616e091e0d86892c94961c0be61_af97jf.jpg"
    )
    pin8 = Pin(
        title='Ramen',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='1 lb (450g) ground beef (80% lean is a good choice for juiciness)\nSalt and pepper to taste\n4 hamburger buns/n4 slices of cheese (American, cheddar, or your preferred type)\nOptional toppings: lettuce, tomato slices, onion slices, pickles, ketchup, mustard, mayonnaise, etc.',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690649598/e7a055c298143b479ade0bda6bd53dcf_wcbsqy.jpg"
    )
    pin9 = Pin(
        title='Miso Soup',
        description="In a saucepan, bring the dashi stock to a gentle simmer over medium heat. Dissolve the miso paste in a small bowl with some of the hot dashi stock, ensuring there are no lumps. Add the dissolved miso paste back to the saucepan and stir to combine. Add the cubed tofu and simmer for a few minutes until the tofu is heated through. If using, add soy sauce and mirin for additional flavor. Ladle the miso soup into serving bowls. Garnish each bowl with sliced green onions and nori strips. Drizzle a little sesame oil over each bowl if desired. Serve the miso soup hot and enjoy its comforting flavors!",
        ingredients='4 cups dashi stock (or vegetable broth for a vegetarian option). 3 tablespoons miso paste (white or red miso, to taste). 1/2 cup cubed tofu. 2 green onions (sliced). 1 sheet nori (seaweed), cut into thin strips. 1 tablespoon soy sauce (optional, for added depth of flavor). 1 tablespoon mirin (optional, for a hint of sweetness). 1 teaspoon sesame oil (optional, for extra richness).',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690650391/dc872932570ac88f164fd2715c3f6a84_sil2r1.jpg"
    )
    pin10 = Pin(
        title='Kimchi',
        description="Cut the Napa cabbage into quarters lengthwise and remove the core. Chop the cabbage into bite-sized pieces. Dissolve the sea salt in water to create a brine. Soak the cabbage in the brine, making sure it's fully submerged, and let it sit for 2-3 hours to wilt. Rinse the cabbage thoroughly under cold water to remove excess salt. Drain well and squeeze out any excess water. In a mixing bowl, combine grated ginger, minced garlic, sugar, fish sauce (or soy sauce), and Korean red pepper flakes to create the kimchi paste. Add the sliced green onions and julienned carrot to the kimchi paste, mixing everything together. Gently massage the kimchi paste onto the wilted cabbage, ensuring it's evenly coated. Pack the kimchi into a clean glass jar or an airtight container, pressing it down to remove air pockets. Leave some space at the top of the container and seal it tightly. Let the kimchi ferment at room temperature for 1-2 days, then refrigerate it to slow down the fermentation process. The kimchi will continue to develop its flavor over time, and it can be stored in the refrigerator for several weeks",
        ingredients='1 medium Napa cabbage (about 2 pounds). 1/4 cup sea salt. 4 cups water. 1 tablespoon grated ginger. 4 cloves garlic (minced). 1 tablespoon sugar. 3 tablespoons fish sauce (for a vegetarian version, use soy sauce). 3 tablespoons Korean red pepper flakes (gochugaru). 4 green onions (sliced). 1 small carrot (julienned).',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690650776/ff944099cfa3072a27f2ed9b913545c3_hdytmj.jpg"
    )
    pin11 = Pin(
        title='Korean Beef Bulgogi',
        description="In a bowl, mix soy sauce, brown sugar, sesame oil, rice wine, minced garlic, grated onion, and grated ginger to make the marinade. Add the sliced beef to the marinade, making sure it's well coated. Cover the bowl with plastic wrap and let the beef marinate in the fridge for at least 1 hour (for best results, marinate overnight). In a large skillet or wok, heat vegetable oil over medium-high heat. Add the marinated beef and stir-fry until it's cooked through and caramelized. Sprinkle sliced green onions and sesame seeds on top for garnish (optional). Serve the beef bulgogi over cooked rice and enjoy the delicious flavors!",
        ingredients='1 lb (450g) thinly sliced beef (ribeye or sirloin). 1/4 cup soy sauce. 2 tablespoons brown sugar. 2 tablespoons sesame oil. 1 tablespoon rice wine or mirin. 3 cloves garlic (minced). 1 small onion (grated). 1 tablespoon grated ginger. 2 green onions (sliced). 1 tablespoon sesame seeds (for garnish, optional). 1 tablespoon vegetable oil (for cooking). Cooked rice (for serving).',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690651032/3c6dc3a9e7c9358198c91630a9f6d717_zejs0k.jpg"
    )
    pin12 = Pin(
        title='Bibimbap! (Korean Rice Bowl)',
        description="Prepare all the ingredients as described above and set them aside. In a large skillet, heat vegetable oil over medium-high heat and stir-fry the marinated beef or chicken until cooked through. Set aside. In the same skillet, add 1 tablespoon of sesame oil and stir-fry the carrots, spinach, bean sprouts, and shiitake mushrooms separately, seasoning each with their respective ingredients. Set aside. Divide the cooked rice into individual serving bowls. Arrange the cooked beef or chicken, sautéed vegetables, and fried eggs on top of the rice in separate sections. Drizzle the remaining 1 tablespoon of sesame oil over the ingredients. Serve the bibimbap with gochujang on the side for each person to mix in according to their spice preference. Garnish with sesame seeds and sliced green onions. To eat, mix all the ingredients together thoroughly, incorporating the gochujang to flavor the rice. Enjoy your delicious and colorful Bibimbap!",
        ingredients='2 cups cooked short-grain rice. 1 cup thinly sliced beef or chicken (marinated in soy sauce, sugar, sesame oil, and garlic). 1 cup julienned carrots (quickly sautéed in sesame oil). 1 cup spinach (quickly blanched and seasoned with sesame oil and salt). 1 cup bean sprouts (blanched and seasoned with sesame oil, soy sauce, and garlic). 1 cup sliced shiitake mushrooms (sautéed with soy sauce and sugar). 2 large eggs (fried sunny-side-up). 1 tablespoon vegetable oil. 2 tablespoons sesame oil (divided). 2 tablespoons gochujang (Korean red pepper paste). 1 tablespoon sesame seeds (for garnish, optional). 2-3 green onions (sliced, for garnish).',
        time="45 minutes",
        user_id=2,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690651282/db71a68c89a60bbd424842ea9b833cb5_jx4n9z.jpg"
    )
    pin13 = Pin(
        title='Baguette',
        description="In a large mixing bowl, combine the bread flour and salt. In a separate small bowl, mix the active dry yeast with warm water and let it sit for a few minutes until it becomes frothy. Pour the yeast mixture into the flour mixture and mix until a dough forms. Knead the dough on a floured surface for about 10 minutes, or until it becomes smooth and elastic. Place the dough in a lightly oiled bowl, cover with a clean cloth, and let it rise in a warm place for about 1 hour or until doubled in size. Preheat your oven to 220°C (425°F) and place a baking pan with water at the bottom of the oven to create steam. Punch down the risen dough and shape it into a baguette by rolling it out into a long, thin loaf. Place the shaped baguette on a baking sheet lined with parchment paper or a baguette pan. Using a sharp knife or blade, make diagonal slashes along the top of the baguette. Bake the baguette in the preheated oven for about 20-25 minutes or until it turns golden brown and sounds hollow when tapped on the bottom. Remove the baguette from the oven and let it cool on a wire rack before slicing and serving.",
        ingredients='500g bread flour. 10g salt. 7g active dry yeast. 350ml warm water.',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690651399/e35ae4b38146c657fb2c7332c56fbbfd_ruz7m3.jpg"
    )
    pin14 = Pin(
        title='Croissant',
        description="In a large mixing bowl, combine flour, sugar, salt, and active dry yeast. Gradually add warm milk and knead until a smooth dough forms. Roll out the dough into a rectangle. Place the cold butter in the center and fold the dough over it, sealing the edges. Roll the dough into a long rectangle and fold it in thirds like a letter. Repeat this process twice, then chill the dough for 30 minutes. Roll the dough into a large rectangle and cut it into triangles. Roll each triangle into a croissant shape. Let the croissants rise for 1-2 hours. Preheat the oven to 200°C (400°F). Brush the croissants with egg wash. Bake for 15-20 minutes or until golden brown. Enjoy your delicious homemade croissants!",
        ingredients='500g all-purpose flour. 50g granulated sugar. 10g salt. 10g active dry yeast. 250ml warm milk. 250g unsalted butter (cold). 1 large egg (for egg wash).',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690651901/92ea6aadb018259547f9c939dfb1c9fb_buxb7s.jpg"
    )
    pin15 = Pin(
        title='Pizza',
        description="In a large mixing bowl, combine flour, active dry yeast, sugar, and salt. Gradually add warm water and olive oil, then knead the dough until smooth. Cover the dough and let it rise for 1-2 hours. Preheat your oven to 220°C (425°F). Roll out the pizza dough to your desired thickness and place it on a pizza stone or baking sheet. Spread pizza sauce evenly over the dough, leaving a small border around the edges. Sprinkle shredded mozzarella cheese over the sauce. Add your favorite pizza toppings on top. Bake the pizza in the preheated oven for 12-15 minutes or until the crust is golden brown and the cheese is bubbly and slightly browned. Remove the pizza from the oven and let it cool for a minute. Slice and serve your delicious homemade pizza!",
        ingredients='2 1/4 cups all-purpose flour. 1 packet (7g) active dry yeast. 1 teaspoon sugar. 3/4 cup warm water. 2 tablespoons olive oil. 1 teaspoon salt. 1/2 cup pizza sauce. 2 cups shredded mozzarella cheese. Your favorite pizza toppings (e.g., pepperoni, mushrooms, bell peppers, onions, olives, etc.).',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690651993/d1862b5bcf4183b48db35819322ebc95_nybqnn.jpg"
    )
    pin16 = Pin(
        title='Pasta',
        description="In a large pot, bring 4 quarts of water to a boil. Add 1 tablespoon of salt to the boiling water. Add the dried pasta to the boiling water and cook according to the package instructions until al dente (usually around 8-10 minutes). While the pasta is cooking, heat your desired pasta sauce in a separate saucepan over low heat. Once the pasta is cooked, drain it in a colander, reserving a small amount of pasta water if needed for the sauce. Add the cooked pasta to the warm pasta sauce and toss it to coat the pasta evenly. If the sauce is too thick, add a little reserved pasta water to reach your preferred consistency. Serve the pasta on individual plates or in a large serving bowl. Optionally, sprinkle grated Parmesan cheese and fresh basil or parsley on top for added flavor and presentation. Enjoy your delicious and comforting pasta dish!",
        ingredients='8 ounces (226g) dried pasta (e.g., spaghetti, penne, fettuccine, etc.). 4 quarts (3.8 liters) water. 1 tablespoon salt (for cooking pasta). Your choice of pasta sauce (e.g., marinara, Alfredo, pesto, etc.). Grated Parmesan cheese (optional, for serving). Fresh basil or parsley (optional, for garnish).',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690652125/e6feff3970dff16aaaba8c334ca11947_uvdgni.jpg"
    )
    pin17 = Pin(
        title='Classic Borscht(Beat Soup)',
        description="Peel and chop beets, cabbage, potatoes, carrots, and onion into small pieces. In a large pot, sauté chopped onion and garlic until softened. Add tomato paste and stir for a minute. Pour in the vegetable or beef broth and bring it to a boil. Add the chopped beets, potatoes, carrots, and cabbage to the pot. Add bay leaves, vinegar, sugar, salt, and pepper. Reduce heat and simmer until the vegetables are tender, usually for about 30-40 minutes. Adjust seasoning to taste. Serve the Classic Borscht hot, optionally garnished with a dollop of sour cream and a sprinkle of fresh dill. Enjoy the hearty and vibrant flavors of this traditional Ukrainian beet soup!",
        ingredients='2 medium beets (peeled and grated). 1 small onion (finely chopped). 1 large potato (peeled and diced). 1 carrot (peeled and grated). 2 cups shredded cabbage. 4 cups beef or vegetable broth. 2 tablespoons tomato paste. 2 tablespoons vegetable oil. 2 cloves garlic (minced). 2 bay leaves. 1 tablespoon vinegar. Salt and pepper to taste. Sour cream and fresh dill (for serving).',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690652616/a83e8531df9c1baef0303708878fc74f_zcxc8w.jpg"
    )
    pin18 = Pin(
        title='Ukrainian Pork Lard (Salo) ',
        description="Cut fresh pork fat (salo) into thin slices or small chunks. Rub the salo with garlic, salt, and pepper, and optionally add paprika, herbs, or spices for additional taste. Place the seasoned salo in a container or jar, covering each layer with the seasoning mixture. Close the container tightly and refrigerate for at least a few days to let the flavors infuse. Ukrainian Pork Lard (Salo) is traditionally served sliced thinly and enjoyed with bread or as a condiment to add rich and savory flavor to various dishes. Note: Salo is a popular and traditional Ukrainian delicacy, but it's important to consume it in moderation due to its high-fat content.",
        ingredients='Fresh pork fat (salo). Garlic. Salt. Pepper. Optional: paprika, herbs, or spices for added flavor.',
        time="45 minutes",
        user_id=3,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690652767/3723ae1df11a8985ad2787ff423365cb_k5zwsa.jpg"
    )
    pin19 = Pin(
        title='Greek Salad',
        description="In a large salad bowl, combine the tomato chunks, sliced cucumber, thinly sliced red onion, chopped green bell pepper, and pitted Kalamata olives. In a small bowl, whisk together the extra-virgin olive oil, red wine vinegar, dried oregano, salt, and pepper to make the dressing. Pour the dressing over the salad ingredients and toss gently to coat everything evenly. Sprinkle the crumbled feta cheese over the salad. Optionally, garnish with fresh parsley for added freshness and presentation. Serve the Greek Salad immediately or refrigerate for a while to let the flavors meld. Enjoy this light and refreshing salad as a side dish or a light meal on its own!",
        ingredients='2 large tomatoes (cut into chunks). 1 cucumber (peeled and sliced). 1 small red onion (thinly sliced). 1 green bell pepper (seeded and chopped). 1/2 cup Kalamata olives (pitted). 1/2 cup crumbled feta cheese. 2 tablespoons extra-virgin olive oil. 1 tablespoon red wine vinegar. 1 teaspoon dried oregano. Salt and pepper to taste. Fresh parsley (for garnish, optional).',
        time="25 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690652851/d267d97236d163d7a24ddd4693d85abe_ri2hnv.jpg"
    )
    pin20 = Pin(
        title='Humus',
        description=" In a food processor, blend chickpeas, tahini, lemon juice, minced garlic, olive oil, ground cumin, and a pinch of salt until smooth. While blending, gradually add water until the hummus reaches your desired creamy consistency. Taste and adjust seasoning with more salt or lemon juice if needed. Transfer the hummus to a serving bowl. Optionally, drizzle olive oil and sprinkle paprika on top for garnish. Serve the hummus with pita bread, fresh vegetables, or as a dip for your favorite snacks.",
        ingredients='1 can (15 oz) chickpeas (garbanzo beans), drained and rinsed. 1/4 cup tahini (sesame paste). 3 tablespoons lemon juice. 2 cloves garlic (minced). 2 tablespoons olive oil. 1/2 teaspoon ground cumin. Salt to taste. 2-3 tablespoons water (adjust for desired consistency). Paprika and olive oil (for garnish, optional).',
        time="45 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690652951/5e0300ee582fcfe3fc05190993f151b2_d5p39j.jpg"
    )
    pin21 = Pin(
        title='Dolmas',
        description="In a large mixing bowl, combine uncooked rice, chopped onion, fresh dill, fresh mint, fresh parsley, lemon juice, olive oil, water, salt, black pepper, ground cumin, ground coriander, ground cinnamon, ground allspice, and ground cloves. Gently separate the grape leaves and remove any stems. Place a grape leaf flat on a clean surface, shiny side down. Spoon about 1 tablespoon of the rice mixture onto the center of the leaf. Fold the bottom of the leaf over the filling, then fold the sides inward, and roll it tightly into a small cylinder. Repeat the process with the remaining grape leaves and filling. Place the dolmas in a large pot, seam side down, in a single layer. Add enough water to cover the dolmas, then place a heat-resistant plate on top to keep them submerged. Bring the water to a boil, then reduce the heat to low, cover the pot, and let the dolmas simmer for about 45 minutes to 1 hour or until the rice is fully cooked. Remove the dolmas from the pot and let them cool. Serve the dolmas cold or at room temperature as an appetizer or side dish.",
        ingredients=' 1 jar (about 8 oz) grape leaves, drained and rinsed (or fresh grape leaves, blanched). 1 cup long-grain white rice (uncooked). 1/2 cup chopped onion. 1/4 cup chopped fresh dill. 1/4 cup chopped fresh mint. 1/4 cup chopped fresh parsley. 1/4 cup lemon juice. 1/4 cup olive oil. 1/4 cup water. 1 teaspoon salt. 1/2 teaspoon black pepper. 1/2 teaspoon ground cumin. 1/2 teaspoon ground coriander. 1/4 teaspoon ground cinnamon. 1/4 teaspoon ground allspice. 1/4 teaspoon ground cloves.',
        time="45 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690653042/2ac6d8d1a6a1a684433f096b6cf792be_sb3erz.jpg"
    )
    pin22 = Pin(
        title='Falafel',
        description="Drain and rinse the soaked chickpeas. In a food processor, combine chickpeas, chopped onion, garlic, parsley, cilantro, ground cumin, ground coriander, baking soda, salt, and pepper. Process the mixture until finely ground and it forms a thick paste. Transfer the falafel mixture to a bowl, cover, and refrigerate for at least 1 hour to firm up. Shape the chilled falafel mixture into small balls or patties. In a deep skillet or pot, heat vegetable oil over medium-high heat. Fry the falafel in batches until golden brown and crispy on all sides. Remove the falafel from the oil and place them on a plate lined with paper towels to drain any excess oil. Serve the falafel hot with pita bread, hummus, tahini sauce, fresh vegetables, and your favorite toppings.",
        ingredients='1 cup dried chickpeas (soaked overnight). 1 small onion (roughly chopped). 3-4 cloves garlic. 1/4 cup fresh parsley leaves. 1/4 cup fresh cilantro leaves. 1 teaspoon ground cumin. 1 teaspoon ground coriander. 1/2 teaspoon baking soda. Salt and pepper to taste. Vegetable oil (for frying).',
        time="45 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690653125/21d6698c065c29cf5b78740c461f4ae6_t05rnx.jpg"
    )
    pin23 = Pin(
        title='Eggplant Parmesan',
        description="Preheat the oven to 375°F (190°C). Sprinkle salt on the eggplant slices and let them sit for 20-30 minutes to release excess moisture. Pat the eggplant slices dry with paper towels. Set up three shallow bowls - one with flour, one with beaten eggs, and one with a mixture of breadcrumbs and grated Parmesan cheese. Dredge each eggplant slice in flour, dip it in beaten eggs, and coat it with the breadcrumb-Parmesan mixture. In a large skillet, heat olive oil over medium heat. Fry the breaded eggplant slices in batches until golden brown on both sides. Place the fried eggplant slices on a paper towel-lined plate to remove any excess oil. In a baking dish, spread a thin layer of marinara sauce. Arrange a layer of fried eggplant slices on top of the sauce. Sprinkle shredded mozzarella cheese over the eggplant layer. Repeat the layers until all the eggplant slices are used, finishing with a layer of mozzarella on top. Bake in the preheated oven for 25-30 minutes or until the cheese is melted and bubbly. Garnish with fresh basil leaves if desired. Serve the Eggplant Parmesan hot, alongside pasta or crusty bread, and enjoy this delicious Italian classic!",
        ingredients='2 large eggplants (sliced into 1/2-inch rounds). 2 cups all-purpose flour. 4 large eggs (beaten). 2 cups breadcrumbs (Italian seasoned or plain). 1 cup grated Parmesan cheese. 2 cups marinara sauce. 2 cups shredded mozzarella cheese. Fresh basil leaves (for garnish, optional). Salt and pepper to taste. Olive oil (for frying).',
        time="45 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690653309/93e44d6e0db8bd100be26ccaf379195d_t8fzcs.jpg"
    )
    pin24 = Pin(
        title='caprese salad',
        description="Slice the tomatoes and mozzarella cheese into equal-sized rounds. Arrange them alternately on a serving plate. Tuck fresh basil leaves between the tomato and mozzarella slices. Drizzle extra virgin olive oil and balsamic vinegar or glaze over the salad. Season with a pinch of salt and freshly ground black pepper. Serve the Caprese Salad immediately and enjoy the delightful combination of flavors in this classic Italian dish!",
        ingredients='Fresh ripe tomatoes. Fresh mozzarella cheese. Fresh basil leaves. Extra virgin olive oil. Balsamic vinegar or balsamic glaze. Salt. Pepper.',
        time="25 minutes",
        user_id=4,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690653427/08f9e4cf15c6d2214f8bd6860b160f9b_zwigmx.jpg"
    )
    pin25 = Pin(
        title='BBQ Ribs',
        description="Preheat the oven to 275°F (135°C). Remove the membrane from the back of the ribs. In a bowl, mix brown sugar, paprika, garlic powder, onion powder, salt, and black pepper to create a dry rub. Rub the dry mixture all over the ribs, covering them thoroughly. Wrap each rack of ribs tightly in aluminum foil and place them on a baking sheet. Bake the ribs in the preheated oven for 2.5 to 3 hours or until tender. Preheat your grill to medium-high heat. Unwrap the ribs and place them on the grill. Brush BBQ sauce generously over the ribs. Grill the ribs for 5-10 minutes, flipping and basting with more BBQ sauce occasionally until they have a nice caramelized glaze. Remove the ribs from the grill, let them rest for a few minutes, then cut them between the bones and serve.",
        ingredients=' 2 racks of baby back ribs. 1 cup BBQ sauce. 1/4 cup brown sugar. 1 tablespoon paprika. 1 tablespoon garlic powder. 1 tablespoon onion powder. 1 teaspoon salt. 1 teaspoon black pepper.',
        time="55 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690653630/bd1aff11314f5a4eabde66adcb75f2fc_omgs5h.jpg"
    )
    pin26 = Pin(
        title='Baked Buffalo Wings',
        description="Preheat the oven to 450°F (230°C). Pat the chicken wings dry with paper towels. In a bowl, mix baking powder, salt, garlic powder, and black pepper. Toss the wings in the dry mixture until evenly coated. Place the coated wings on a baking rack set on top of a baking sheet. Bake the wings in the preheated oven for 40-45 minutes or until crispy and golden brown, flipping them halfway through. In a separate bowl, combine hot sauce and melted butter to make the Buffalo sauce. Once the wings are done baking, toss them in the Buffalo sauce until fully coated. Serve the Baked Buffalo Wings with ranch or blue cheese dressing and celery sticks on the side.",
        ingredients=" 2 pounds chicken wings. 2 tablespoons baking powder. 1 teaspoon salt. 1 teaspoon garlic powder. 1/2 teaspoon black pepper. 1/2 cup hot sauce (such as Frank's RedHot). 1/4 cup unsalted butter (melted). Ranch or blue cheese dressing (for serving). Celery sticks (for serving).",
        time="45 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690653778/8c5fd037e965835ec4e02f1f02026805_rditq0.jpg"
    )
    pin27 = Pin(
        title='Salsa',
        description="In a bowl, combine diced tomatoes, chopped red onion, jalapeño, cilantro, minced garlic, and lime juice. Season with salt and pepper to taste. Mix well and let the flavors meld together in the refrigerator for at least 30 minutes before serving. Enjoy the fresh and tangy Salsa with tortilla chips, tacos, burritos, or as a flavorful topping for your favorite dishes!",
        ingredients='4 ripe tomatoes (diced). 1/2 red onion (finely chopped). 1 jalapeño (seeds removed and finely chopped). 1/4 cup fresh cilantro leaves (chopped). 1 clove garlic (minced). 1 lime (juiced). Salt and pepper to taste.',
        time="35 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690653888/52a0ba6316618683ad1595d89d348f91_yzsaym.jpg"
    )
    pin28 = Pin(
        title='Quesadillas',
        description="On half of each flour tortilla, sprinkle a layer of shredded cheese, cooked and shredded chicken (if using), diced bell peppers, diced onions, chopped cilantro, ground cumin, chili powder, salt, and pepper. Fold the tortillas in half to enclose the filling. Heat a skillet or griddle over medium heat and lightly grease it with cooking spray or butter. Cook the quesadillas for 2-3 minutes on each side or until the tortillas are golden brown and the cheese is melted. Repeat with the remaining quesadillas. Slice the cooked quesadillas into wedges and serve them hot with salsa, guacamole, sour cream, or your favorite dipping sauce.",
        ingredients='8 flour tortillas. 2 cups shredded cheese (such as cheddar, Monterey Jack, or a blend). 1 cup cooked and shredded chicken (optional). 1/2 cup diced bell peppers. 1/2 cup diced onions. 1/4 cup chopped cilantro. 1 teaspoon ground cumin. 1/2 teaspoon chili powder. Salt and pepper to taste. Cooking spray or butter.',
        time="45 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690654274/8edeaa6802c8427cae0f0f3eb312044e_msvh6y.jpg"
    )
    pin29 = Pin(
        title='Sweet And Sour Pork',
        description="In a bowl, combine cornstarch, flour, salt, and black pepper. In another bowl, whisk together the egg and water to make a batter. Dip the pork pieces into the batter, then coat them with the cornstarch mixture. In a deep skillet or wok, heat vegetable oil over medium-high heat. Fry the battered pork pieces until they are golden and crispy. Remove the pork from the oil and place them on a paper towel-lined plate to drain any excess oil. In the same skillet, sauté chopped bell peppers and onions until they are slightly softened. Add pineapple chunks, ketchup, rice vinegar, soy sauce, and brown sugar to the skillet. Stir in the dissolved cornstarch to thicken the sauce. Add the fried pork pieces back to the skillet and toss them in the sweet and sour sauce until fully coated. Serve the Sweet and Sour Pork over steamed rice and garnish with green onions or sesame seeds, if desired.",
        ingredients='1 pound pork loin (cut into bite-sized pieces). 1/2 cup cornstarch. 1/4 cup all-purpose flour. 1/2 teaspoon salt. 1/4 teaspoon black pepper. 1 egg. 1/4 cup water. Vegetable oil (for frying). 1/2 cup chopped bell peppers (assorted colors). 1/2 cup chopped onions. 1 cup pineapple chunks (fresh or canned). 1/4 cup ketchup. 1/4 cup rice vinegar. 2 tablespoons soy sauce. 2 tablespoons brown sugar. 1 tablespoon cornstarch (dissolved in 1/4 cup water).',
        time="45 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690654626/33dd5f4eb08209ddbb4eb4741c681139_oih8o4.jpg"
    )
    pin30 = Pin(
        title='Dumplings',
        description="In a large bowl, mix flour and water to form a dough, then knead until smooth. In a separate bowl, combine ground pork or chicken, chopped cabbage, green onions, soy sauce, sesame oil, grated ginger, minced garlic, salt, and pepper to create the dumpling filling. Take a small portion of the dough and roll it into a thin circle, or use store-bought dumpling wrappers. Place a spoonful of the filling in the center of each wrapper, then fold and pleat the edges to seal the dumplings. In a steamer or a large pan with a lid, bring water to a boil. Place the dumplings in the steamer or pan and steam for about 10-15 minutes, or until the dumplings are cooked through and the wrappers become translucent. Serve the Dumplings hot with dipping sauces like soy sauce, black vinegar, or chili oil, and enjoy these delightful bite-sized treats!",
        ingredients='1 cup all-purpose flour. 1/2 cup water. 1/2 pound ground pork or chicken. 1/2 cup finely chopped cabbage. 2 green onions (finely chopped). 1 tablespoon soy sauce. 1 tablespoon sesame oil. 1 teaspoon grated ginger. 2 cloves garlic (minced). Salt and pepper to taste. Dumpling wrappers (store-bought or homemade).',
        time="45 minutes",
        user_id=5,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690654707/701c72b1173ae903e046afeecd39b4ba_xdxq4z.jpg"
    )
    
    
    
    
    
    
    pin31 = Pin(
        title='Sashimi',
        description="Slice the raw fish into thin, bite-sized pieces. Arrange the sashimi slices on a serving platter. Serve with wasabi, soy sauce, and pickled ginger on the side. Enjoy the fresh and delicate flavors of Sashimi, a traditional Japanese dish that highlights the natural taste of the fish!",
        ingredients='Fresh and high-quality raw fish (such as tuna, salmon, yellowtail, or whitefish). Wasabi (for serving). Soy sauce (for serving). Pickled ginger (for serving).',
        time="45 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690654889/6009a1ccb4b9724e6b7377e54ecb979d_mlpo2r.jpg"
    )
    pin32 = Pin(
        title='Unagi',
        description="In a saucepan, combine soy sauce, mirin, sugar, sake, grated ginger, and minced garlic, then bring the mixture to a simmer over medium heat until the sugar dissolves. Preheat the grill or broiler. Place the unagi fillets on the grill or broiler pan, skin-side down, and brush the sauce generously over the eel. Grill or broil the unagi for 2-3 minutes on each side, brushing with more sauce occasionally until the eel is nicely glazed and heated through. Serve the Unagi over steamed rice, drizzle with more sauce if desired, and garnish with toasted sesame seeds and sliced green onions. Enjoy the succulent and flavorful taste of Grilled Eel, a popular dish in Japanese cuisine!",
        ingredients=' 2 unagi fillets (fresh or frozen, deboned and sliced into pieces if whole). 1/4 cup soy sauce. 1/4 cup mirin (sweet rice wine). 2 tablespoons sugar. 1 tablespoon sake (Japanese rice wine). 1 teaspoon grated fresh ginger. 1 clove garlic (minced). Steamed rice (for serving). Toasted sesame seeds and sliced green onions (for garnish).',
        time="35 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690655006/9f4d889c2754c37df8e677c33e7d2616_igd97b.jpg"
    )
    pin33 = Pin(
        title='Quiche Lorraine',
        description="Preheat oven to 375°F (190°C). Roll out pie crust and fit into a 9-inch pie dish. Whisk eggs, heavy cream, salt, pepper, and nutmeg. Sprinkle bacon and cheese in crust. Pour egg mixture over. Bake for 35-40 minutes until set and lightly browned. Cool slightly before serving.Enjoy the savory and delightful flavors of Quiche Lorraine, a classic French dish that's perfect for any meal of the day!",
        ingredients='1 pre-made pie crust. 6-8 slices of bacon (cooked and crumbled). 1 cup shredded Swiss or Gruyere cheese. 4 large eggs. 1 1/2 cups heavy cream or half-and-half. 1/2 teaspoon salt. 1/4 teaspoon black pepper. A pinch of ground nutmeg.',
        time="45 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690655118/03e973a0a2f37a05e8f473df4634bfc9_ehngp6.jpg"
    )
    pin34 = Pin(
        title='Tomato Tarte Tin',
        description="In a skillet, melt butter over medium heat, then add sugar and stir until it caramelizes. Add balsamic vinegar and stir until well combined. Arrange sliced tomatoes in the caramel mixture, season with salt, pepper, and fresh thyme. Roll out puff pastry and place it over the tomatoes, tucking the edges. Bake in a preheated oven at 375°F (190°C) for 25-30 minutes or until the puff pastry is golden and crisp. Invert the tarte onto a serving plate while it's still warm, so the tomatoes are on top.",
        ingredients='Puff pastry. Tomatoes. Butter. Sugar. Balsamic vinegar. Thyme. Salt. Pepper.',
        time="25 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690655450/b8c66cd467b6ac605cc933ed4aa9b0af_yb3uiy.jpg"
    )
    pin35 = Pin(
        title='Galbi',
        description="Marinate ribs in a mixture of soy sauce, sugar, sesame oil, minced garlic, grated ginger, sliced green onions, and black pepper, refrigerate for at least 2 hours (preferably overnight) to let flavors infuse. Grill the marinated short ribs for 2-3 minutes on each side, brushing with more marinade occasionally until they are nicely glazed and cooked through. Serve the Galbi with steamed rice for a delicious and savory Korean grilled short ribs experience!",
        ingredients=' Beef short ribs. Soy sauce. Sugar. Sesame oil. Garlic. Ginger. Green onions. Black pepper.',
        time="55 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690655621/1eae93d0464cdc1134980d4f619fa512_gjomfd.jpg"
    )
    pin36 = Pin(
        title='Mandu',
        description=" Finely chop cabbage, onions, and garlic, then mix them with the ground meat in a bowl. Season the mixture with soy sauce and sesame oil, adjusting to taste. Take a dumpling wrapper, place a spoonful of the filling in the center, moisten the edges with water, and fold it in half to seal. Continue making dumplings until all the filling is used. To cook, you can either steam them for 10-12 minutes or pan-fry them until they are golden and crispy. Serve Mandu with dipping sauce and enjoy these delicious Korean dumplings!",
        ingredients='Ground meat (pork or beef). Vegetables (cabbage, onions, garlic). Soy sauce. Sesame oil. Dumpling wrappers.',
        time="55 minutes",
        user_id=6,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690655712/0a08cb3ecd535a46f43a2962256acf56_gxb2ly.jpg"
    )
    pin37 = Pin(
        title='Risotto',
        description="In a saucepan, heat the chicken or vegetable broth and keep it warm on low heat. In a separate large saucepan, melt butter over medium heat, then sauté finely chopped onion until translucent. Add the Arborio rice to the saucepan and stir it until it's coated with the melted butter. Pour in white wine and cook, stirring frequently, until the wine is absorbed by the rice. Gradually add a ladleful of warm broth to the rice and stir until it's absorbed, repeating this process until the rice is creamy and cooked but still slightly firm (about 20 minutes). Stir in grated Parmesan cheese, salt, and pepper to taste. Serve immediately and savor the rich and creamy texture of this classic Italian risotto!",
        ingredients='Arborio rice. Chicken/vegetable broth. Butter. Onion. White wine. Parmesan cheese. Salt. Pepper.',
        time="45 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690656034/f940c5e8489a82f49f32492de819cd47_hrpfiw.jpg"
    )
    pin38 = Pin(
        title='Ravioli',
        description="Preheat your grill, stovetop griddle, or frying pan over medium-high heat\n Divide the ground beef into 4 equal portions, shaping each portion into a ball.\nFlatten each ball into a patty about 3/4 to 1 inch thick. Make a slight depression in the center of each patty to prevent it from puffing up during cooking.\nSeason both sides of the patties with salt and pepper.\nCook the patties on the grill or stovetop for about 4-5 minutes on each side or until they reach your desired level of doneness. If you prefer well-done burgers, you can cook them a little longer.\nDuring the last minute of cooking, add a slice of cheese on top of each patty and let it melt.\nWhile the patties are cooking, lightly toast the hamburger buns on the grill or stovetop until they are warm and slightly crispy.\nAssemble the burgers by placing a cooked patty with melted cheese on the bottom half of each bun.\nAdd your preferred toppings, such as lettuce, tomato slices, onions, pickles, ketchup, mustard, or mayonnaise.\nPlace the top half of the bun on the toppings to complete the cheeseburger.",
        ingredients='Ravioli pasta. Filling (cheese, meat, or vegetables). Sauce (tomato, cream, or butter).',
        time="35 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690656364/c29172ec796ae8e37f09724f84748df0_mv6hzz.jpg"
    )
    pin39 = Pin(
        title='Uzvar(ukrainian drink)',
        description=" In a pot, boil dried fruits, honey, cinnamon, and cloves in water until the fruits are soft and flavors meld. Strain the Uzvar and serve it hot or cold. Enjoy this traditional and flavorful Ukrainian drink!",
        ingredients='Dried fruits (apples, pears, prunes). Water. Honey. Cinnamon. Cloves.',
        time="45 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690656499/15fdb65a50fb775432e2650273c266d1_kmwfuv.jpg"
    )
    pin40 = Pin(
        title='Syrniki',
        description="Mix cottage cheese with eggs, flour, sugar, and vanilla extract until well combined. Form the mixture into pancakes and fry them in oil or butter until golden and cooked through. Serve Syrniki hot, optionally topped with sour cream, jam, or fresh berries for a delicious and popular Russian treat!",
        ingredients='Cottage cheese. Eggs. Flour. Sugar. Vanilla extract. Oil/butter.',
        time="25 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690656630/500bd03478e53059df38095562f96d8c_lv6sxy.jpg"
    )
    pin41 = Pin(
        title='Holubtsi',
        description="Blanch cabbage leaves until softened. In a bowl, mix ground meat, cooked rice, sautéed onions and garlic, and season to taste. Roll the meat mixture in cabbage leaves, tucking in the edges. Place the Holubtsi in a pot, pour tomato sauce and broth over them, and simmer until the cabbage is tender and flavors meld. Serve the Ukrainian Holubtsi hot and enjoy the comforting taste of this traditional dish!",
        ingredients='Cabbage leaves. Ground meat (beef or pork). Rice. Onion. Garlic. Tomato sauce. Broth.',
        time="40 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690656716/797e9ccb3e524c55d8a27e8280334d2f_w0foyk.jpg"
    )
    pin42 = Pin(
        title='Lasagna',
        description="Layer lasagna noodles, meat sauce, béchamel sauce, and shredded cheese in a baking dish, repeating until all ingredients are used, with cheese on top. Bake in a preheated oven at 375°F (190°C) for about 30-35 minutes or until the top is bubbly and golden. Let it rest for a few minutes before serving the delicious and hearty Lasagna!",
        ingredients='Lasagna noodles. Meat sauce. Béchamel sauce. Shredded cheese.',
        time="45 minutes",
        user_id=7,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690656785/977ca8e9c3971291157ce1e2180e88c2_s7n8m0.jpg"
    )
    pin43 = Pin(
        title='Persian Dolmeh',
        description="Blanch grape leaves until pliable. In a bowl, mix ground meat, cooked rice, finely chopped onions, garlic, and herbs. Fill grape leaves with the meat mixture, folding and rolling them. Place the Dolmeh in a pot, pour diluted tomato paste, lemon juice, and olive oil over them. Add water to cover the Dolmeh and simmer until cooked. Serve the Persian Dolmeh warm or at room temperature, and savor the delightful flavors of this traditional dish!",
        ingredients='Grape leaves. Ground meat (beef or lamb). Rice. Onion. Garlic. Herbs (parsley, dill, mint). Tomato paste. Lemon juice. Olive oil.',
        time="45 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690657161/056f7b8115e0050265c4abb642463687_sjyxvd.jpg"
    )
    pin44 = Pin(
        title='Pesto',
        description="In a food processor, blend fresh basil leaves, pine nuts, garlic, and grated Parmesan cheese until finely chopped. While blending, gradually pour in olive oil until the desired consistency is reached. Season with salt to taste. Use Pesto as a sauce for pasta, as a spread on sandwiches, or as a flavorful addition to various dishes. Enjoy the vibrant and aromatic taste of this classic Italian sauce!",
        ingredients='Fresh basil leaves. Pine nuts. Garlic. Parmesan cheese. Olive oil. Salt.',
        time="35 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690657282/5472bdef3ae8d7dbc46fde82f685fd24_dsv4ud.jpg"
    )
    pin45 = Pin(
        title='Couscous',
        description="In a saucepan, bring water or broth to a boil with a drizzle of olive oil or a pat of butter and a pinch of salt. Stir in couscous and immediately remove from heat. Cover the saucepan and let it sit for 5 minutes to allow the couscous to absorb the liquid and become fluffy. Fluff the couscous with a fork, and it's ready to serve. For added flavor, you can sauté chopped vegetables, herbs, or spices separately and mix them into the couscous before serving. Enjoy the light and versatile taste of couscous as a delicious side dish or base for various meals!",
        ingredients=' Couscous. Water or broth. Olive oil or butter. Salt. Optional: chopped vegetables, herbs, or spices for added flavor.',
        time="35 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690656034/f940c5e8489a82f49f32492de819cd47_hrpfiw.jpg"
    )
    pin46 = Pin(
        title='Veggie Burger',
        description=" In a food processor, blend black beans, cooked quinoa, chopped vegetables, bread crumbs, egg, and spices until well combined and a thick, sticky mixture forms. Shape the mixture into patties and cook them on a grill, stovetop, or in the oven until they are heated through and crispy on the outside. Optionally, add cheese slices on top of the patties while cooking. Serve the Veggie Burger on burger buns with lettuce, tomatoes, pickles, and your favorite condiments. Enjoy this delicious and nutritious plant-based burger alternative!",
        ingredients='Cooked or canned black beans. Cooked quinoa. Chopped vegetables (onions, bell peppers, carrots, etc.). Bread crumbs. Egg (or flaxseed egg for a vegan option). Spices (cumin, paprika, garlic powder, salt, pepper). Optional: cheese slices, burger buns, lettuce, tomatoes, pickles, and condiments for serving.',
        time="35 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690657602/1d054feca1cda7e0bfaa14f8177c34a3_yfqzuu.jpg"
    )
    pin47 = Pin(
        title='Quinoa Salad',
        description="In a large bowl, combine cooked quinoa, chopped vegetables, and fresh herbs. If desired, crumble feta cheese over the salad for added flavor. In a separate small bowl, whisk together olive oil, lemon juice, minced garlic, salt, and pepper to make the dressing. Pour the dressing over the quinoa and vegetables, tossing gently to coat evenly. Chill the Quinoa Salad in the refrigerator for at least 30 minutes before serving. Enjoy the refreshing and nutritious taste of this delightful salad!",
        ingredients=' Cooked quinoa. Chopped vegetables (cucumbers, tomatoes, bell peppers, red onions). Fresh herbs (parsley, cilantro, mint). Feta cheese (optional). Dressing (olive oil, lemon juice, garlic, salt, pepper).',
        time="25 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689907009/a6169d71aec018196a5590da4ad2b167_ck2bbs.jpg"
    )
    pin48 = Pin(
        title='Lentil Soup',
        description="In a large pot, heat olive oil over medium heat and sauté chopped onions, carrots, celery, and garlic until softened. Add lentils, crushed tomatoes, vegetable or chicken broth, bay leaf, thyme, and oregano to the pot. Bring the soup to a boil, then reduce the heat to a simmer and cover the pot. Cook the Lentil Soup for about 20-25 minutes or until the lentils are tender. Season with salt and pepper to taste. Serve the comforting and hearty Lentil Soup hot, optionally garnished with fresh herbs. Enjoy this wholesome and delicious soup!",
        ingredients='Lentils. Chopped vegetables (carrots, celery, onions). Garlic. Vegetable or chicken broth. Crushed tomatoes. Herbs (bay leaf, thyme, oregano). Olive oil. Salt. Pepper.',
        time="45 minutes",
        user_id=8,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690658217/6d79eb3bfe7249d0ad58defa8f93ce2d_ex2c9p.jpg"
    )
    pin49 = Pin(
        title='Apple Pie',
        description="Preheat oven to 375°F (190°C). Roll out pie crust and fit it into a pie dish. In a large bowl, mix sliced apples with sugar, brown sugar, cinnamon, nutmeg, lemon juice, and cornstarch until the apples are evenly coated. Pour the apple mixture into the pie crust. Dot the top of the apples with small pieces of butter. Roll out the second pie crust and place it over the apples. Trim any excess dough and crimp the edges to seal. Cut a few slits on top for ventilation. Optionally, brush the top crust with egg wash or milk for a shiny finish. Bake the Apple Pie for 45-50 minutes or until the crust is golden and the apples are tender. Let it cool slightly before serving. Enjoy the warm and comforting taste of homemade Apple Pie, ideally served with a scoop of vanilla ice cream!",
        ingredients='Pie crust (store-bought or homemade). Apples (peeled, cored, and sliced). Sugar. Brown sugar. Cinnamon. Nutmeg. Lemon juice. Cornstarch. Butter.',
        time="45 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690658290/b895b893646ef8e5b8d22db7361e2846_czcqx4.jpg"
    )
    pin50 = Pin(
        title='Macaroni and Cheese',
        description="Cook the elbow macaroni according to package instructions until al dente. In a separate saucepan, melt butter over medium heat, then whisk in flour to make a roux. Gradually add milk while stirring constantly to make a smooth sauce. Bring the sauce to a simmer and let it thicken. Add shredded cheese, salt, and pepper, stirring until the cheese is fully melted and the sauce is creamy. Combine the cheese sauce with the cooked macaroni, mixing until the macaroni is evenly coated. Optionally, transfer the macaroni and cheese mixture into a baking dish, sprinkle breadcrumbs on top, and bake in a preheated oven at 375°F (190°C) for a few minutes until the breadcrumbs are golden and crispy. Serve the Macaroni and Cheese hot and enjoy the gooey and delicious classic comfort food!",
        ingredients='Elbow macaroni. Cheese (cheddar, Gouda, or any melting cheese). Butter. Flour. Milk. Salt. Pepper. Optional: breadcrumbs for topping.',
        time="30 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690658387/46fd2ff1e4ef2bbc87dad4666895d148_lya8uc.jpg"
    )
    pin51 = Pin(
        title='Tamales',
        description="Soak corn husks in warm water until they are pliable. In a large bowl, mix masa harina, water or broth, melted lard or vegetable shortening, salt, and baking powder until a soft dough forms. In a separate bowl, mix the shredded cooked meat with chili sauce. Spread a thin layer of masa dough on each soaked corn husk. Place a spoonful of the meat mixture and any additional fillings in the center of the masa dough. Fold the sides of the corn husk over the filling and fold the bottom end up. Steam the tamales in a steamer for about 1 to 1.5 hours or until the masa is firm and cooked through. Serve the Tamales hot and enjoy the flavorful and traditional Mexican dish!",
        ingredients='Corn husks. Masa harina (corn flour). Water or broth. Lard or vegetable shortening. Shredded cooked meat (chicken, pork, or beef). Chili sauce. Salt. Baking powder. Optional: additional fillings like cheese, beans, or vegetables.',
        time="45 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690658518/23735906af79ed41870ac3ba90006228_szvtid.jpg"
    )
    pin52 = Pin(
        title='Fajitas',
        description="In a large skillet, heat olive oil over medium-high heat. Add sliced chicken, beef, or shrimp and cook until browned and cooked through. Remove the meat from the skillet and set it aside. In the same skillet, add sliced bell peppers and onion, and cook until they are softened and slightly charred. Return the cooked meat to the skillet and sprinkle fajita seasoning over the mixture. Stir until everything is evenly coated with the seasoning. Warm the flour tortillas in a separate skillet or microwave. Serve the Fajitas with warm tortillas and optional toppings like sour cream, guacamole, salsa, and shredded cheese. Roll up the filling in the tortillas and enjoy the delicious and flavorful Mexican Fajitas!",
        ingredients='Sliced chicken, beef, or shrimp. Bell peppers (red, green, and/or yellow). Onion. Fajita seasoning (or a mix of chili powder, cumin, paprika, garlic powder, salt, and pepper). Olive oil. Flour tortillas. Optional: sour cream, guacamole, salsa, shredded cheese for serving.',
        time="25 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690658967/db7e84e089a38d9203eb0cf38845ed1c_j1xteh.jpg"
    )
    pin53 = Pin(
        title='Fried Rice',
        description="In a large skillet or wok, heat some oil over medium-high heat. Add chopped vegetables and garlic, and stir-fry until they are tender-crisp. Push the vegetables to one side of the skillet and crack eggs on the other side. Scramble the eggs and mix them with the vegetables. Add the cooked protein and stir to combine. Add the cooked rice to the skillet and break up any clumps. Drizzle soy sauce and sesame oil over the rice, and toss everything together until the rice is evenly coated and heated through. Optionally, add chopped green onions and bean sprouts for extra freshness and crunch. Serve the Fried Rice hot and enjoy this simple and delicious Asian-inspired dish!",
        ingredients='Cooked rice (preferably cold or day-old). Cooked protein (chicken, shrimp, beef, or tofu). Chopped vegetables (carrots, peas, bell peppers, onions). Eggs. Soy sauce. Sesame oil. Garlic. Optional: green onions, bean sprouts, and other seasonings.',
        time="45 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690660996/514954c7903c11038f01070e90fa6e38_oi1hbx.jpg"
    )
    pin54 = Pin(
        title='Huo Guo (hot pot)',
        description="Place a hot pot with the broth in the center of the dining table and heat it. Arrange the thinly sliced meats, seafood, tofu, noodles, leafy greens, and mushrooms on separate plates around the hot pot. Once the broth is simmering, guests can cook their desired ingredients in the hot pot, dipping them in the broth until they are cooked to their liking. Serve with various dipping sauces for added flavor. Enjoy the communal and interactive experience of Huo Guo (hot pot) as you savor a delicious and customizable meal with family and friends!",
        ingredients='hinly sliced meats (beef, lamb, pork, or chicken). Assorted seafood (shrimp, squid, fish balls, etc.). Tofu. Noodles. Leafy greens (spinach, bok choy, etc.). Mushrooms. Dipping sauces (soy sauce, sesame oil, chili oil, etc.). Hot pot broth (spicy or non-spicy).',
        time="55 minutes",
        user_id=9,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690661338/b47a5a1332d0ef43290d1edf964e6413_irpln0.jpg"
    )
    pin55 = Pin(
        title='Gyoza',
        description="Finely chop cabbage, garlic, ginger, and green onions. In a bowl, mix ground pork with chopped vegetables, soy sauce, sesame oil, salt, and pepper. Take a gyoza wrapper, place a spoonful of the filling in the center, moisten the edges with water, and fold it in half to seal. Pleat the edges to create a decorative pattern. Continue making gyoza until all the filling is used. Heat some oil in a non-stick skillet and place the gyoza in a single layer. Cook until the bottom is lightly browned. Add water to the skillet and cover with a lid to steam the gyoza until the water evaporates. Remove the lid and let the gyoza cook until the bottom is crispy. Serve the Gyoza hot with a dipping sauce made from soy sauce, rice vinegar, and chili oil. Enjoy the delicious and flavorful Japanese dumplings!",
        ingredients='Gyoza wrappers (or dumpling wrappers). Ground pork. Cabbage. Garlic. Ginger. Green onions. Soy sauce. Sesame oil. Salt. Pepper.',
        time="40 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690661591/c7998a95d1eb57bb3997a8944466514b_cwdwlf.jpg"
    )
    pin56 = Pin(
        title='Chirashi bowl',
        description="Prepare sushi rice by cooking it and seasoning with rice vinegar, sugar, and salt. Slice the sashimi into bite-sized pieces. Dice cucumber and avocado. Cut tamagoyaki into thin slices if using. Assemble the Chirashi bowl by placing a mound of sushi rice in a bowl. Arrange the assorted sashimi, cucumber, avocado, tamagoyaki, and other toppings on top of the rice. Garnish with pickled ginger, nori seaweed, and sesame seeds. Optionally, drizzle some soy sauce or sushi seasoning over the bowl. Serve the Chirashi bowl and enjoy the delightful and colorful assortment of flavors in this traditional Japanese dish!",
        ingredients='Sushi rice. Assorted sashimi (salmon, tuna, yellowtail, etc.). Cucumber. Avocado. Pickled ginger. Nori seaweed. Sesame seeds. Optional: tamagoyaki (Japanese rolled omelette), edamame, shiitake mushrooms, and other toppings.',
        time="25 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690661827/b88f73b94cd4eba320982e7bcbba3a75_bpqdc8.jpg"
    )
    pin57 = Pin(
        title='Yakitori',
        description="Preheat the grill or broiler. Thread the chicken pieces onto bamboo skewers. In a saucepan, mix soy sauce, mirin, sake, and sugar to make the Yakitori sauce. Bring the sauce to a simmer and let it reduce slightly. Grill or broil the chicken skewers, brushing them with the Yakitori sauce occasionally, until they are cooked through and nicely charred. Serve the Yakitori hot and enjoy the delicious and flavorful Japanese grilled chicken skewers! Optionally, you can garnish with green onions or sesame seeds for extra taste and presentation.",
        ingredients='Chicken (thighs or breast), cut into bite-sized pieces. Yakitori sauce (soy sauce, mirin, sake, sugar). Bamboo skewers.',
        time="35 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690662311/cb3bfd5d60e8662aa3faca96fd91117f_mlijon.jpg"
    )
    pin58 = Pin(
        title='Mandu',
        description="Finely chop cabbage, garlic, ginger, and green onions. In a bowl, mix ground meat with chopped vegetables, crumbled tofu, soy sauce, sesame oil, salt, and pepper. Take a dumpling wrapper, place a spoonful of the filling in the center, moisten the edges with water, and fold it in half to seal. Pleat the edges to create a decorative pattern. Continue making mandu until all the filling is used. Heat some oil in a non-stick skillet and place the mandu in a single layer. Cook until the bottom is lightly browned. Add water to the skillet and cover with a lid to steam the mandu until the water evaporates. Remove the lid and let the mandu cook until the bottom is crispy. Serve the Mandu hot with a dipping sauce made from soy sauce, rice vinegar, and chili oil. Enjoy the delicious and savory Korean dumplings!",
        ingredients='Dumpling wrappers. Ground meat (pork, beef, or a combination). Tofu. Cabbage. Garlic. Ginger. Green onions. Soy sauce. Sesame oil. Salt. Pepper.',
        time="45 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690662451/0f2121583de80685958034eb60eece23_vaxeed.jpg"
    )
    pin59 = Pin(
        title='Japachae',
        description="Cook the sweet potato glass noodles according to package instructions until they are soft and translucent. Drain and set aside. Marinate the thinly sliced beef with soy sauce, sesame oil, garlic, and sugar for about 10-15 minutes. In a pan, stir-fry the marinated beef until it's cooked. Set aside. In the same pan, stir-fry the vegetables (spinach, carrots, onion, bell peppers, and shiitake mushrooms) until they are tender. Mix the cooked vegetables and beef with the glass noodles. Season with more soy sauce and sesame oil if desired. Sprinkle sesame seeds on top. Serve the Japchae warm or at room temperature and enjoy this delightful and flavorful Korean dish!",
        ingredients='Korean sweet potato glass noodles (dangmyeon). Beef (sirloin or ribeye), thinly sliced. Spinach. Carrots. Onion. Bell peppers. Shiitake mushrooms. Garlic. Soy sauce. Sesame oil. Sugar. Sesame seeds.',
        time="55 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690662535/f58a66a7d3a18e9b791a0e5c4ccb352c_o9dz39.jpg"
    )
    pin60 = Pin(
        title='Tteokboki',
        description="In a pan or pot, bring water or broth to a boil and add the Korean rice cakes. Cook the rice cakes until they become soft and chewy. Add sliced fish cakes, chopped onion, minced garlic, and sliced green onions to the pot. In a separate bowl, mix gochujang, gochugaru, soy sauce, sugar, and sesame oil to make the sauce. Pour the sauce over the rice cakes and fish cakes, stirring well to coat everything evenly. Simmer the Tteokboki over medium heat until the sauce thickens and the ingredients are well combined. Adjust the seasoning to your taste, adding more gochujang or sugar if desired. Serve the Tteokboki hot and enjoy the spicy and savory Korean rice cake dish!",
        ingredients='Korean rice cakes (tteok). Fish cakes. Onion. Green onions. Garlic. Gochujang (Korean chili paste). Gochugaru (Korean chili flakes). Soy sauce. Sugar. Sesame oil. Water or broth.',
        time="40 minutes",
        user_id=10,
        image_url="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1690662744/4422629422cbba7b2e175841ec934b19_ssz62q.jpg"
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