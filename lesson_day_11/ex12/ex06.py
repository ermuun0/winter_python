from ex01 import Restaurant
class IceCreamStand (Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0, flavors = []):
        super().__init__(restaurant_name, cuisine_type, number_served, )
        self.flavor =flavors
    def show_Flavor(self):
        print(f'{self.flavor}')
ice_cream = IceCreamStand('ice' , 'ice', 0 , ['chocolate', 'straw Berry'])
ice_cream.show_Flavor()
        