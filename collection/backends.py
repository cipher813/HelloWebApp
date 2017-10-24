from registration.backends.simple.views import RegistrationView

# new registration view, subclassing RegistrationView from plugin
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        # named URL to redirect to after successful registration
        return ('registration_create_thing')
