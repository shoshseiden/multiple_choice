from django import forms


class StudentLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        if username != "student":
            raise forms.ValidationError("Incorrect username/password")
        if password != "a":
            raise forms.ValidationError("Incorrect username/password")
        return self.cleaned_data


class InstructorLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        if username != "instructor":
            raise forms.ValidationError("Incorrect username/password")
        if password != "b":
            raise forms.ValidationError("Incorrect username/password")
        return self.cleaned_data
