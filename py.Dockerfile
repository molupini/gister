# base
FROM python:3.8-buster as base

# ARGUMENTS
ARG username=BretFisher
ARG follow=true

# ENVIRONMENTS
ENV username=${username}
ENV follow=${follow}
ENV PORT=8080
EXPOSE ${PORT}

RUN pip3 install fire
RUN pip3 install requests

WORKDIR /bin/app

# dev
FROM base as dev
CMD ["gist.py", "run", ${username}, ${follow}] 
ENTRYPOINT [ "python" ]

# prod
FROM base as prod
COPY ./src/. .
CMD ["gist.py", "run", ${username}, ${follow}] 
ENTRYPOINT [ "python" ]
