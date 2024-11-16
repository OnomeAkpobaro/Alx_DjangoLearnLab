from django.apps import AppConfig




class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'
    
class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

  # from .models import CustomUser, Bookshelf
        # from django.contrib.contenttypes.models import ContentType
# Content_type = ContentType.objects.get_for_model(Bookshelf)
# permission =  Permission.objects.get(
#     codename= 'can_add',
#     name = 'Can add book',
#     Content_type = Content_type
#     )
# CustomUser.user_permissions.add(permission)