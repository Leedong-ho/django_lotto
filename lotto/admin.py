from django.contrib import admin

from lotto.models import GuessNumbers
# == from .models import  - 같은 폴더안의 파일에 접근 할때 . 만찍어서도 가능

# Register your models here.

admin.site.register(GuessNumbers)
