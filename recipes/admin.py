from django.contrib import admin

from .models import *


class IngredientInline(admin.TabularInline):
    fk_name = "recipe"
    model = Ingredient
    extra = 5


class InstructionInline(admin.TabularInline):
    fk_name = "recipe"
    model = Instruction
    extra = 5


class TagInline(admin.TabularInline):
    fk_name = "recipe"
    model = Tag
    extra = 3


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']
    list_display_links = ['title']
    inlines = [IngredientInline, InstructionInline, TagInline]

    # срабатывает при добавлении экземпляра
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user

        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(Tag)
admin.site.register(Profile)
