let myMap = null;
let currentLocationMarker = null;

function single_locate() {
    navigator.geolocation.getCurrentPosition(function (position) {
            console.log("Moving to current location", position);
            currentLocationMarker.setLatLng([position.coords.latitude, position.coords.longitude]).addTo(myMap);
            myMap.panTo([position.coords.latitude, position.coords.longitude]);
        },
        function (positionError) {
            alert("Geolocation failure");
            console.debug(positionError.message);
        }, {timeout: 5000, enableHighAccuracy: true});
}

function index_startup() {
    if (window.location.protocol !== 'https:') {
        alert("Geolocation requires usage of HTTPS, and you're using HTTP. Trying to JS redirect...");
        window.location.protocol = "https:";
        return;
    }

    if (!navigator.geolocation) {
        alert("Your browser doesn't support geolocation.");
        return;
    }
    myMap = L.map("map");
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(myMap);
    myMap.setView([62.6050, 29.756], 13);

    violetIcon = new L.Icon({
        iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-violet.png',
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.4.0/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });

    navigator.geolocation.getCurrentPosition(function (position) {
            // First location got
            console.log("Moving to current location", position);
            currentLocationMarker = L.marker([position.coords.latitude, position.coords.longitude]).addTo(myMap);
            myMap.panTo([position.coords.latitude, position.coords.longitude]);
        },
        function (positionError) {
            alert("Geolocation failure");
            console.debug(positionError.message);
        }, {maximumAge: 5000, timeout: 5000, enableHighAccuracy: true});
}
