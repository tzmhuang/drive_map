const dropArea = document.querySelector(".drop_box"),
  button = dropArea.querySelector("button"),
  dragText = dropArea.querySelector("header"),
  input = dropArea.querySelector("input");

let file;
var filename;

button.onclick = () => {
  input.click();
};

// input.addEventListener("change", function (e) {
//   var fileName = e.target.files[0].name;
//   let filedata = `
//     <form action="/home/zanming/Projects/BevMap/map_webapp/test_uploads/test.ext" method="post" enctype="multipart/form-data">
//     <div class="form">
//     <h4>${fileName}</h4>
//     <button class="btn">Upload</button>
//     </div>
//     </form>`;
//   dropArea.innerHTML = filedata;
// });
const handleImageUpload = event => {
  const files = event.target.files
  const formData = new FormData()
  formData.append('myFile', files[0])

  fetch('/saveImage', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.path)
  })
  .catch(error => {
    console.error(error)
  })
}

input.addEventListener('change', event => {
  handleImageUpload(event)
})