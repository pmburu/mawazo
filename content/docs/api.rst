API
===

This part of the documentation lists the full API reference of all classes and functions.

WSGI
----

.. autoclass:: content.wsgi.ApplicationLoader
   :members:
   :show-inheritance:

Config
------

.. automodule:: content.config

.. autoclass:: content.config.application.Application
   :members:
   :show-inheritance:

.. autoclass:: content.config.redis.Redis
   :members:
   :show-inheritance:

.. automodule:: content.config.gunicorn

CLI
---

.. automodule:: content.cli

.. autofunction:: content.cli.cli.cli

.. autofunction:: content.cli.utils.validate_directory

.. autofunction:: content.cli.serve.serve

App
---

.. automodule:: content.app

.. autofunction:: content.app.asgi.on_startup

.. autofunction:: content.app.asgi.on_shutdown

.. autofunction:: content.app.asgi.get_application

.. automodule:: content.app.router

Controllers
~~~~~~~~~~~

.. automodule:: content.app.controllers

.. autofunction:: content.app.controllers.ready.readiness_check

Models
~~~~~~

.. automodule:: content.app.models

Views
~~~~~

.. automodule:: content.app.views

.. autoclass:: content.app.views.error.ErrorModel
   :members:
   :show-inheritance:

.. autoclass:: content.app.views.error.ErrorResponse
   :members:
   :show-inheritance:

Exceptions
~~~~~~~~~~

.. automodule:: content.app.exceptions

.. autoclass:: content.app.exceptions.http.HTTPException
   :members:
   :show-inheritance:

.. autofunction:: content.app.exceptions.http.http_exception_handler

Utils
~~~~~

.. automodule:: content.app.utils

.. autoclass:: content.app.utils.aiohttp_client.AiohttpClient
   :members:
   :show-inheritance:

.. autoclass:: content.app.utils.redis.RedisClient
   :members:
   :show-inheritance:
