# pushme-server
[![Build Status](https://travis-ci.org/buoto/pushme-server.svg)](https://travis-ci.org/buoto/pushme-server)
[![Code Climate](https://codeclimate.com/github/buoto/pushme-server/badges/gpa.svg)](https://codeclimate.com/github/buoto/pushme-server)

Django app wrapping Google Cloud Messaging service which provides api allowing you to send push messages to connected devices in one HTTP request. Simplicity of that design can be illustrated by [this almost-one-liner script](./misc/send.sh):

    #!/usr/bin/env bash
    API_URL=${API_URL:='api.pushme.neutrino.re'}
    curl $API_URL/send -d apikey=$API_KEY\&content=$1
    echo ''
To send this push message only two things were required: API_KEY obtained from api (`/gen_key`) and actual message content. Then you can use it, for example to notify yourself that your production server has crashed or that somebody pinged you on weechat.


## About
This app was created during AGHacks2015 Hackathon, as a part of push.me project
([devpost.com/software/push-me](http://devpost.com/software/push-me)).
To be usable it requires mobile app to obtain phone id and handle push messages. Lastest build of app is available here: [LINK](http://przembot.neutrino.re/share/pushapp-minapi9.apk)

Project also contained website which helps you to manage your api keys and devices in browser. See: [pushme.neutrino.re](http://pushme.neutrino.re/)

## API doc
Comming soon.

## Installation and running
1. In virtualenv, install pip requirements located in `./requirements.txt`.
2. Edit `./pushme/settings.py` and add necessary keys marked by `FILLME` comments.
3. Create postgres database set in settings.py (default pushme).
4. Run server with `manage.py` (`./manage.py runserver`).
