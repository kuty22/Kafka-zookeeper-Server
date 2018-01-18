# Kafka-zookeeper-Server


### summary:
  - [Introduction](#introduction)
  - [Install](#install)
  - [Start](#start)
  - [Documentation](#documentation)
  - [Reference](#reference)



## Introduction

  This is an example of kafka and zookeeper with docker.
  It use an external docker network to simplify the plugging of a module.

  The basic configuration haven't any topic.

  > for more information about kafka or zookeeper:
  > - [Github](https://github.com/apache/kafka/)
  > - [Kafka Website](https://kafka.apache.org)
  > - [Zookeeper Website](http://zookeeper.apache.org)


## Install

### requirement:
- Docker
- docker-compose
- git

### Two ways are available to install:
- Makefile
- basic install

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
```

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
```

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


## Reference

> - [Github](https://github.com/apache/kafka/)
> - [Kafka Website](https://kafka.apache.org)
> - [Zookeeper Website](http://zookeeper.apache.org)
> - [Docker hub kafka (ches/kafka)](https://hub.docker.com/r/ches/kafka/)
> - [Docker hub zookeeper (jplock/zookeeper)](https://hub.docker.com/r/jplock/zookeeper/)
> - [Kafka documentation](https://kafka.apache.org/documentation/)
> - [Zookeeper documentation](http://zookeeper.apache.org/doc/current/index.html)
> - [Tutorial and explanation](https://www.tutorialspoint.com/apache_kafka/apache_kafka_quick_guide.htm)
