from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
  confirmPassword = serializers.CharField(style={'input-type':'password'}, write_only=True)

  class Meta:
    model = Account
    fields = ['email', 'username','password','confirmPassword']
    extra_kwargs = {
       'password':{'write_only':True}
    }

    def save(self):
      account = Account(
        email = self.validate_data['email'],
        username = self.validate_data['username'],
      )
      password = self.validate_data['password']
      confirmPassword = self.validate_data['confirmPassword']

      if password != confirmPassword:
        raise serializers.ValidationError({'password' : 'passwords must match.'})
      account.set_password(password)
      account.save()
      return account





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer