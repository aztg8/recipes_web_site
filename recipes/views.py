from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .models import *
from .forms import *


def index(request):
    categories = Category.objects.all()
    difficulties = Difficulty.objects.all()
    recipes = Recipe.objects.all()

    context = {
        "categories": categories,
        "difficulties": difficulties,
        "recipes": recipes,
        "title": "Главная страница"
    }

    return render(request, 'index.html', context)


def sort_recipes_by_category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    recipes = Recipe.objects.filter(category=category_id)

    context = {
        "title": f"Категория: {category.title}",
        "recipes": recipes,
        "category": category
    }

    return render(request, "category_page.html", context)


def sort_by_difficulty_view(request, difficulty_id):
    difficulty = Difficulty.objects.get(id=difficulty_id)
    recipes = Recipe.objects.filter(difficulty=difficulty_id)

    context = {
        "title": f"Сложность: {difficulty.title}",
        "recipes": recipes,
        "difficulty": difficulty
    }

    return render(request, "difficulty_page.html", context)


def recipe_detail_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    top_recipes = Recipe.objects.all().order_by('-viewCount')
    ingredients = Ingredient.objects.filter(recipe=recipe_id)
    instructions = Instruction.objects.filter(recipe=recipe_id)

    context = {
        "recipe": recipe,
        "top_recipes": top_recipes,
        "title": f"Рецепт: {recipe.title}",
        "ingredients": ingredients,
        "instructions": instructions
    }

    return render(request, "recipe_detail.html", context)


def about_us_page_view(request):
    return render(request, "about_us.html")


def our_team_page_view(request):
    return render(request, "our_team.html")


def services_page_view(request):
    return render(request, "services.html")


def search_view(request):
    word = request.GET.get("q")
    recipes = Recipe.objects.filter(title__iregex=word)

    context = {
        "title": "Результаты поиска",
        "recipes": recipes
    }

    return render(request, "search.html", context)


def user_login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.success(request, "Вы успешно вошли в аккаунт !")
                return redirect('index')
            else:
                messages.error(request, "Логин или пароль неправильный !")
                return redirect('login')
        else:
            messages.error(request, "Логин или пароль неправильный !")
            return redirect('login')
    else:
        form = UserLoginForm()

    context = {
        "title": "Вход в аккаунт",
        "form": form
    }
    return render(request, "login.html", context)


def user_registration_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(request, "Регистрация прошла успешно !")
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('registration')
    else:
        form = UserRegistrationForm()

    context = {
        "title": "Регистрация",
        "form": form
    }

    return render(request, "registration.html", context)


def user_logout_view(request):
    logout(request)
    messages.warning(request, "Вы вышли с аккаунта !")
    return redirect('index')


def check_profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    context = {
        "profile": profile,
        "title": "Профиль пользователя"
    }

    return render(request, "profile.html", context)


def change_profile_data(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        user_form = UserForm(instance=user, data=request.POST)
        profile_form = ProfileForm(instance=profile, data=request.POST,
                                   files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()
            messages.success(request, "Данные успешно изменены !")
            return redirect("profile", user.id)
        else:
            for field in user_form.errors:
                messages.error(request, user_form.errors[field].as_text())
            for field in profile_form.errors:
                messages.error(request, profile_form.errors[field].as_text())
            return redirect('change_profile', user.id)
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        "title": "Изменить профиль",
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, "change_profile.html", context)


def add_recipe_view(request):
    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST,
                                 files=request.FILES)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, "Рецепт успешно добавлен !")
            return redirect("recipe_detail", recipe.id)
        else:
            for field in recipe_form.errors:
                messages.error(request, recipe_form.errors[field].as_text())
            return redirect("add_recipe")
    else:
        recipe_form = RecipeForm()

    context = {
        "title": "Добавить рецепт",
        "recipe_form": recipe_form
    }

    return render(request, "add_recipe.html", context)


def update_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == "POST":
        form = RecipeForm(data=request.POST,
                          files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Рецепт успешно обновлен !")
            return redirect("recipe_detail", recipe.id)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect("update_recipe", recipe.id)

    else:
        form = RecipeForm(instance=recipe)

    context = {
        "title": "Обновление рецепта",
        "recipe_form": form
    }

    return render(request, "add_recipe.html", context)

def delete_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == "POST":
        recipe.delete()
        messages.info(request, "Рецепт успешно удален !")
        return redirect("index")

    context = {
        "title": "Удаление рецепта",
        "recipe": recipe
    }

    return render(request, "delete.html", context)










