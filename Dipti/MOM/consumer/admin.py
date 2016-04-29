from django.contrib import admin

# Register your models here.
from .models import Dish, Producer

#admin.site.register(Producer)
#admin.site.register(Dish)


class DishInline(admin.TabularInline):
    model = Dish
    extra = 2


class ProducerAdmin(admin.ModelAdmin):
	#...
	
	list_display = ('name', 'zipcode')     ##Display on homepage for Producer and Zipcode

    	fieldsets = [
        			(None, {'fields': ['name']}),
        			(None, {'fields': ['address']}),
       				(None, {'fields': ['zipcode']}),
    				]
    
    	inlines = [DishInline]

admin.site.register(Producer, ProducerAdmin)