from models.kashta import KashtaModel
from models.package import PackagetModel

# We create some instances of our tea model here, which will be used in seeding.
Kashtas_list = [
    KashtaModel(name= "The Chalet", city= "Hamad Town", discription= "A hall with swimming pool" ,category ="summer", kashtaPrice=70,user_id=1),
    KashtaModel(name= "Bangkok", city= "Hamad Town", discription= "1 swimming pool with football field" ,category ="summer", kashtaPrice=90,user_id=1),
    KashtaModel(name= "Blue Wave", city= "Hamad Town", discription= "2 swimming pools and 2 rooms" ,category ="summer", kashtaPrice=85,user_id=1),
    KashtaModel(name= "Al Nokheta Camp", city= "Hamad Town", discription= "a camp of 3 tints with other intertaninmnts" ,category = "winter", kashtaPrice=120,user_id=1),
    KashtaModel(name= "The Wings", city= "Al Hamalah", discription= "A hall with swimming pool" ,category ="summer", kashtaPrice=100,user_id=1),
    KashtaModel(name= "Wanasa", city= "Sakheer", discription= "a camp of 3 big tints" ,category = "winter", kashtaPrice=70,user_id=1),
    KashtaModel(name= "Al Areesh", city= "Hamad Town", discription= "A hall with swimming pool" ,category ="summer", kashtaPrice=80,user_id=1),
    KashtaModel(name= "Zain", city= "Sakheer", discription= "3 big tents camp with other facilities" ,category = "winter", kashtaPrice=100,user_id=1),
    KashtaModel(name= "Sama Al Bahrain", city= "Al Hamala", discription= "A hall with swimming pool" ,category ="summer", kashtaPrice=70,user_id=1)
    
]

Packages_list = [
    PackagetModel(name= "Lunch", discription= "Two types of rice with meat and chicken, served with two types of desserts" , packageprice=66),
    PackagetModel(name= "Dinner", discription= "Mixed grill with appetizers and two types of desserts" , packageprice=95),
    PackagetModel(name= "Ice Cream Cart", discription= "Ten ice cream flavors with 3 types of sauces, cookies, and cups" , packageprice=28),
    PackagetModel(name= "Beverage Cart", discription= "A4 types of cold drinks and 2 types of hot drinks" , packageprice=35)
    
]

