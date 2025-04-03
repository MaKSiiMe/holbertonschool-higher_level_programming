document.addEventListener("DOMContentLoaded", () => {
  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then(response => response.json())
    .then(newData => {
      document.getElementById("hello").textContent = newData.hello;
    })
    .catch(e => console.error("Error:", e));
})