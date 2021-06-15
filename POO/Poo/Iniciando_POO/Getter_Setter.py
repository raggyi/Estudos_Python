class Product :
    def __init__(self, name, price) :
        self.name=name
        self.price=price

    def discount(self, percent) :
        return self.price - (self.price * (percent / 100))

    # Getter
    @property
    def price(self) :
        return self._price

    @property
    def name(self):
        return self._name
    #Setter
    @name.setter
    def name(self, value):
        self._name = value.title()
    @price.setter
    def price(self, value) :
        if isinstance( value, str ) :
            value=float( value.replace( 'R$', '' ) )
        self._price=value


p1=Product ('Caixa', 10)
print( p1.discount( 10 ))
p2= Product('mokao','R$20')
print(p2.price)
print(p2.name)