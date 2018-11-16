
BackBut="./images/Back_Button.png"
MenuBut="./images/button_main-menu.png"
PreBut="./images/button_previous.png"
GreenTick="./images/green_tick.jpg"

def cuisine_placeholders():
	WesternBut = "./images/Cuisines/Western/Western_Cat.jpg"
	ChineseBut = "./images/Cuisines/Chinese/Chinese_Cat.jpg"
	KoreanBut = "./images/Cuisines/Korean/Korean_Cat.jpg"
	JapaneseBut = "./images/Cuisines/Japanese/Jap_Cat.jpg"
	MalayBut = "./images/Cuisines/Malay/Malay_Cat.jpg"
	IndianBut = "./images/Cuisines/Indian/Indian_Cat.jpg"
	ThaiBut = "./images/Cuisines/Thai/Thai_Cat.jpg"
	DrinksBut = "./images/Cuisines/Snacks_Beverages/SnackBev_Cat.jpg"

	return (WesternBut,ChineseBut,KoreanBut,JapaneseBut,MalayBut,IndianBut,ThaiBut,DrinksBut)

def western_placeholders():
	Place_1 = "./images/Cuisines/Western/ChickenChop.jpg"
	Place_2 = "./images/Cuisines/Western/FishChips.jpg"
	Place_3 = "./images/Cuisines/Western/Hamburger.jpeg"
	Place_4 = "./images/Cuisines/Western/Omelette.jpg"
	Place_5 = "./images/Cuisines/Western/PorkChop.jpg"
	Place_6 = "./images/Cuisines/Western/SausageCassoulet.jpg"
	Place_7 = "./images/Cuisines/Western/Spaghetti.jpg"
	Place_8 = "./images/Cuisines/Western/Steak.jpg"

	return (Place_1,Place_2,Place_3,Place_4,Place_5,Place_6,Place_7,Place_8)

def korean_placeholders():
	Place_1 = "./images/Cuisines/Korean/BeefBulgogi.jpg"
	Place_2 = "./images/Cuisines/Korean/Bibimbap.jpeg"
	Place_3 = "./images/Cuisines/Korean/Buchimgae.jpg"
	Place_4 = "./images/Cuisines/Korean/ChickenBulgogi.jpg"
	Place_5 = "./images/Cuisines/Korean/KoreanStew.jpg"
	Place_6 = "./images/Cuisines/Korean/Japchae.jpg"
	Place_7 = "./images/Cuisines/Korean/Kimchi.jpg"
	Place_8 = "./images/Cuisines/Korean/Ramen.jpg"

	return (Place_1,Place_2,Place_3,Place_4,Place_5,Place_6,Place_7,Place_8)

def japanese_placeholders():
	Place_1 = "./images/Cuisines/Japanese/BeefDon.jpg"
	Place_2 = "./images/Cuisines/Japanese/CharsiewDon.jpg"
	Place_3 = "./images/Cuisines/Japanese/OyakoDon.jpg"
	Place_4 = "./images/Cuisines/Japanese/RamenJap.jpg"
	Place_5 = "./images/Cuisines/Japanese/Soba.jpg"
	Place_6 = "./images/Cuisines/Japanese/Sushi.jpg"
	Place_7 = "./images/Cuisines/Japanese/Tempura.jpeg"
	Place_8 = "./images/Cuisines/Japanese/Yakitori.jpg"

	return (Place_1,Place_2,Place_3,Place_4,Place_5,Place_6,Place_7,Place_8)

def chinese_placeholders():
	Place_1 = "./images/Cuisines/Chinese/BakChorMee.jpg"
	Place_2 = "./images/Cuisines/Chinese/CharsiewRoastPork.jpg"
	Place_3 = "./images/Cuisines/Chinese/ChickenRice.jpg"
	Place_4 = "./images/Cuisines/Chinese/FishballNoodles.jpg"
	Place_5 = "./images/Cuisines/Chinese/FriedRice.jpg"
	Place_6 = "./images/Cuisines/Chinese/Gyoza.jpg"
	Place_7 = "./images/Cuisines/Chinese/WantonNoodles.jpg"
	Place_8 = "./images/Cuisines/Chinese/XiaoLongBao.jpg"

	return (Place_1,Place_2,Place_3,Place_4,Place_5,Place_6,Place_7,Place_8)

def malay_placeholders():
	Place_1 = "./images/Cuisines/Malay/AyamPenyet.jpg"
	Place_2 = "./images/Cuisines/Malay/IkanBakar.jpg"
	Place_3 = "./images/Cuisines/Malay/Lontong.jpg"
	Place_4 = "./images/Cuisines/Malay/MeeRebus.jpg"
	Place_5 = "./images/Cuisines/Malay/MeeSiam.jpg"
	Place_6 = "./images/Cuisines/Malay/NasiLemak.jpg"
	Place_7 = "./images/Cuisines/Malay/Rendang.jpg"
	Place_8 = "./images/Cuisines/Malay/Satay.jpeg"

	return (Place_1,Place_2,Place_3,Place_4,Place_5,Place_6,Place_7,Place_8)

def indian_placeholders():
	Place_1 = "./images/Cuisines/Indian/Briyani.jpg"
	Place_2 = "./images/Cuisines/Indian/ChickenCurry.jpg"
	Place_3 = "./images/Cuisines/Indian/Dosa.jpg"
	Place_4 = "./images/Cuisines/Indian/Murtabak.jpeg"
	Place_5 = "./images/Cuisines/Indian/Nan.jpg"
	Place_6 = "./images/Cuisines/Indian/Prata.jpg"
	Place_7 = "./images/Cuisines/Indian/Rojak.jpg"
	Place_8 = "./images/Cuisines/Indian/TikkaMasala.jpg"

	return (Place_1,Place_2,Place_3,Place_4,Place_5,Place_6,Place_7,Place_8)

def thai_placeholders():
	Place_1 = "./images/Cuisines/Thai/CashewNutChicken.jpg"
	Place_2 = "./images/Cuisines/Thai/CoconutChicken.jpg"
	Place_3 = "./images/Cuisines/Thai/GreenCurry.jpg"
	Place_4 = "./images/Cuisines/Thai/KhaoPad.jpg"
	Place_5 = "./images/Cuisines/Thai/PadKrapow.jpg"
	Place_6 = "./images/Cuisines/Thai/PadThai.jpg"
	Place_7 = "./images/Cuisines/Thai/RedCurry.jpg"
	Place_8 = "./images/Cuisines/Thai/TomYumSoup.jpg"

	return (Place_1,Place_2,Place_3,Place_4,Place_5,Place_6,Place_7,Place_8)

menu_placeholders=[western_placeholders(), korean_placeholders(), japanese_placeholders(),chinese_placeholders(),malay_placeholders(),indian_placeholders(),thai_placeholders()]


def western_store():
	return (["Western Cuisine"],["Western Cuisine"],["Western Cuisine"],["Western Cuisine"],["Western Cuisine"],["Western Cuisine"],["Western Cuisine", "Pasta Express", "Italian Cuisine"])

def korean_store():
	return(["Korean Cuisine", "Japanese Korean Cuisine"],["Korean Cuisine", "Japanese Korean Cuisine"],["Korean Cuisine", "Japanese Korean Cuisine"],["Korean Cuisine", "Japanese Korean Cuisine"],["Korean Cuisine", "Japanese Korean Cuisine"],["Korean Cuisine", "Japanese Korean Cuisine"])

def japan_store():
	return(["Japanese Cuisine", "Japanese Korean Cuisine"],["Japanese Cuisine", "Japanese Korean Cuisine"],["Japanese Cuisine", "Japanese Korean Cuisine"],["Japanese Cuisine", "Japanese Korean Cuisine"],["Japanese Cuisine", "Japanese Korean Cuisine"],["Japanese Cuisine", "Japanese Korean Cuisine"],["Japanese Cuisine", "Japanese Korean Cuisine"])

def chinese_store():
	return(["Braised Rice and Noodles", "Xian Noodles", "Noodle Delight", "Asian Food Delight", "Chinese Ramen"],["Braised Rice and Noodles", "Chinese Cuisine", "Chicken Rice", "Si Chuan Mei Shi"],["Chicken Rice"],["Yong Tau Foo", "Xian Noodles", "Noodle Delight"],["Braised Rice and Noodles", "Chinese Cuisine", "Jiu Li Xiang", "Claypot & Porridge", "Mixed Rice", "Mixed Fried Rice"],["Chinese Cuisine", "Xiao Long Bao", "Snacks", "Si Chuan Mei Shi", "Taiwanese Cuisine", "Si Chuan Cuisine", "Asian Food Delights", "Claypot & Porridge"],["Yong Tau Foo", "Noodle Delight"])

def malay_store():
	return(["Malay Cuisine", "Ayam Penyet"],["Malay Cuisine", "Ayam Penyet"],["Malay Cuisine"],["Malay Cuisine"],["Malay Cuisine"],["Malay Cuisine"],["Malay BBQ", "Malay Cuisine"])

def indian_store():
	return(["Indian Cuisine"],["Indian Cuisine"],["Indian Cuisine"],["Indian Cuisine"],["Indian Cuisine"],["Indian Cuisine"],["Indian Cuisine"])

def asian_food():
	return(["Asian Food Delights"],["Asian Food Delights"],["Asian Food Delights"],["Asian Food Delights"],["Asian Food Delights"],["Asian Food Delights"],["Asian Food Delights"])

stores_placeholder=[western_store(),korean_store(),japan_store(),chinese_store(),malay_store(),indian_store(),asian_food()]

canteen_data={
"Canteen 1": 
{"can_coord":(448, 450), 
"can_food":["Western Cuisine", "Mala", "Braised Rice and Noodles", "Chinese Cuisine", "Japanese Cuisine"],
"can_price":[[4, 24], [4, 20], [3, 20], [3, 25], [3, 20]]},
"Canteen 2": 
{"can_coord":(432, 367), 
"can_food":["Mixed Rice", "Shandong Big Bun", "Yong Tau Foo", "Korean Cuisine", "Xiao Long Bao", "Chicken Rice", "Ayam Penyet", "Western Cuisine", "Snacks"], 
"can_price":[[3, 20], [3, 20], [4, 20], [3, 20], [3, 20], [3, 20], [4, 20], [3, 20], [1, 5]]},
"Canteen 9": 
{"can_coord":(414, 188), 
"can_food":["Indian Cuisine", "Western Cuisine", "Jiu Li Xiang", "Chinese Cuisine", "Xian Noodles"],
"can_price":[[3, 23], [3, 23], [3, 25], [3, 23], [3, 23]]},
"Canteen 11":
{"can_coord":(464, 102),
"can_food":["Japanese Cuisine", "Mixed Fried Rice", "Si Chuan Mei Shi", "Korean Food", "Indian Cuisine"],
"can_price":[[3, 23], [3, 23], [3, 23], [3, 23], [3, 23]]},
"Canteen 13":
{"can_coord":(224, 230),
"can_food":["Noodle Delight", "Korean Cuisine", "Western Cuisine", "Chinese Cuisine", "Japanese Cuisine"],
"can_price":[[3, 23], [3, 23], [3, 23], [3, 23], [3, 23]]},
"Canteen 14":
{"can_coord":(266, 193),
"can_food":["Malay Cuisine", "Taiwanese Cuisine", "Si Chuan Cuisine", "Asian Food Delights", "Ban Mian Fish Soup"],
"can_price":[[3, 23], [3, 23], [3, 23], [3, 23], [3, 23]]},
"Canteen 16":
{"can_coord":(218, 288),
"can_food":["Indian Cuisine", "Japanese Cuisine", "Chinese Ramen", "Signature Dishes with Rice", "Mala"],
"can_price":[[3, 23], [3, 23], [3, 26], [3, 23], [3, 23]]},
"Northspine":
{"can_coord":(190, 415),
"can_food":["Italian Cuisine", "Xian Cuisine", "Japanese Korean Cuisine", "BBQ Delight", "Vietnamese Cuisine", "Vegetarian Food", "Malay BBQ", "Indian Cuisine", "Soup Delight", "Western Cuisine", "Cantonese Roast Duck", "Mixed Rice", "Hand Made Noodles", "Chicken Rice", "Yong Tau Foo", "Mini Wok"],
"can_price":[[3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23]]},
"Koufu":
{"can_coord":(269, 604),
"can_food":["Vegetarian Cuisine", "Mixed Rice", "Japanese Cuisine", "Pasta Express", "Malay Cuisine", "Ban Mian & Fish Soup", "Indian Cuisine", "Chicken Rice", "Chinese Cuisine", "Yong Tau Foo"],
"can_price":[[4, 13], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23]]},
"North hill":
{"can_coord":(569, 162),
"can_food":["Claypot & Porridge", "Western Cuisine", "Ah Boon's Fish Soup", "Chicken Rice", "Malay Cuisine", "Traditional Dough Fritters", "Mixed Rice"],
"can_price":[[3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23], [3, 23]]}
}
