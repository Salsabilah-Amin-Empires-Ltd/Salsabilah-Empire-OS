const { Pool } = require('pg'); // পোস্টগ্রেস ব্যবহার করলে
const pool = new Pool({
    user: 'YOUR_USERNAME',
    host: 'localhost',
    database: 'salsabilah_db',
    password: 'YOUR_PASSWORD',
    port: 5432,
});

module.exports = pool;
