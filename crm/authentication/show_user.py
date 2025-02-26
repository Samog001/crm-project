# context processor

# here context processor is used to implement how a username displays

def show_user(request):
    
    username = request.user.username
    
    name = username.split('@')[0]
    
    return {'name_of_user':name}