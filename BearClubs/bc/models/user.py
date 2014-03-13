from django.contrib import auth

class User(auth.models.User):
    # Following fields inherited from auth.models.User
    # ------------------------------------------------
    # username     = models.CharField(max_length=128, unique=True);
    # password     = models.CharField(max_length=128, unique=True);
    # email        = models.EmailField(max_length=128, unique=True);
    # first_name   = models.CharField(max_length=64);
    # last_name    = models.CharField(max_length=64);

    class Meta:
        app_label = 'bc';
