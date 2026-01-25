
kashtas_db = {
    "teas": [
        {"id": 1, "name": "chai",  "rating": 40},
        {"id": 2, "name": "lemongrass", "price": 50},
        {"id": 3, "name": "matcha", "price": 20},
    ]
}

from models.kashta import KashtaModel

# We create some instances of our tea model here, which will be used in seeding.
Kashtas_list = [
    KashtaModel(name= "The Chalet", city= "Hamad Town", discription= "A hall with swimming pool" , price=70),
    KashtaModel(name= "Bangkok", city= "Hamad Town", discription= "1 swimming pool with football field" , price=90),
    KashtaModel(name= "Blue Wave", city= "Hamad Town", discription= "2 swimming pools and 2 rooms" , price=85),
    KashtaModel(name= "Al Nokheta Camp", city= "Hamad Town", discription= "a camp of 3 tints with other intertaninmnts" , price=120),
    KashtaModel(name= "The Wings", city= "Al Hamalah", discription= "A hall with swimming pool" , price=100),
    KashtaModel(name= "Wanasa", city= "Sakheer", discription= "a camp of 3 big tints" , price=70),
    KashtaModel(name= "Al Areesh", city= "Hamad Town", discription= "A hall with swimming pool" , price=80),
    KashtaModel(name= "Zain", city= "Sakheer", discription= "3 big tents camp with other facilities" , price=100),
    KashtaModel(name= "Sama Al Bahrain", city= "Al Hamala", discription= "A hall with swimming pool" , price=70)
    
]