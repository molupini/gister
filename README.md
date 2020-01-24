# USER PUBLIC GIST SCRIPT

Powered by Python and Docker.

  - Edit Environment Variables 
  - Deploy with docker-compose 

#### Features

You can:
  - See User Public Gist(s) 
  - Console Out New Gist
  - Saved to File for Persistance 
  
## Installation

#### Install

Open your favorite Terminal and run these commands.

First, if necessary:
```sh
$ mkdir ./gist 
```
Second:
```sh
$ git gist
```
Third:
```sh
$ git clone git@github.com:molupini/userPublicGist.git
```

Forth:
```sh
$ mkdir ./.env
```

#### Author

Making any change in your source file will update immediately.

Before we begin, required environment variables:
```sh
$ vi ./.env/app.env
AUTH_TOKEN=null
USERNAME=BretFisher
FOLLOW=true
RATE=120
```


#### Deploy & Execute 

Easily done in a Docker container.
Make required changes within Dockerfile + compose files if necessary. When ready, simply use docker-compose to build your environment.
This will create the *gist, ...* services with necessary dependencies.

For dev, docker compose:
```sh
$ docker-compose build
$ docker-compose up
```

Verify the deployment monitoring the console
```sh
$ {'result': 'BretFisher gist.id found 2a7f882ac5a30c9e7c45'}
```

For prod, build:
```sh
$ docker build -f py.Dockerfile -t mauriziolupini/gist:prod .
```

Commit prod, push docker builds:
```sh
$ docker push mauriziolupini/gist:prod
```

## Kubernetes + Google Cloud

See [KUBERNETES.md] coming soon.


### License

MIT


### Author
**Want to contribute? Great! See repo [git-repo-url] from [Maurizio Lupini][mo]    -Author, Working at [...][linkIn]**


   [mo]: <https://github.com/molupini>
   [linkIn]: <https://za.linkedin.com/in/mauriziolupini>
   [git-repo-url]: <git@github.com:molupini/userPublicGist.git>
   [python]: <https://www.python.org/>
   [git]: <https://git-scm.com/>