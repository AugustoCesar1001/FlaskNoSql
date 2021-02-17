



def response(id, username, hashed_password, name, email, cellphone):
    retorno = {'id': str(id),
            'username': username,
            'password': hashed_password,
            'name': name,
            'email': email,
            'cellphone': cellphone
        }
    return retorno