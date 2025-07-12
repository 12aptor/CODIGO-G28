class UserResource:
    def create(self, json):
        try:
            id = int(json['id'])
            name = json['name']
            email = json['email']
            age = int(json['age'])
            with open('users.txt', 'a') as file:
                file.write('\n')
                file.write(f'{id},{name},{email},{age}')

            return {
                'id': id,
                'name': name,
                'email': email,
                'age': age
            }, 201
        except Exception as e:
            return {
                'error': str(e)
            }, 500

    def list(self):
        try:
            users = []
            with open('users.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    datos = line.strip().split(',')
                    id = int(datos[0])
                    name = datos[1]
                    email = datos[2]
                    age = int(datos[3])

                    users.append({
                        'id': id,
                        'name': name,
                        'email': email,
                        'age': age
                    })

            return users, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500

    def update(self, id, json):
        try:
            name = json['name']
            email = json['email']
            age = int(json['age'])

            updated_users = []

            with open('users.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    datos = line.strip().split(',')
                    user_id = int(datos[0])

                    if user_id == id:
                        updated_line = f"{id},{name},{email},{age}"
                        updated_users.append(updated_line)
                    else:
                        updated_users.append(line)

            with open('users.txt', 'w') as file:
                file.writelines(updated_users)
            
            return {
                'id': id,
                'name': name,
                'email': email,
                'age': age
            }, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500

    def delete(self, id):
        try:
            updated_users = []
            with open('users.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    datos = line.strip().split(',')
                    user_id = int(datos[0])
                    if user_id != id:
                        updated_users.append(line)

            with open('users.txt', 'w') as file:
                file.writelines(updated_users)

            return {
                'message': f'User deleted'
            }, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500