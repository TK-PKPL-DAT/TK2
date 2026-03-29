from django.conf import settings


def allowed_member(request):
    is_allowed = (
        request.user.is_authenticated
        and request.user.email in settings.ALLOWED_MEMBERS
    )
    return {'is_allowed_member': is_allowed}
