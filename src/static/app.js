function getKey() {
  const body = {
    action: 'get_key'
  }
  const requestParams = {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  }
  const url = '/cryptography'
  fetch(url, requestParams)
    .then(function (response) {
      return response.json();
    })
    .then(function (myJson) {
      $("#key").val(myJson.data)
    });
}

function cryptography(action) {
  const key = $("#key").val()
  const inputData = $("#data").val()
  const body = {
    action: action,
    key: key,
    data: inputData
  }
  const url = '/cryptography'
  const requestParams = {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  }

  fetch(url, requestParams)
    .then(function (response) {
      return response.json();
    })
    .then(function (myJson) {
      $("#data").val(myJson.data)
    });
}
