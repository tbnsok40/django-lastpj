from django import forms # 폼을 사용해야 하기 때문에 import 해줍니다. 
from .models import Memo # 모델 기반으로 만들기로 했기 때문에 모델도 가지고 옵니다! 
class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['title','content']

        widgets = {
            'title':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'제목을 입력하세요'
                }
            ),
            'content':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'rows': '5',
                }
            )
        }
        labels = {
						'title' : '제목', 
						'content' : '내용', 
				}
