class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
    

    def add(self,producto):
        id = str(producto.id_producto)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "ID" : producto.id_producto,
                "nombre": producto.nombre,
                "cantidad" : 1,
                "precio": producto.precio,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio"] += producto.precio
        self.save()


    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def remove(self,producto):
        id = str(producto.id_producto)
        if id in self.carrito:
            del self.carrito[id]
            self.save()
    
    def decrement(self,producto):
        id = str(producto.id_producto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -=1
            self.carrito[id]["precio"] -= producto.precio
            if self.carrito[id]["cantidad"] <=0:
                self.remove(producto)
                self.save()
    
    def clear(self):
        self.session["carrito"] = {}
        self.session.modified = True


        














































































