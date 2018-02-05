
# Django
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

# local Django
from users.models import User


class StaffRequiredMixin(object):
    """
    Mixin which requires the admin privileges.
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(
            request, *args, **kwargs
        )


class UserPerfilMixin(object):

    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(id=self.kwargs['pk'])
        if user == request.user:
            return super(UserPerfilMixin, self).dispatch(
                request, *args, **kwargs
            )
        else:
            return redirect('user:index')


class UserPerfilRestMixin(object):

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object().user.id
        if user == request.user.id:
            return super(UserPerfilRestMixin, self).dispatch(
                request, *args, **kwargs
            )
        else:
            return redirect('user:index')
