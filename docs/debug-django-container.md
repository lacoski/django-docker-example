# Debugging Python Django trong Container

## Tại env, thêm gói ptvsd

```
ptvsd==4.3.2
```

## Tại Lauch Json thêm

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Remote Django App",
            "type": "python",
            "request": "attach",
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "/usr/src/app/"
                }
            ],
            "port": 3000,
            "host": "localhost"
        }
    ]
}
```

Lưu ý:
- remoteRoot = `/usr/src/app/`

## Tại `manage.py` thêm

```
    if settings.DEBUG:
        if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
            import ptvsd
            ptvsd.enable_attach(address = ('0.0.0.0', 3000))

    execute_from_command_line(sys.argv)
```


File mẫu

```
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.conf import settings

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    if settings.DEBUG:
        if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
            import ptvsd
            ptvsd.enable_attach(address = ('0.0.0.0', 3000))

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

## Tại docker compose, mở thêm port 3000

```
version: '3.4'

services:
  djangodockerexample:
    image: djangodockerexample
    build:
      context: .
      dockerfile: Dockerfile.test
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./:/usr/src/app/
    ports:
      - 8000:8000
      - 3000:3000
```