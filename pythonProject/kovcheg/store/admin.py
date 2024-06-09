# from django.contrib import admin
#
# # Register your models here.
from django.contrib import admin, messages
from django.utils.safestring import mark_safe
#
from .models import Store, Category,TagPost, Brand,Age,TypeFeed,Size



@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    save_on_top = True#панель сохранения дублируется сверху
    readonly_fields = ['post_photo'] #запрет на редактирование формы
    prepopulated_fields = {'slug': ('title',)} #автослаг
    list_display = ('id','post_photo','title','typeFeed','is_published','price') #что отображаем в админ панеле
    list_display_links = ('id','title') #кликабельные ссылки
    filter_horizontal = ['tags','size','age'] #горизонтальная форма для тэгов
    ordering = ['title','time_created']
    actions = ['set_published','set_draft'] # новое действие при выборе
    search_fields = ['title'] #поисковая строка
    list_filter = ['cat2__name','is_published','brand','size','tags'] #мой фильтр фильтр встроенный

    @admin.display(description='Изображение')
    def post_photo(self, store:Store):#своя строка в админ панеле
        if store.photo:
            return mark_safe(f"<img src='{store.photo.url}' width=50>")
        return "без фото"

    @admin.action(description='Опубликовать выбанные записи')
    def set_published(self,request,queryset):#свое действие в выпадающем меню
        count = queryset.update(is_published=Store.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")
    @admin.action(description='снять с публикации')

    def set_draft(self, request, queryset):  # свое действие в выпадающем меню
        count = queryset.update(is_published=Store.Status.DRAFT)
        self.message_user(request, f" {count} снято с публикации", messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')#что отображаем
    list_display_links = ('id','name') #кликабельрные
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Age)
class AgeAdmin(admin.ModelAdmin):
    list_display = ('id','name')#что отображаем
    list_display_links = ('id','name') #кликабельрные
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id','name')#что отображаем
    list_display_links = ('id','name') #кликабельрные
    prepopulated_fields = {'slug': ('name',)}

@admin.register(TypeFeed)
class AgeAdmin(admin.ModelAdmin):
    list_display = ('id','name')#что отображаем
    list_display_links = ('id','name') #кликабельрные
    prepopulated_fields = {'slug': ('name',)}

@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ('id','tag')
    list_display_links = ('id', 'tag')
    prepopulated_fields = {'slug': ('tag',)}


@admin.register(Brand)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    prepopulated_fields = {'slug': ('name',)}


