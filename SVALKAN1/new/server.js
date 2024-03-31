const express = require("express");
const path = require('path');
const app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'Template'));

localhost = "localhost"
port = 3000
app.get("/", function (req, res) {
    //const s = fs.readFileSync("\\info.json")
    res.render('index')
});
app.listen(3000, function () {
    console.log("Server is running on http://localhost:3000");
});