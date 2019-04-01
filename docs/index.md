# DjangoCon EU Geotracker

This is skeleton project for DjangoCon EU 2019 Geotracker.

## Installation

Clone <https://github.com/jtiai/dceu-geotracker> repository.

Provided `docker-compose.yml` and `Dockerfile` will install
everything needed.

You can alternatively install PostGIS natively. It should install required libraries.

Since `geolocation` requires HTTPS access you need to route your localhost
somewhere. Checkout serveo.net <https://serveo.net> or ngrok <https://ngrok.com> that
does it pretty easily.

You can also deploy to your own server/site but that's not covered here.

## Setup

Run migrations:
```
docker-compose run --rm web pipenv python manage.py migrate
```

Create superuser:
```
docker-compose run --rm web pipenv python manage.py createsuperuser
```

Start service:
```
docker-compose up
```

On a second window start serveo or ngrok and route `localhost:8000`
port to https-address.

Verify that you can connect from your mobile device to that address. 

If everything works as expected you should see a map with "locate" button.

Note that mobile device may ask permission to share geolocation with your app.
To make app work you need to accept it. Also it's advised that you
turn on GPS before launching your app in browser.

## Problems?

Create ticket in issue tracker.