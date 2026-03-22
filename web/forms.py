from django import forms


class CustomSignupForm(forms.Form):
    full_name = forms.CharField(max_length=150, required=False, label='Full Name')

    def signup(self, request, user):
        parts = self.cleaned_data['full_name'].strip().split(' ', 1)
        user.first_name = parts[0]
        user.last_name = parts[1] if len(parts) > 1 else ''
        user.save()
        return user
