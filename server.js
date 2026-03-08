const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Routes
app.use('/api', require('./routes/api'));

app.listen(PORT, () => {
    console.log(`Salsabilah Empire OS is running on port ${PORT}`);
});

