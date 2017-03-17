from django import forms

class signinForm(forms.Form):
	name=forms.CharField(label='用户名',max_length=50)
	password=forms.CharField(label='密码',widget=forms.PasswordInput())

class registerForm(forms.Form):
	name=forms.CharField(label='用户名:',max_length=50)
	password1=forms.CharField(label='密码:',widget=forms.PasswordInput())
	password2=forms.CharField(label='确认密码:',widget=forms.PasswordInput())
	email=forms.EmailField(label='电子邮箱:')

class create_blogForm(forms.Form):
	title=forms.CharField(label='标题:',max_length=100)
	summary=forms.CharField(label='摘要:',max_length=100)
	content=forms.CharField(label='正文:',widget=forms.Textarea)