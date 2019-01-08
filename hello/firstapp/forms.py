from django import forms


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "myfield"}))
    
# class UserForm(forms.Form):
#     name = forms.CharField(min_length=3)
#     age = forms.IntegerField(min_value=1, max_value=100)
#     required_css_class = "field"
#     error_css_class = "error"

# class UserForm(forms.Form):
#     name = forms.CharField(min_length=3)
#     age = forms.IntegerField(min_value=1, max_value=100)

# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()

# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField(min_value=1, max_value=100)
#     weight = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)

# class UserForm(forms.Form):
#     name = forms.CharField(min_length=2, max_length=20)
#     email = forms.EmailField(required=False, min_length=7)

# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField(required=False)
#     email = forms.EmailField(required=False)

# class UserForm(forms.Form):
#     name = forms.CharField(help_text="Enter your name")
#     age = forms.IntegerField(help_text="Enter your age")

# class UserForm(forms.Form):
#     name = forms.CharField(initial="undefined")
#     age = forms.IntegerField(initial=18)
# class UserForm(forms.Form):
#     name = forms.CharField(label="Name")
#     comment = forms.CharField(label="Comment", widget=forms.Textarea)
#
# class UserForm(forms.Form):
#     name = forms.CharField(label="NAME")
#     age = forms.IntegerField(label="AGE")
