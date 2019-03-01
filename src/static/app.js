async function API(action, key, inputData) {
  const url = '/cryptography'
  const body = {
    action: action,
    key: key,
    data: inputData
  }
  const requestParams = {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  }

  const response = await fetch(url, requestParams)
  if (response.ok) return await response.json()
  throw new Error(await response.text());
}

function getKey() {
  API('get_key').then(response => $("#key").val(response.data)).catch(alert)
}

function cryptography(action) {
  const key = $("#key").val()
  const inputData = $("#data").val()
  API(action, key, inputData).then(response => $("#data").val(response.data)).catch(alert)
}

function clearAll() {
  $("#key").val('')
  $("#data").val('')
  console.log('clear')
}
