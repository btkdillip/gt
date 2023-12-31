from .models import category

def menu_links(request):
    links=category.objects.all()
    return dict(links=links)






#
# great kart project:
# ------------------------------------------------
# section:- 7
# context processer & product details
#
#
# video 69:
# --------
# make context processors for displaying categories on navbar
#
# -
# now we have to fetch the all products in a category wise in the navbar
# so that we have to do list down all the categorie here so that when ever we click in a particular category, it will bring us all the products by that category
#
# for that this we will be using a python function called context processors
#
# in that project open that category app
# in that app create new file called context_processer.py file  write the function called menu_links
#
#
#
# what it will do is
#
# it takes a request as an argument and it wil return the dicitionary of data as a context
#
#
# since we are using the context processor, we are going to tell the this templeates that we are using context processer in the setting.py , like
#
#
# "category.context_processors.function_name "   "like menu_links'
#
# why we adding here is
#
#
# so by adding here what will happen is we will able to call this ,and use this menulinks in any templates we want
#
# so this menu links will be avaliable in all the templates
#
# so that the reason we use this context processors
#
# links in the html page
# -------------------------------------------<div class="dropdown-menu">
# 				{% for category in links %}
# 				<a class="dropdown-item" href="{{ category.get_url }}">{{ category.category_name }}</a>
# 				{% endfor %}
# 			</div>
#
#  href="{{ category.get_url }}"
#
#
#
#
# for this category.get_url purpuse
#
#
# we have to create another function in category models.py
#
#
#  def get_url(self):
#         return reverse('product_by_category',args=[self.slug])
#
# this args=[self.slug] will call the slug field in the category this slug give the name to product_by_category url then will give to the link about this name then it will called
#
# this product_by_category' will call the url of the store
# in the function we have import reverse function for give
#
