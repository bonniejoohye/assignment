//지도 만들기
var mapContainer = document.getElementById("map"), // 지도를 표시할 div
  mapOption = {
    center: new kakao.maps.LatLng(33.451475, 126.570528), // 지도의 중심좌표
    level: 3, // 지도의 확대 레벨
  };

// 지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption);

// 장소 검색 객체를 생성합니다
var ps = new kakao.maps.services.Places();

// 키워드로 장소를 검색합니다
let save = "";

const inputValue = () => {
  const input = document.getElementById("input");
  save = input.value;
  ps.keywordSearch(save, placesSearchCB);
};

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB(data, status, pagination) {
  if (status === kakao.maps.services.Status.OK) {
    input.value = "";
    // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
    // LatLngBounds 객체에 좌표를 추가합니다
    var bounds = new kakao.maps.LatLngBounds();

    for (var i = 0; i < data.length; i++) {
      displayMarker(data[i]);
      bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
    }

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
    map.setBounds(bounds);
  }

  // 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
  var infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

  //마커 보여주기
  function displayMarker(place) {
    var marker = new kakao.maps.Marker({
      map: map,
      position: new kakao.maps.LatLng(place.y, place.x),
    });

    // 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, "click", function () {
      // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
      let place_id = place.id;

      infowindow.setContent(
        '<div style="padding:5px;font-size:12px;">' +
          place.place_name +
          "<br>" +
          place.address_name +
          "<br>" +
          place.phone +
          "<br>" +
          `<a href="https://map.kakao.com/link/to/${place_id}" style="color:blue" target="_blank">상세보기</a>` +
          ' <button onclick="infowindow.setMap(null); ">닫기</button>' +
          "</div>"
      );
      infowindow.open(map, marker);
    });
  }
}
