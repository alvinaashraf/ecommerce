"""
A context processor is a function that takes the current HttpRequest
 object as an argument and returns a dictionary of variables that
  can be made available to all templates. These variables are added
   to the context of the request, meaning that they can be accessed in
   any template that is rendered as a result of that request.
    This allows you to include common information, such as a site logo or user details,
     on every page of your website, without having to include the same code in multiple views.
AFTER THIS ADD IN SETTINGS file ->  templates

"""
from .models import Category

def menu_links(request):
    links= Category.objects.all()
    return dict(links=links)