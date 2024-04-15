const xhr = new XMLHttpRequest();

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#area').addEventListener('change', function () {
        xhr.open("POST", "/items");
        xhr.responseType = "document"
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
        xhr.onload = () => {
            console.log(xhr.responseXML.title);
          };
        xhr.send("area=" + this.value)
    })
})