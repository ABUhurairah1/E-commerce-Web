from .models import Product
from decimal import Decimal

class Cart():
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session-key')
        if 'session-key' not in request.session:
            cart = self.session['session-key'] = {}
        self.cart = cart

    def add(self, product, product_qty):
        """
        Adding and updating the user's cart session data
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'title': str(product.title),
                'description': str(product.description),
                'category': str(product.category),
                'price': str(product.price),
                'quantity': product_qty
            }

        self.session.modified = True

    def __iter__(self):
        """
        Collect the product id in the session to query the database and return products
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

        
    def get_sub_total(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


    def __len__(self):
        """
        Get the cart data and count the quantity
        """
        return sum(item['quantity'] for item in self.cart.values())
    

    def delete(self , product):

        """
  
           Delete item from session data


        """

        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True



    def update(self , product,product_qty):

        """
  
           Update values in session data


        """
        product_id = str(product)
        quantity = product_qty

        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity

        self.session.modified = True


    