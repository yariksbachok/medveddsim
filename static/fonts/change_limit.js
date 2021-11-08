let timerId = setInterval( () => {
    fetch(`${window.location.protocol}/my_number `
    )
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        console.log(data)
        for (const i of data) {
            document.getElementById(i.id).innerHTML=i.sms_kod
            console.log(i.id);
        }
      });
  }, 5000)


if (performance.navigation.type == 1) {
    document.location.href = '/activeites/'
} else {
    console.log( "Страница не перезагружена");
}
