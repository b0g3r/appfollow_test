# appfollow_test
Test assignment for [AppFollow](https://appfollow.io) as Python-developer. MIT Licence

## How to launch
You need a docker>=17.06 and docker-compose>=3.3

Type `docker-compose up` in project directory and project will be available at `http://localhost`

## Checkers
All python sub-projects containts mypy and wemake-python-styleguide (flake8) as dev-dependencies. For running checks
you can use commands

`mypy .`

and

`flake8`

If you don't want to install dependencies in your system (good point) you can run checks in Docker or with project
 dependency manager: `poetry install && poetry run mypy .`.
 
## Services

### fetcher
Looks through database and wait for new app permissions requests, then processes theirs. Parses response from private
 GooglePlay Store API, downloads icons for permission blocks.

### api
Service-API which maintain permission requests via JSON requests API. Contains only one sad endpoint.

### frontend
Little frontend on vue + semantic-ui. Makes responses, spins loading, shows permissions. Distributed by nginx with
 shared volume with permissions block icons. Building when Dockerfile builds within multi-stage build.

## TODO:
 - [ ] Фатальный недостаток в fetcher модуле, на который аж линтер ругается -- слишком сложный парсинг блоков разрешений
 - [x] Демо
 - [ ] Не получилось использовать collection.watch, из того что понял -- нужно запустить монго в режиме репликации, 
 если будет скучно, надо будет побороть
 - [ ] Не запаривался с фронтендом, возможно стоит нормально разнести по компонентам и прибраться в стилях
