const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static('public'));

app.post('/api/click', (req, res) => {
    console.log('Đã nhận được tín hiệu nhấn nút từ client qua Raspberry Pi!');
    const { time } = req.body;
    console.log(`Thời gian bấm: ${time}`);

    res.json({ 
        status: 'success', 
        message: 'Raspberry Pi đã nhận được cú click thành công!' 
    });
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server đang chạy trên Raspberry Pi tại: http://localhost:${PORT}`);
});
