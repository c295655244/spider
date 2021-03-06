 #coding=utf-8
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)#检查字段长度
    email = forms.EmailField(required=False,label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)#forms框架把每一个字段的显示逻辑分离到一组部件（widget）中

    #form系统自动寻找匹配的函数方法，该方法名称以clean_开头，并以字段名称结束
   # def clean_message(self):#最起码写四个字
     #   message = self.cleaned_data['message']
       # num_words = len(message.split())
        #if num_words < 4:
         #   raise forms.ValidationError("Not enough words!")
        #return message
