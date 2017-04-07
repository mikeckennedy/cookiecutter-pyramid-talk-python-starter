import pyramid_handlers
from pyramid.response import Response

from {{cookiecutter.project_slug}}.controllers.base_controller import BaseController
from {{cookiecutter.project_slug}}.services.cms_service import CmsService


class CMSController(BaseController):
    @pyramid_handlers.action(renderer='templates/cms/page.pt')
    def page(self):
        url = self.request.path_url.replace(self.request.host_url, '')
        page = CmsService.get_page_by_url(url)

        if not page:
            return Response(status=404, body="Not found.")

        if page.is_redirect:
            return self.redirect(page.redirect_url)

        return {'html': page.html}
