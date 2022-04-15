function initMap() {
  const myLatLng = { lat: Number(document.getElementById("lat").value), lng: Number(document.getElementById("lng").value) };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: myLatLng,
  });

  new google.maps.Marker({
    position: myLatLng,
    map,
    title: "Hello World!",
  });
}

window.initMap = initMap;