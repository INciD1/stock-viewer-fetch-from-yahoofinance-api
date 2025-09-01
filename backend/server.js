const express = require('express');
const { exec } = require('child_process');
const cors = require('cors');
const path = require('path');
const NodeCache = require('node-cache');

const app = express();
const PORT = 3000;
const cache = new NodeCache({ stdTTL: 600 }); // แคช 10 นาที
const PYTHON_PATH = 'C:\\Users\\LEGION\\AppData\\Local\\Programs\\Python\\Python310\\python.exe';

app.use(cors());
app.use(express.static(path.join(__dirname, '../frontend')));

app.get('/api/stock/:symbol', async (req, res) => {
  const symbol = req.params.symbol;
  const cacheKey = `stock_${symbol}`;
  const cachedData = cache.get(cacheKey);

  if (cachedData) {
    console.log(`✅ Serving cached data for ${symbol}`);
    return res.json(cachedData);
  }

  const command = `"${PYTHON_PATH}" "${path.join(__dirname, 'fetch_stock.py')}" ${symbol}`;

  try {
    const { stdout, stderr } = await new Promise((resolve, reject) => {
      exec(command, { shell: 'cmd.exe' }, (error, stdout, stderr) => {
        if (error) {
          reject(error);
          return;
        }
        resolve({ stdout, stderr });
      });
    });

    if (stderr) {
      console.error('❌ Python stderr:', stderr);
      throw new Error(`Python script error: ${stderr}`);
    }

    const data = JSON.parse(stdout);
    if (data.error) {
      throw new Error(data.error);
    }

    cache.set(cacheKey, data);
    res.json(data);
  } catch (error) {
    console.error('❌ Error:', {
      message: error.message,
      stderr: error.stderr || 'No stderr',
    });
    res.status(500).json({
      error: `Failed to fetch data from Yahoo Finance: ${error.message}`,
      details: error.stderr || 'No additional details',
    });
  }
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/index.html'));
});

app.listen(PORT, () => {
  console.log(`✅ Server running at http://localhost:${PORT}`);
});