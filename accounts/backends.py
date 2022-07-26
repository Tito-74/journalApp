from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CaseInsensitiveModelBackend(ModelBackend):

  def authenicate(self, request, username=None, password=None, **kwargs):
    UserModel = get_user_model
    if UserModel is None:
      username = kwargs.get(UserModel.USERNAME_FIELD)
    try:
      case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
    except UserModel.DoesNotExist:
      UserModel().set_password(password)
    else:
      if user.check_password(password) and self.user_can_authenticate(user):
        return user
