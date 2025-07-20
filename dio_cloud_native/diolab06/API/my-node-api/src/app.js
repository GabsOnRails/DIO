const express = require('express');
const addressRoutes = require('./routes/address');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use('/address', addressRoutes); // altered to /address

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});