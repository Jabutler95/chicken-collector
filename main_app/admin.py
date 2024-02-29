from django.contrib import admin
from .models import Chicken, Feeding, Toy

# Register your models here.


admin.site.register(Chicken)
admin.site.register(Feeding)
admin.site.register(Toy)