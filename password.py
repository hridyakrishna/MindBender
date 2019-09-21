def password():
    password = input ('Enter Password')


    weak = 'weak'
    medium = 'medium'
    strong = 'strong'

    if len(password) <8:
        print ('password is too Short. Must be atleast 8 charactets')

    elif len(password) >10 and len(password) <12:
			print ('Password is medium')


    elif len(password)    >=12 :
        print ('Password is Strong')
