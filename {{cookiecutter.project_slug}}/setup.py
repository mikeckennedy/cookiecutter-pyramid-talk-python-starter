import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'html2text',
    'logbook',
    'mailchimp',
    'mailer',
    'passlib',
    'pyramid',
    'pyramid_chameleon',
    # 'pyramid_debugtoolbar', # installed via pip3 install -r requirements-dev.txt
    'pyramid_handlers',
    'rollbar',
    'sqlalchemy',
    # 'waitress', # installed via pip3 install -r requirements-dev.txt
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compatibility
    'pytest',  # includes virtualenv
    'pytest-cov',
]

setup(name='{{cookiecutter.project_slug}}',
      version='0.0',
      description='Site with CMS',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Talk Python',
      author_email='contact@talkpython.fm',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = {{cookiecutter.project_slug}}:main
      """,
      )

print()
print()
print('**************************************************************')
print('*')
print("*        Be sure to run 'pip3 install -r requirements-dev.txt'")
print("*        if this is your dev install. Otherwise the dev server")
print("*        and debug toolbar will be absent.")
print('*')
print('**************************************************************')
