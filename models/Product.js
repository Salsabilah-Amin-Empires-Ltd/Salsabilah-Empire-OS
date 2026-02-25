const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
    sku: { type: String, required: true, unique: true },
    name: { type: String, required: true },
    category: { type: String, default: 'Electronics' },
    brand: { type: String },
    purchasePrice: { type: Number, required: true },
    sellingPrice: { type: Number, required: true },
    stockQuantity: { type: Number, default: 0 },
    // ইলেকট্রনিক্স ব্যবসার জন্য বিশেষ ফিল্ড
    serialNumbers: [{ type: String }], // প্রতিটি আইটেমের আলাদা IMEI/SN
    warrantyMonths: { type: Number, default: 12 },
    supplierInfo: {
        name: String,
        whatsapp: String
    },
    lastUpdated: { type: Date, default: Date.now }
}, { timestamps: true });

module.exports = mongoose.model('Product', productSchema);
