import operations as op

name    = input("Escriba su nombre completo: ")
email   = input("Escriba su correo electronico: ")
veces   = int(input("¿Cuántas notas desea ingresar?: "))
notas   = []

i = 1
while i <= veces:
    notas.append(float(input("Digite la {0}° nota: ".format(i))))
    i += 1

print("Nombre: {0} Correo: {1}".format(name, email))
print(op.promedio(notas,veces))