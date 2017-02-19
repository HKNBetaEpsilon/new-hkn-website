from django import template

from users.models import Member

register = template.Library() 

@register.filter(name='is_officer') 
def is_officer(uniqname):
    if uniqname == None or len(uniqname) == 0:
        return False
    try:
        m =  Member.objects.get(uniqname=uniqname)
        return m.status == 'O'
    except DoesNotExist as e:
        return False