# Django and Django REST Framework examples

Worked examples of Django and Django REST Framework (DRF), from a first project through to class-based API views, viewsets and authentication. Each folder is a standalone project you can run on its own.

## Projects

| Folder | What it covers |
|--------|----------------|
| [`DjangoRestApi/`](DjangoRestApi/) | A REST API for companies and employees using DRF `ModelViewSet`, serializers and a router. The core CRUD example. |
| [`Authentication/`](Authentication/) | Signup, login and logout with Django's built-in auth, with templates for the forms. |
| [`eshop/`](eshop/) | A small store app with products, categories and customers, plus file uploads. |
| [`MoviePracticeProject/`](MoviePracticeProject/) | Movies, actors and roles, showing many-to-many relations through an intermediate model. |
| [`office_emp/`](office_emp/) | Employees and departments, a simple one-to-many relationship app. |

## The same API view five ways

The four files at the repo root implement the same course list and detail endpoints using each style DRF offers, so you can compare them side by side:

- `ClassBased-FunctionBased-View.py`: function views with `@api_view`, and the plain `APIView` class.
- `ClassBased-View-using-mixin.py`: `GenericAPIView` combined with `ListModelMixin`, `CreateModelMixin`, and friends.
- `ClassBased-View-using-generics.py`: the concrete generic views such as `ListAPIView` and `RetrieveUpdateDestroyAPIView`.
- `ClassBased-View-using-ViewSet.py`: a `ViewSet` wired up through a router.

## Run any project

```bash
pip install django djangorestframework
cd DjangoRestApi            # or any other project folder
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open http://127.0.0.1:8000/ (the browsable API) or http://127.0.0.1:8000/admin/.

`django.txt` is a cheat sheet of the `manage.py` commands used along the way.
