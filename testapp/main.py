from zope.event import notify

from cromlech.dawnlight import DawnlightPublisher, ViewLookup, renderer_locator, query_http_renderer
from cromlech.io.interfaces import PublicationBeginsEvent, PublicationEndsEvent
from cromlech.webob.response import Response
from cromlech.webob.request import Request
from cromlech.configuration.utils import load_zcml

from webob.dec import wsgify

from grokcore.component import context
from dolmen.view import View

view_lookup = ViewLookup(renderer_locator(query_http_renderer))

class Site(object):
    def __init__(self, name):
        self.name = name

class Index(View):
    context(Site)

    responseFactory = Response
    
    def render(self):
        return "This is the site view"

class Application(object):
    def __init__(self):
        self.site = Site('testapp')
        
    @wsgify(RequestClass=Request)
    def __call__(self, request):
        publisher = DawnlightPublisher(
            request, self, view_lookup=view_lookup)
        notify(PublicationBeginsEvent(self.site, request))

        result = publisher.publish(self.site, handle_errors=True)

        notify(PublicationEndsEvent(request, result))

        return result

def testapp(global_conf, zcml_file):
    load_zcml(zcml_file)
    return Application()
