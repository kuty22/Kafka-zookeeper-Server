# Kafka-zookeeper-Server


### summary:
  - [Introduction](#introduction)
  - [Install](#install)
  - [Start](#start)
  - [Documentation](#documentation)
  - [Reference](#reference)



## Introduction

  #### Kafka:
  Kafka® is used for building real-time data pipelines and streaming apps. It is horizontally scalable, fault-tolerant, wicked fast, and runs in production in thousands of companies.
  This is an example of kafka and zookeeper with docker.

  #### Zookeeper:
  ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications. Each time they are implemented there is a lot of work that goes into fixing the bugs and race conditions that are inevitable. Because of the difficulty of implementing these kinds of services, applications initially usually skimp on them ,which make them brittle in the presence of change and difficult to manage. Even when done correctly, different implementations of these services lead to management complexity when the applications are deployed.

  > It use an external docker network to simplify the plugging of a module.
  >
  > the process to create one is describe in [Install section](#install)

  The basic configuration haven't any topic.

  > for more information about kafka or zookeeper:
  > - [Github](https://github.com/apache/kafka/)
  > - [Kafka Website](https://kafka.apache.org)
  > - [Zookeeper Website](http://zookeeper.apache.org)


## Install

### requirement:
- [Docker](https://www.docker.com)
- [Docker-compose](https://docs.docker.com/compose/)
- [git](https://git-scm.com/documentation)
- [External Docker network](https://docs.docker.com/engine/userguide/networking/work-with-networks/)
- gradle(optional only to use kafka manualy)([install](https://gradle.org/install/))

### Two ways are available to install:
- Makefile
- basic install

If you do not have a docker network this step is not optional:
```
# The basic project use "platform-networks"
docker network create platform-networks
```
if you want to use your own docker network, you must change network field in the docker-compose.yml/docker-compose-test.yml:
docker-compose.yml:
```
# line 47 change the network name.
platform:
  external:
    name: platform-networks
```
docker-compose-test.yml:
```
# line 37 change the network name.
platform:
  external:
    name: platform-networks
```

_Makefile_:
1. install external module:
```
make install
```
2. build project:
```
make build
```
3. test(optional)
```
  # the test will run a python3 container which will test:
  # - topic creation
  # - data transfers
  # - multiple client

  make test
```
  make test build and up a python3 container which will run a script and display to you
  tests logs, then the container down and you can clean the Kafka memory with a down_build_up
  or continue to use it(tests created and added data to ["test","testSec"] topic).

_basic install_:
1. install external modules:
```
  git submodule init

  git submodule update
```

2. build project:
```
  docker-compose build
```

3. test(optional):
```
  docker-compose down

  docker-compose -f docker-compose-test.yml build

  docker-compose -f docker-compose-test.yml up -d

  docker-compose -f docker-compose-test.yml logs test_module
```
  make test build and up a python3 container which will run a script and display to you
  tests logs, then the container down and you can clean the Kafka memory with a down_build_up
  or continue to use it(tests created and added data to ["test","testSec"] topic).
## Start

> Tests process is advising,

> seen above for more explanation.

For start your server:
```
  # down/build/up (more information on Documentation section)
  make
```

you can verify your platform is up with:
```
  make ps
```

for logs:
```
  # all logs
  make logs

  # specific service
  # example:
  #   make logs service=kafka
  make logs service=<module-name>
```

## Documentation

_Makefile commands available_:

|   **commands name**   | **description**                    |
|:---------------------:|:---------------------------------- |
|        `make`         | 1. down each service               |
|                       | 2. build basic project             |
|                       | 3. run project                     |
|                       |                                    |
|    `make build_up`    | 1. build basic project             |
|                       | 2. run project                     |
|                       |                                    |
|     `make build`      | build basic project.               |
|                       |                                    |
|       `make up`       | run project                        |
|                       |                                    |
|      `make down`      | down project                       |
|                       |                                    |
|      `make test`      | 1. down each service               |
|                       | 2. build test                      |
|                       | 3. run tests                       |
|                       |                                    |
| `make build_up_test`  | 1. build test                      |
|                       | 2. run tests                       |
|                       |                                    |
|   `make build_test`   | build basic project.               |
|                       |                                    |
|    `make up_test`     | run tests                          |
|                       |                                    |
|   `make down_test`    | down test                          |
|                       |                                    |
|       `make ps`       | list container                     |
|                       |                                    |
|      `make logs`      | display all platform logs          |
|                       |                                    |
| `make logs service=?` | display logs for a specific module |


Tricks:

|              **commands**              | **description**         |
|:--------------------------------------:|:----------------------- |
| `docker network create "Network-Name"` | Create a docker network |
|          `docker network ls`           | List docker network     |

## Reference

> - [Github](https://github.com/apache/kafka/)
> - [Kafka Website](https://kafka.apache.org)
> - [Zookeeper Website](http://zookeeper.apache.org)
> - [Docker hub kafka (ches/kafka)](https://hub.docker.com/r/ches/kafka/)
> - [Docker hub zookeeper (jplock/zookeeper)](https://hub.docker.com/r/jplock/zookeeper/)
> - [Kafka documentation](https://kafka.apache.org/documentation/)
> - [Zookeeper documentation](http://zookeeper.apache.org/doc/current/index.html)
> - [Tutorial and explanation](https://www.tutorialspoint.com/apache_kafka/apache_kafka_quick_guide.htm)
