from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import patterns, url

class WriterboxApphook(CMSApp):
    app_name = "writerbox"
    name = _("Writerbox Application")

    def get_urls(self, page=None, language=None, **kwargs):
        #self.section.section = "news"
        #return url(r'^writerbox/', include('writer.urls', namespace='writers'))
        #return "^writerbox/"
        return ["writer.urls"]


apphook_pool.register(WriterboxApphook)  # register the application
