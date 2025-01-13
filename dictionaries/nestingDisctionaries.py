alien_0={'color':'green','points':5}
alien_1={'color':'red','points':7}
alien_2={'color':'blue','points':2}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(f"alien: {alien['color']},{alien['points']}.")

print("Create lalines like an constructor")
for alien_number in range(30):
    n_alien={'number':alien_number,'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(n_alien)

print("Show aliens")

for alien_d in aliens[:5]:
    print(alien_d)
print("...")
print(f"Total number of aliens: {len(aliens)}")

# CRUD en un diccionario dentro de otro diccionario
users = {
    'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton'},
    'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris'},
}

# Crear
users['nbohr'] = {'first': 'niels', 'last': 'bohr', 'location': 'copenhagen'}

# Leer
user_info = users.get('mcurie')
if user_info:
    print(f"\nNombre completo: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"Ubicación: {user_info['location'].title()}")

# Actualizar
users['aeinstein']['location'] = 'berlin'

# Eliminar
users.pop('mcurie', None)

# Mostrar todos
for username, user_info in users.items():
    print(f"\nUsuario: {username}")
    print(f"Nombre completo: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"Ubicación: {user_info['location'].title()}")
