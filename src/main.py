class Pizza:
    valid_size=['small','medium','large','x-large']
    base_price= {'small':6.49,'medium':8.49,'large':10.49,'x-large':13.49}

    def __init__(self,size='medium',toppings=None):
        self.__size= size
        self.__toppings = toppings if toppings is not None else ['cheese']
        #self.size= size

    def add(self,toppings):
        if toppings is None:
            self.__toppings.append('cheese')
        else:
            self.__toppings.extend(toppings)
    def __str__(self):
        topping_str= ','.join(self.__toppings)
        return  f"size{self.__size},toppings=[{topping_str}],price={self.price}"
    @property
    def price(self):
        pricePiz=Pizza.base_price[self.__size]
        topping_cost = len(self.__toppings)*0.5
        return pricePiz + topping_cost
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,value):
        if value not in Pizza.valid_size:
            raise  ValueError(f"invalide:{value}.Valid size are:{','.join(Pizza.valid_size)}")
        self.__size = value

print(f'Creating a default pizza')
p = Pizza()
print(p)

toppings = 'cheese olive'.split()
print(f'\nAdding topping: {toppings}')
p.add(toppings=toppings)
print(p)

