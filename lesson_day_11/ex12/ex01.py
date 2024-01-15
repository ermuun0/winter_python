class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0, ):
        
        self.served = number_served
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        print(f'Restaurant name is {self.name}')
        print(f'Restaurant cuisine type is {self.type}')
        
    def open_restaurant(self):
        print(f'{self.name} is open')
    def set_number_served(self):
        self.served = self.served
        print(f'{self.served} people served')
    def increment_number_served(self, increas_number):
        self.increas = increas_number
        self.served = self.served + self.increas
        print(f'{self.served} people served')
    
        
yuna_restaurant = Restaurant('Yuna', 'korean restaurant', 80)
yuna_restaurant.describe_restaurant()
yuna_restaurant.open_restaurant()
yuna_restaurant.set_number_served()
yuna_restaurant.increment_number_served(70)
arig_restaurant = Restaurant('Arig', 'Japanese restaurant')
arig_restaurant.describe_restaurant()
arig_restaurant.open_restaurant()
bull_restaurant = Restaurant('Bull', 'hot-pot restaurant')
bull_restaurant.describe_restaurant()
bull_restaurant.open_restaurant()


    