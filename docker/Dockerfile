ARG BASE_IMAGE=scailfin/madgraph5-amc-nlo:mg5_amc2.8.1
# hadolint ignore=DL3006
FROM ${BASE_IMAGE} as base

FROM base as builder
COPY . /code
# hadolint ignore=DL3003
RUN apt-get -qq -y update && \
    apt-get -qq -y install --no-install-recommends \
        git && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/* && \
    cd /code && \
    python -m pip install --upgrade --no-cache-dir pip setuptools wheel && \
    python -m pip install --no-cache-dir . && \
    python -m pip list

FROM base
RUN apt-get -qq -y update && \
    apt-get -qq -y install --no-install-recommends \
        curl && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local /usr/local
ENTRYPOINT ["pymela"]
