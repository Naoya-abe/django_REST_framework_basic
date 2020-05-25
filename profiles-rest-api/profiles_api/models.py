from django.db import models

# AbstractBaseUserを利用してUserモデルをカスタマイズ
from django.contrib.auth.models import AbstractBaseUser
# PermissionsMixinを用いてUserの認証を行う
from django.contrib.auth.models import PermissionsMixin
# BaseUserManager利用してUserManagerモデルをカスタマイズ
from django.contrib.auth.models import BaseUserManager
# profiles_projectのsettings.pyを参照できるようにする
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    # ユーザを作成するメソッド
    def create_user(self, email, name, password=None):
        """Create a new user profile"""

        # emailが入力されていないときはValueErrorを呼び出す
        if not email:
            raise ValueError('User must have an email address')

        # emailのドメインを小文字に変換
        email = self.normalize_email(email)

        # UserProfileモデルを参照してuserを定義
        user = self.model(email=email, name=name)

        # userが入力したパスワードをハッシュ化
        user.set_password(password)

        # settings.pyでdefaultに設定されているDBに保存
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""

        # 上記create_userを利用
        user = self.create_user(email, name, password)

        # superuserの権限を適用
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    # カラム名 = データ型（オプション）
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    # ユーザが退会したらここをFalseにする(論理削除)
    is_active = models.BooleanField(default=True)

    # 管理画面にアクセスできるか
    is_staff = models.BooleanField(default=False)

    # Managerのメソッドを使えるようにする
    objects = UserProfileManager()

    # emailを利用したログイン認証に変更
    USERNAME_FIELD = 'email'

    # 必須項目追加
    REQUIRED_FIELDS = ['name']

    # 1つのnameフィールドで表示したいので、既存のメソッドをオーバーライド
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    # 管理画面などで表示される文字列を定義
    def __str__(self):
        return self.email


class ProfilesFeedItem(models.Model):
    """Profile status update"""

    # 外部キーの設定(ForeignKey=多:1)
    user_profile = models.ForeignKey(
        # to:どのmodelと関係をもたせるか
        settings.AUTH_USER_MODEL,
        # CASCADE:外部キーが削除されたら一緒に消える
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
