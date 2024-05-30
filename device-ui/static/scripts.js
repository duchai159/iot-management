function dv(deviceId, turnOn){
    var icon = document.querySelector(`.device-${deviceId} .icon`);
    var status = document.querySelector(`.device-${deviceId} .status`);
    var card = document.querySelector(`.device-${deviceId} .card`);

    if (turnOn) {
        status.textContent = 'ON';
        icon.classList.add('on');
        card.classList.add('on');
    } else {
        status.textContent = 'OFF';
        icon.classList.remove('on');
        card.classList.remove('on');
    }
}

function fetchStatus(){
    fetch("/status")
        .then((response) => response.json())
        .then((data) => {
          if (data!==null){
            for (let key in data) {
                let item = data[key];
                dv(item.deviceId, item.turnOn)
            }
          }
        });
}

setInterval(fetchStatus, 1000)