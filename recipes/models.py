from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True,
                             verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Difficulty(models.Model):
    title = models.CharField(max_length=255, unique=True,
                             verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сложность"
        verbose_name_plural = "Сложности"


class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(default="")
    prepTimeMinutes = models.IntegerField(verbose_name="Время подготовки")
    cookTimeMinutes = models.IntegerField(verbose_name="Время приготовления")
    servings = models.IntegerField(verbose_name="Порции")
    cuisine = models.CharField(max_length=255, verbose_name="Кухня")
    caloriesPerServing = models.IntegerField(verbose_name="Калории/порция")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    viewCount = models.IntegerField(default=0, editable=False, verbose_name="Просмотры")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, verbose_name="Сложность приготовления")

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор",
                               default=1,
                               editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class Ingredient(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="Название")
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name="Рецепт")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Instruction(models.Model):
    title = models.TextField(verbose_name="Название")
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name="Рецепт")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Инструкция"
        verbose_name_plural = "Инструкции"


class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Profile(models.Model):
    photo = models.ImageField(upload_to='profiles/',
                              verbose_name="Фото",
                              null=True, blank=True)
    phone_number = models.CharField(max_length=20,
                                    verbose_name="Номер телефона",
                                    default="**********")
    address = models.CharField(max_length=150,
                               verbose_name="Адрес",
                               default="**********")
    job = models.CharField(max_length=30,
                           verbose_name="Профессия",
                           default="**********")
    telegram = models.CharField(max_length=30,
                                verbose_name="Ник в телеграме",
                                default="**********")
    instagram = models.CharField(max_length=30,
                                 verbose_name="Ник в инстаграме",
                                 default="**********")

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name="Пользователь")

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
