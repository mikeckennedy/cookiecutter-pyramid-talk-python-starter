from {{cookiecutter.project_slug}}.data.cms_page import CmsPage
from {{cookiecutter.project_slug}}.data.dbsession import DbSessionFactory


class CmsService:
    @classmethod
    def get_page_by_url(cls, url):
        if not url:
            return None

        url = url.lower().strip()
        session = DbSessionFactory.create_session()

        page = session.query(CmsPage) \
            .filter(CmsPage.url == url) \
            .first()

        return page

    @classmethod
    def add_page(cls, url, html, is_redirect=False, redirect_url=None):
        if not url or not url.strip():
            raise ValueError('url cannot be empty')

        url = url.lower().strip()
        session = DbSessionFactory.create_session()

        page = CmsPage()
        page.url = url
        page.html = html
        page.is_redirect = is_redirect
        page.redirect_url = redirect_url

        session.add(page)
        session.commit()

        return page

    @classmethod
    def init_test_data(cls):
        url = '/landing_pages/a_dynamic_cms_page'

        if cls.get_page_by_url(url) is not None:
            return

        cls.add_page(
            url,
            '<h1>This is a CMS page</h1>\n' +
            '\n' +
            '<p>\n' +
            'You can create them in the DB and any URL can be mapped.<br>\n' +
            'See CmsController / CmsService for more info.\n' +
            '</p>\n'
        )
