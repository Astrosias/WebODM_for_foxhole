from app.plugins import PluginBase, Menu, MountPoint
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required

class Plugin(PluginBase):

    def main_menu(self):
        return [Menu(_("Video editor"), self.public_url(""), "fa fa-map-marker-alt fa-fw")]

    def app_mount_points(self):
        @login_required
        def render_app(request):
            return render(request, self.template_path("app.html"), {'title': 'Sample your videos'})

        return [
            MountPoint('$', render_app)
        ]


