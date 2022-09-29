from django import forms
from .models import GuessNumbers


class PostForm(forms.ModelForm):

    class Meta:  # models.py에 있는 클래스를 기반으로하여 그내용을 채울수 있는 양식을 만들것인지
                     # 이때 class Meta: 를 지정함 - 약속임
        model = GuessNumbers
        fields = ('name', 'text', )

# 이후에 이 양식을 보여주고 유저에게 post요청을 받아낼 urlpatten을 만들기 -> urls.py
