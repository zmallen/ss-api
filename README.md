# ss-api
Silly Simple API

This is a [Django Rest Framework](https://www.django-rest-framework.org/) template for deploying an app on https://fly.io

Some features of this template:

1. No session authentication - it assumes you use fly.io, which gives you access to run commands directly via `manage.py`
2. HTTP health checks - using fly.io's [http checks](https://fly.io/docs/reference/configuration/#services-http_checks), you can have fly connect to this app and issue a basic request against `/ping/` to check DB connectivity
3. Local dev via `docker compose` and a `Dockerfile` to run the app
4. OpenAPI and Swagger ready via `drf-yasg` package
5. Ready to go: clone and run on fly via `fly launch`, then run a migration and get a dev token via:
  * `fly ssh console -C 'python /app/manage.py migrate`
  * `fly ssh console -C 'python /app/manage.py getdevtoken'`

For a blog post going into more detail of the app makeup, please go to:

** CHANGE THIS **
https://dev.to/teachmetechy/django-rest-framework-on-flyio-29gh-temp-slug-7902488?preview=9cf35c7e8c0dd689a1be384dcdc2fc11a8d33ba79aa0bed4035e3c3aec8fd01b537ea3fb8588b4606b25ca16c4f7bfdca34e0a78c06f21a8c3924458
