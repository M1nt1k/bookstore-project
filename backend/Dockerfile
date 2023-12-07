FROM python:3.11 AS builder

WORKDIR /app/backend

COPY poetry.lock pyproject.toml ./
COPY . ./

RUN python -m pip install --no-cache-dir poetry==1.4.2 \
    && python -m poetry config virtualenvs.in-project true \
    && python -m poetry install --without dev,test --no-interaction --no-ansi

CMD ["python", "-m", "poetry", "run", "serve"]
