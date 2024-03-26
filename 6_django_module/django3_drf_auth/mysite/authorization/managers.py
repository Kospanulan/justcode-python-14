from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, password, role=3):
        user = self.model(username=username)
        user.set_password(password)
        user.role = role
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password, role=1)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

