from django.contrib import admin

from api.models import User, Category, Product, Comments, Cart, Orders, ProductHistory

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comments)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(ProductHistory)
