FROM python:3.7
RUN mkdir /install
WORKDIR /install
COPY . .
RUN make dev-env
RUN make deps
CMD ["make"]