from django.contrib.auth.models import User
from django.http import HttpRequest


class EmailAuthBackend:
    '''
    Authenticate using an e-mail address.
    '''

    def authenticate(
        self, request: HttpRequest, username: str = None, password: str = None
    ) -> User | None:
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id: int) -> User | None:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
