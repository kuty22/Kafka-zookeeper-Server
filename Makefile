DC=docker-compose
BUILD=build
DOWN=down
UP=up -d
TEST_FILE=-f docker-compose-test.yml
service=

# stop build and start
all: down_build_up

### basic make ###
down_build_up: down build up

buid_up: build up

build:
	$(DC) $(BUILD)

up:
	$(DC) $(UP)

down:
	$(DC) $(DOWN)

### test make ###

test: down_build_up_test

down_build_up_test:  down_test build_test up_test

buid_up_test: build_test up_test

build_test:
	$(DC) $(TEST_FILE) $(BUILD)

down_test:
	$(DC) $(TEST_FILE) $(DOWN)

up_test:
	$(DC) $(TEST_FILE) $(UP)

### utils ###
ps:
	$(DC) ps

logs:
	$(DC) logs $(service)

### install ###
install:
	git submodule init
	git submodule update
