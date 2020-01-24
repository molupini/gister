# base
FROM python:3.8-buster as base

# ARGUMENTS
ARG USERNAME=BretFisher
ARG FOLOW=true

# ENVIRONMENTS
ENV USERNAME=${USERNAME}
ENV FOLLOW=${FOLLOW}
ENV PORT=8080
EXPOSE ${PORT}

RUN pip3 install fire
RUN pip3 install requests

WORKDIR /bin/app

# dev
FROM base as dev
CMD ["gist.py", "run"] 
ENTRYPOINT [ "python" ]
#  ${username}, ${follow}
# prod
FROM base as prod
COPY ./src/. .
CMD ["gist.py", "run"] 
ENTRYPOINT [ "python" ]
