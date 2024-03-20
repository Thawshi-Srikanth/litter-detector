const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

const formData = new FormData();
formData.append('image', fs.createReadStream('band.png'));

axios.post('http://localhost:5000/predict', formData, {
    headers: formData.getHeaders(),
})
.then((response) => {
    console.log(response.data);
})
.catch((error) => {
    console.error("Error: ", error.message);
});