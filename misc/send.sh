#!/usr/bin/env bash
API_URL=${API_URL:='api.pushme.neutrino.re'}
curl $API_URL/send -d apikey=$API_KEY\&content=$1
echo ''
