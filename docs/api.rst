API
===

This part of the documentation lists the full API reference of all classes and functions.

WSGI
----

.. autoclass:: mawazo.wsgi.ApplicationLoader
   :members:
   :show-inheritance:

Config
------

.. automodule:: mawazo.config

.. autoclass:: mawazo.config.application.Application
   :members:
   :show-inheritance:

.. autoclass:: mawazo.config.redis.Redis
   :members:
   :show-inheritance:

.. automodule:: mawazo.config.gunicorn

CLI
---

.. automodule:: mawazo.cli

.. autofunction:: mawazo.cli.cli.cli

.. autofunction:: mawazo.cli.utils.validate_directory

.. autofunction:: mawazo.cli.serve.serve

App
---

.. automodule:: mawazo.app

.. autofunction:: mawazo.app.asgi.on_startup

.. autofunction:: mawazo.app.asgi.on_shutdown

.. autofunction:: mawazo.app.asgi.get_application

.. automodule:: mawazo.app.router

Controllers
~~~~~~~~~~~

.. automodule:: mawazo.app.controllers

.. autofunction:: mawazo.app.controllers.ready.readiness_check

Models
~~~~~~

.. automodule:: mawazo.app.models

Views
~~~~~

.. automodule:: mawazo.app.views

.. autoclass:: mawazo.app.views.error.ErrorModel
   :members:
   :show-inheritance:

.. autoclass:: mawazo.app.views.error.ErrorResponse
   :members:
   :show-inheritance:

Exceptions
~~~~~~~~~~

.. automodule:: mawazo.app.exceptions

.. autoclass:: mawazo.app.exceptions.http.HTTPException
   :members:
   :show-inheritance:

.. autofunction:: mawazo.app.exceptions.http.http_exception_handler

Utils
~~~~~

.. automodule:: mawazo.app.utils

.. autoclass:: mawazo.app.utils.aiohttp_client.AiohttpClient
   :members:
   :show-inheritance:

.. autoclass:: mawazo.app.utils.redis.RedisClient
   :members:
   :show-inheritance:
