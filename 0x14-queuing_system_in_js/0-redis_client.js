import redis from 'redis';

redis.createClient().on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error}`);
});

redis.createClient().on('connect', function() {
  console.log('Redis client connected to the server');
});
