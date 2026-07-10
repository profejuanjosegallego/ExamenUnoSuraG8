def registrar_usuario(usuarios, correo, password):
    """Registra un usuario nuevo en la lista de usuarios."""
    for usuario in usuarios:
        if usuario["correo"] == correo:
            print("El correo ya está registrado.")
            return False

    usuarios.append({"correo": correo, "password": password})
    print("Usuario registrado correctamente.")
    return True


def autenticar_usuario(usuarios, correo, password, intentos):
    """Valida las credenciales de un usuario con un máximo de intentos."""
    for intento in range(intentos):
        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                return True

        restantes = intentos - (intento + 1)
        if restantes > 0:
            print(f"Credenciales incorrectas. Intentos restantes: {restantes}")

    print("Cuenta bloqueada temporalmente")
    return False
