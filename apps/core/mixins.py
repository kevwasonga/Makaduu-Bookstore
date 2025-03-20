from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

class PublisherRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_publisher and self.request.user.verified_publisher

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        elif not self.request.user.is_publisher:
            raise PermissionDenied("You must be a publisher to access this page.")
        else:
            raise PermissionDenied("Your publisher account needs to be verified.")
