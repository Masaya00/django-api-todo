from django.db import models


class BaseModel(models.Model):
    is_deleted = models.BooleanField('削除フラグ', default=False)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        abstract=True


class Category(BaseModel):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=30)

    class Meta:
        db_table = 'category'


class Post(BaseModel):
  title = models.CharField('タイトル', max_length=50)
  content = models.TextField('コンテンツ')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
  view_count = models.IntegerField('閲覧回数', default=0)
  favorite_count = models.IntegerField('お気に入り数', default=0)
  is_private = models.BooleanField('非公開フラグ', default=0)

  class Meta:
    db_table = 'post'

  def __str__(self) -> str:
    return self.title


class Task(models.Model):
  title = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.id}-{self.title}'