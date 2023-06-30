class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
    

    def add(self,producto):
        if str(producto.id_producto) not in self.cart.keys():
            self.cart[producto.id_producto] = {
                "ID" : producto.id_producto,
                "nombre": producto.nombre,
                "cantidad" : producto.stock,
                "precio": str(producto.precio),
            }
        else:
            for key, value in self.cart.items():
                if key == str(producto.id_producto):
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self,producto):
        ID = str(producto.id_producto)
        if ID in self.cart:
            del self.cart[ID]
            self.save()
    
    def decrement(self,producto):
        for key, value in self.cart.items():
            if key == str(producto.id_producto):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.remove(producto)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en carrito")
    
    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True


        














































































