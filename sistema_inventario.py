class ProductoError(Exception):
    """Excepción personalizada para errores relacionados con productos"""
    pass


class InventarioError(Exception):
    """Excepción personalizada para errores relacionados con el inventario"""
    pass


class Producto:
    """
    Clase que representa un producto en el inventario.
    
    Atributos:
        nombre (str): Nombre del producto
        precio (float): Precio unitario del producto
        cantidad (int): Cantidad disponible en inventario
    """
    
    def __init__(self, nombre, precio, cantidad):
        """
        Constructor de la clase Producto...
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio unitario
            cantidad (int): Cantidad en inventario
            
        Raises:
            ProductoError: Si los valores no cumplen las validaciones
        """
        self.nombre = self._validar_nombre(nombre)
        self.precio = self._validar_precio(precio)
        self.cantidad = self._validar_cantidad(cantidad)
    
    def _validar_nombre(self, nombre):
        """Valida que el nombre no esté vacío"""
        if not isinstance(nombre, str):
            raise ProductoError("El nombre debe ser una cadena de texto")
        
        nombre = nombre.strip()
        if not nombre:
            raise ProductoError("El nombre del producto no puede estar vacío")
        
        return nombre
    
    def _validar_precio(self, precio):
        """Valida que el precio sea un número positivo"""
        try:
            precio = float(precio)
        except (ValueError, TypeError):
            raise ProductoError("El precio debe ser un número válido")
        
        if precio < 0:
            raise ProductoError("El precio no puede ser negativo")
        
        return precio
    
    def _validar_cantidad(self, cantidad):
        """Valida que la cantidad sea un entero no negativo"""
        try:
            cantidad = int(cantidad)
        except (ValueError, TypeError):
            raise ProductoError("La cantidad debe ser un número entero válido")
        
        if cantidad < 0:
            raise ProductoError("La cantidad no puede ser negativa")
        
        return cantidad
    
    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto.
        
        Args:
            nuevo_precio (float): Nuevo precio del producto
            
        Raises:
            ProductoError: Si el precio no es válido
        """
        self.precio = self._validar_precio(nuevo_precio)
        print(f"✓ Precio actualizado a ${self.precio:.2f}")
    
    def actualizar_cantidad(self, nueva_cantidad):
        """
        Actualiza la cantidad del producto.
        
        Args:
            nueva_cantidad (int): Nueva cantidad del producto
            
        Raises:
            ProductoError: Si la cantidad no es válida
        """
        self.cantidad = self._validar_cantidad(nueva_cantidad)
        print(f"✓ Cantidad actualizada a {self.cantidad} unidades")
    
    def calcular_valor_total(self):
        """
        Calcula el valor total del producto (precio × cantidad).
        
        Returns:
            float: Valor total del producto
        """
        return self.precio * self.cantidad
    
    def __str__(self):
        """
        Representación en cadena del producto.
        
        Returns:
            str: Información formateada del producto
        """
        valor_total = self.calcular_valor_total()
        return (f" {self.nombre:<20} | "
                f" ${self.precio:>8.2f} | "
                f" {self.cantidad:>6} unid. | "
                f" Total: ${valor_total:>10.2f}")


class Inventario:
    """
    Clase que gestiona una colección de productos.
    
    Atributos:
        productos (list): Lista de objetos Producto
    """
    
    def __init__(self):
        """Constructor que inicializa una lista vacía de productos"""
        self.productos = []
        print(" Inventario inicializado correctamente")
    
    def agregar_producto(self, producto):
        """
        Añade un producto al inventario.
        
        Args:
            producto (Producto): Objeto de tipo Producto a añadir
            
        Raises:
            InventarioError: Si el producto no es válido o ya existe
        """
        if not isinstance(producto, Producto):
            raise InventarioError("Solo se pueden agregar objetos de tipo Producto")
        
        # Verificar si el producto ya existe
        producto_existente = self.buscar_producto(producto.nombre)
        if producto_existente:
            raise InventarioError(f"El producto '{producto.nombre}' ya existe en el inventario")
        
        self.productos.append(producto)
        print(f" Producto '{producto.nombre}' agregado exitosamente al inventario")
    
    def buscar_producto(self, nombre):
        """
        Busca un producto por su nombre.
        
        Args:
            nombre (str): Nombre del producto a buscar
            
        Returns:
            Producto or None: El producto encontrado o None si no existe
        """
        nombre = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre:
                return producto
        return None
    
    def calcular_valor_inventario(self):
        """
        Calcula el valor total de todos los productos en el inventario.
        
        Returns:
            float: Valor total del inventario
        """
        return sum(producto.calcular_valor_total() for producto in self.productos)
    
    def listar_productos(self):
        """Muestra todos los productos del inventario de forma formateada"""
        if not self.productos:
            print("\n El inventario está vacío")
            return
        
        print(f"\n{'='*80}")
        print(f"{' INVENTARIO DE PRODUCTOS':^80}")
        print(f"{'='*80}")
        print(f"{'Producto':<20} | {'Precio':>10} | {'Cantidad':>10} | {'Valor Total':>15}")
        print("-" * 80)
        
        for producto in self.productos:
            print(producto)
        
        print("-" * 80)
        valor_total = self.calcular_valor_inventario()
        print(f"{'VALOR TOTAL DEL INVENTARIO:':<50} 💰 ${valor_total:>15.2f}")
        print(f"{'TOTAL DE PRODUCTOS:':<50}  {len(self.productos):>15}")
        print("=" * 80)
    
    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario.
        
        Args:
            nombre (str): Nombre del producto a eliminar
            
        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        producto = self.buscar_producto(nombre)
        if producto:
            self.productos.remove(producto)
            print(f"  Producto '{nombre}' eliminado del inventario")
            return True
        else:
            print(f" Producto '{nombre}' no encontrado")
            return False


def crear_producto():
    """
    Función auxiliar para crear un nuevo producto con validación de entrada.
    
    Returns:
        Producto or None: Nuevo producto creado o None si hubo error
    """
    try:
        print("\n CREAR NUEVO PRODUCTO")
        print("-" * 30)
        
        nombre = input("Ingresa el nombre del producto: ").strip()
        precio = input("Ingresa el precio del producto: $")
        cantidad = input("Ingresa la cantidad en inventario: ")
        
        producto = Producto(nombre, precio, cantidad)
        return producto
        
    except ProductoError as e:
        print(f" Error al crear producto: {e}")
        return None
    except Exception as e:
        print(f" Error inesperado: {e}")
        return None


def buscar_y_mostrar_producto(inventario):
    """
    Función auxiliar para buscar y mostrar un producto.
    
    Args:
        inventario (Inventario): Instancia del inventario
    """
    try:
        nombre = input("\nIngresa el nombre del producto a buscar: ").strip()
        
        if not nombre:
            print(" El nombre no puede estar vacío")
            return
        
        producto = inventario.buscar_producto(nombre)
        
        if producto:
            print(f"\n PRODUCTO ENCONTRADO:")
            print("-" * 50)
            print(producto)
        else:
            print(f" Producto '{nombre}' no encontrado en el inventario")
            
    except Exception as e:
        print(f" Error en la búsqueda: {e}")


def actualizar_producto(inventario):
    """
    Función auxiliar para actualizar un producto existente.
    
    Args:
        inventario (Inventario): Instancia del inventario
    """
    try:
        nombre = input("\nIngresa el nombre del producto a actualizar: ").strip()
        producto = inventario.buscar_producto(nombre)
        
        if not producto:
            print(f"❌ Producto '{nombre}' no encontrado")
            return
        
        print(f"\n Producto actual:")
        print(producto)
        
        print("\n¿Qué deseas actualizar?")
        print("1. Precio")
        print("2. Cantidad")
        print("3. Ambos")
        
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        if opcion in ['1', '3']:
            nuevo_precio = input(f"Nuevo precio (actual: ${producto.precio:.2f}): $")
            producto.actualizar_precio(nuevo_precio)
        
        if opcion in ['2', '3']:
            nueva_cantidad = input(f"Nueva cantidad (actual: {producto.cantidad}): ")
            producto.actualizar_cantidad(nueva_cantidad)
        
        if opcion not in ['1', '2', '3']:
            print(" Opción no válida")
            
    except ProductoError as e:
        print(f" Error al actualizar producto: {e}")
    except Exception as e:
        print(f" Error inesperado: {e}")


def menu_principal():
    """
    Función que muestra el menú principal y procesa las opciones del usuario.
    """
    inventario = Inventario()
    
    while True:
        try:
            print(f"\n{'='*50}")
            print(f"{' SISTEMA DE INVENTARIO':^50}")
            print(f"{'='*50}")
            print("1.   Agregar producto")
            print("2.   Buscar producto")
            print("3.   Listar todos los productos")
            print("4.   Calcular valor total del inventario")
            print("5.   Actualizar producto")
            print("6.   Eliminar producto")
            print("7.  Salir")
            print("-" * 50)
            
            opcion = input("Selecciona una opción (1-7): ").strip()
            
            if opcion == '1':
                producto = crear_producto()
                if producto:
                    try:
                        inventario.agregar_producto(producto)
                    except InventarioError as e:
                        print(f" Error: {e}")
            
            elif opcion == '2':
                buscar_y_mostrar_producto(inventario)
            
            elif opcion == '3':
                inventario.listar_productos()
            
            elif opcion == '4':
                valor_total = inventario.calcular_valor_inventario()
                print(f"\n VALOR TOTAL DEL INVENTARIO: ${valor_total:.2f}")
                print(f" PRODUCTOS EN INVENTARIO: {len(inventario.productos)}")
            
            elif opcion == '5':
                actualizar_producto(inventario)
            
            elif opcion == '6':
                nombre = input("\nIngresa el nombre del producto a eliminar: ").strip()
                inventario.eliminar_producto(nombre)
            
            elif opcion == '7':
                print("\n" + "="*50)
                print("¡Gracias por usar el Sistema de Inventario!")
                print("¡Que tengas un excelente día! 🌟")
                print("="*50)
                break
            
            else:
                print(" Opción no válida. Por favor selecciona una opción del 1 al 7.")
        
        except KeyboardInterrupt:
            print("\n\n  Programa interrumpido por el usuario.")
            break
        except Exception as e:
            print(f" Error inesperado en el menú: {e}")


if __name__ == "__main__":
    print(" Iniciando Sistema de Inventario...")
    menu_principal()