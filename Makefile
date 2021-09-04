CURR_BRANCH := $(shell git symbolic-ref --short HEAD)
UNAME := $(shell uname -s)

ifeq ($(UNAME),Linux)
	OPEN_CMD := sensible-browser
endif
ifeq ($(UNAME),Darwin)
	OPEN_CMD := open
endif

deploy:
	@echo Pushing branch \"$(CURR_BRANCH)\" to Heroku...
	git push heroku $(CURR_BRANCH):main
	@echo Done.
	heroku open

up:
	docker-compose up -d
	$(OPEN_CMD) http://localhost:8000
	docker-compose logs -tf

log:
	heroku logs -t

kill:
	docker-compose down

restart:
	docker-compose restart
