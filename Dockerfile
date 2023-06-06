FROM python:3.11-alpine as base
RUN apk update

FROM base as base_build
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade --target=/dependencies -r /tmp/requirements.txt

FROM base
COPY --from=base_build /dependencies /usr/local/lib/python3.11/site-packages/

WORKDIR /src
COPY ./src/ /src/
COPY ./entrypoint.sh  /user/local/entrypoint.sh

RUN ["chmod", "+x", "/user/local/entrypoint.sh"]
