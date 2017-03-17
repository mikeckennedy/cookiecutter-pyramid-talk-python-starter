# Talk Python's Pyramid Web App Starter

An opinionated **_Cookiecutter_** template for creating Pyramid web applications starting way further down the development chain. This cookiecutter template will create a new Pyramid web application with the following benefits and more:

* **Factored and organized**: This code was generalized out of a large, professional web application
* **Master layout template**: Comes pre-configured with a master layout template. Navigation, CSS, JS, etc is factored into a single template file and is reused across all views
* **Chameleon language**: This template uses the chameleon template language (the cleanest template language for Python - we did say opinionated right?)
* **Pyramid Handlers**: Code is factored into handler / controller classes. You have the full power of object-oriented programming immediately available
* **Secure user management**: The app comes with full user management. Users can register, log in and out, and reset passwords. We use the [passlib](https://passlib.readthedocs.io/en/stable/) package for secure user storage using best practices
**SQLAlchemy data access**: Comes with [SQLAlchemy ORM](https://www.sqlalchemy.org/) preconfigured using **sqlite**
* **Bootstrap and modern design**: As you can see from the screenshot below, the app comes with [bootstrap](https://getbootstrap.com/) and [fontawesome](http://fontawesome.io/). It uses a free, [open-source theme](https://startbootstrap.com/template-overviews/landing-page/) and images used under [CC-Attribution](https://creativecommons.org/licenses/by-sa/2.0/).
* **Logging with [LogBook](https://logbook.readthedocs.io/en/stable/)**: A logging system for Python that replaces the standard library’s logging module. It was designed with both complex and simple applications in mind and the idea to make logging fun
* **Runtime error monitoring with [Rollbar](https://rollbar.com)**: Rollbar adds runtime notifications and detailed error tracking and it comes pre-configured in this template
* **Mailing list integration**: [Mailchimp](https://mailchimp.com/)
* **Outbound email with templates**: The app has a set of static HTML files with placeholders that are loaded by the outbound email system and populated with user data
* **Bower static resource management**: Most templates are based on out-of-date files (css templates, js, etc.). This template is uses [bower](https://bower.io/) for it's static files. This means a single CLI command will get you the latest everything.
* **Fast pages that are never stale**: Every static resource is referenced with our own cache busting system. This means you can use extremely aggressive caching for performance on static files yet they immediately invalidate upon changes
* **Comes with an entire online course**: This template is built from the final project in [Python for Entrepreneurs](https://training.talkpython.fm/courses/explore_entrepreneurs/python-for-entrepreneurs-build-and-launch-your-online-business), a 20 hour course on building professional web apps in Python and Pyramid from [Talk Python Training](https://training.talkpython.fm/)

## What you get

Here's a screenshot of the home page. You also get much more as you navigate other sections of the web app.

![](https://raw.githubusercontent.com/mikeckennedy/cookiecutter-pyramid-talk-python-starter/master/readme_resources/app-screenshot.png)

Here's the project folder structure:

![](https://raw.githubusercontent.com/mikeckennedy/cookiecutter-pyramid-talk-python-starter/master/readme_resources/project-structure.png)

## Usage

To use this template you just run the single command:

```
cookiecutter https://github.com/mikeckennedy/cookiecutter-pyramid-talk-python-starter
```

Answer the cookiecutter prompts (notice how smart defaults are suggested anywhere possible):

![](https://raw.githubusercontent.com/mikeckennedy/cookiecutter-pyramid-talk-python-starter/master/readme_resources/template-execution-trimmed.png)

*[Note: Once you have run cookiecutter with the full URL, it is cached locally and can be run with just the template name.]*

## Compare to Pyramid's standard templates

The Pyramid web framework offers a handful of nice starter templates. They have recently moved to [Cookiecutter](https://cookiecutter.readthedocs.io) as the primary way to [scaffold new Pyramid web applications](http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/project.html#pyramid-cookiecutters).

## Feature survey