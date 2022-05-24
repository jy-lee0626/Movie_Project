from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image
        gender = data.get("gender")
        first_name = request.data.get("first_name")
        setattr(user, "gender", gender)
        setattr(user, "first_name", first_name)
        if gender == 'Female':
            setattr(user, "profile_image", "female_avatar.png")
        else: 
            setattr(user, "profile_image", "male_avatar.png")
        user.save()
        return user