import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5
  }
];

function getItemById(id) {
  return listProducts.filter((item) => item.itemId === id)[0];
}

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

const app = express();
const port = 1245;
const messageError = { status: 'Product not found' };

app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});

app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', function(req, res) {
    const id = Number(req.params.itemId);
    const value = getItemById(id)[0];

  if (!value) {
    res.send(JSON.stringify(messageError));
  }
  res.send(JSON.stringify(value));
})

app.get('/reserve_product/:itemId', async function(req, res) {
  const id = Number(req.params.itemId);
  const value = getItemById(id)[0];

  if (!value) {
    res.send(JSON.stringify(messageError));
  }

  const initial = value.initialAvailableQuantity;
  const current = await getCurrentReservedStockById(id);

  if (Number(initial) <= Number(current)) {
    res.send({ "status": "Not enough stock available", "itemId": id });
  }

  reserveStockById(id, 1);

  res.send(JSON.stringify({ "status": "Reservation confirmed", "itemId": id }));
});
