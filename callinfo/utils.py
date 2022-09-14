from .models import User


def phoneno_registered(phoneno):
    try:
        User.objects.get(phoneno=phoneno)
        valid = True
    except:
        valid = False
    return valid


def is_user_authenticated(phoneno, password):

    ''' Here we need to get the model obj 1st and then need to extract req field using field_name of model '''

    user_obj = User.objects.get(phoneno=phoneno)
    reg_password = user_obj.password
    if reg_password == password:
        auth = True
    else:
        auth = False
    return auth
