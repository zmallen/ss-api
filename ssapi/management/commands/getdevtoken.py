# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django_extensions.management.color import color_style
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Gets an admin token for local dev'

    def get_token(self, user):
        return user.auth_token

    def handle(self, *args, **options):
        stylin = color_style()
        user = None
        try:
            self.stdout.write(stylin.INFO('Looking for superuser..'))
            user = User.objects.get(username='superuser')
            self.stdout.write(stylin.SUCCESS('superuser found!'))
        except User.DoesNotExist:
            self.stdout.write(stylin.ERROR('superuser doesn\'t exist, creating!'))
            user = User.objects.create_user('superuser', password='superuser')
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(stylin.SUCCESS('superuser created!'))
        auth_token = self.get_token(user)
        self.stdout.write(stylin.SUCCESS('Use the following key for dev:'))
        self.stdout.write(stylin.SUCCESS(u'(｡◕‿‿◕｡)☞☞') + stylin.MODULE(stylin.BOLD('  Token %s  ' % str(auth_token))) + stylin.SUCCESS(u'☜☜(｡◕‿‿◕｡)'))
