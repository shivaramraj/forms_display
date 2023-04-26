from django import forms
c=[('MALE','male'),('FEMALE','female')]
class StudentForms(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=20)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    # address=forms.CharField(max_length=20,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    # # gender=forms.ChoiceField(choies=c,widget=forms.RadioSelect)
    # gender=forms.ChoiceField(choices=c,widget=forms.RadioSelect)
