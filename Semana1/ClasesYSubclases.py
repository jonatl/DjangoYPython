class Usuarios:

	tipo_usuario = "Free"
	publicidad = True

	def __init__(self, nid, alias, nombre, apellidos):
		self.nid = nid
		self.alias = alias
		self.nombre = nombre
		self.apellidos = apellidos

	def muestra_datos(self):
		print("El nombre y los apellidos del usuario son: " + self.nombre, self.apellidos)
		print("El ID de usuario es: " + self.nid + ".")
		print("El alias del usuario es: " + self.alias + ".")


class UsuariosPremium(Usuarios):
	tipo_usuario = "Premium"
	publicidad = False
	soporte_premium=True

class UsuariosIPERPremium(Usuarios):
	tipo_usuario = "IPERPremium"
	publicidad = False
	soporte_premium=True

usuario1 = Usuarios("001", "raulito43", "Raúl", "Fernández Gomila")
usuario1.muestra_datos()
print(usuario1.tipo_usuario)
print()

usuario2=UsuariosPremium("002","Jonin","chinchin","Robertinñia")
usuario2.muestra_datos()
print(usuario2.tipo_usuario)
print()

usuario3=UsuariosIPERPremium("003","Elmer","Homero","MedioMetro")
usuario3.muestra_datos()
print(usuario3.tipo_usuario)


