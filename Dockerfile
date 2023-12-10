ARG PIP_TOOLS_VERSION=7.3.0
ARG PIP_DISABLE_PIP_VERSION_CHECK=1
ARG PIP_ROOT_USER_ACTION=ignore

# build stage:
FROM python:3.11 AS build

ARG PIP_TOOLS_VERSION
ARG PIP_DISABLE_PIP_VERSION_CHECK
ARG PIP_ROOT_USER_ACTION

WORKDIR /app
COPY requirements.in requirements.txt ./

RUN apt-get update && apt-get install -y --no-install-recommends  \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir --no-cache install "pip-tools==$PIP_TOOLS_VERSION"
RUN cp requirements.txt old.requirements.txt \
    && pip-compile --strip-extras --generate-hashes -q -o requirements.txt requirements.in
RUN echo "Repo/Container Requirements Differences:"  \
    && (diff requirements.txt old.requirements.txt || true)

RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements.txt

# production stage:
FROM python:3.11-slim

ARG PIP_DISABLE_PIP_VERSION_CHECK
ARG PIP_ROOT_USER_ACTION

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DJANGO_SETTINGS_MODULE="salekcodes.settings"

WORKDIR /app
COPY --from=build /app/wheels /wheels
COPY . .

RUN pip install --no-cache-dir --no-cache /wheels/*

EXPOSE 8001

CMD ["/bin/bash", "entrypoint.sh"]
