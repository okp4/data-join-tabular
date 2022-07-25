# -----
FROM okp4/gdal-python:3.9.13 AS builder

ENV \
    # poetry:
    POETRY_VERSION=1.1.7 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.poetry/bin"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y  \
  && rm -rf /var/lib/apt/lists/*

ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /build

COPY poetry.lock pyproject.toml ./
RUN  poetry config virtualenvs.create false \
  && poetry install --no-root --no-dev

COPY src src

RUN poetry build

# -----
FROM okp4/gdal-python:3.9.13

LABEL org.opencontainers.image.source=https://github.com/okp4/data-join-tabular

COPY --from=builder /build/dist/*.whl /tmp/whl/

RUN python3 -m pip install --no-cache-dir /tmp/whl/*.whl \
  && rm -rf /tmp/whl \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y  \
  && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["data-join-geospatial"]
