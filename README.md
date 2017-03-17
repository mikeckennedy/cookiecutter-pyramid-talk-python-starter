# Talk Python's Pyramid Web App Starter

An opinionated **_Cookiecutter_** template for creating Pyramid web applications starting way further down the development chain. This cookiecutter template will create a new Pyramid web application with the following benefits and more:

* **Factored and organized**: This code was generalized out of a large, professional web application
* **Master layout template**: Comes pre-configured with a master layout template. Navigation, CSS, JS, etc is factored into a single template file.
* **Chameleon language**: This template uses the chameleon template language (the cleanest template language for Python - we did say opinionated right?)
* **Pyramid Handlers**: Code is factored into handler / controller classes. You have the full power of object-oriented programming immediately available
* **Secure user management**
* **SQLAlchemy data access**
* **Bootstrap and modern design**
* **Logging with [LogBook](https://logbook.readthedocs.io/en/stable/)**: A logging system for Python that replaces the standard library’s logging module. It was designed with both complex and simple applications in mind and the idea to make logging fun
* **Runtime error monitoring with [Rollbar](https://rollbar.com)**: Rollbar adds runtime notifications and detailed error tracking and it comes pre-configured in this template
* **Mailing list integration**: [Mailchimp](https://mailchimp.com/)
* **Outbound email with templates**:
* **Bower static resource management**:
* **Fast pages that are never stale**:* 

## What you get

Here's a screenshot of the home page. You also get much more as you navigate other sections of the web app.

![](https://raw.githubusercontent.com/mikeckennedy/cookiecutter-pyramid-talk-python-starter/master/readme_resources/app-screenshot.png)

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