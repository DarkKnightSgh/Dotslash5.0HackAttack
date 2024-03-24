const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 5000;

app.get('/api/caption', (req, res) => {
  const filePath = path.join(__dirname, 'backend', 'caption.txt');
  
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      res.status(500).json({ error: 'Internal Server Error' });
      return;
    }
    
    res.send(data);
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
