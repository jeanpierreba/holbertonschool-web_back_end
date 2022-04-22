import redis from 'redis';

const client = redis.createClient();

const schoolsList = [
  'Portland=50',
  'Seattle=80',
  'New York=20',
  'Bogota=20',
  'Cali=40',
  'Paris=2'
]

schoolsList.forEach((x) => {
  const separateStrings = x.split('=');
  client.hset('HolbertonSchools', separateStrings[0], separateStrings[1], redis.print);
})

client.hgetall('HolbertonSchools', function(error, res) {
	if (error) {
		console.log('WRONG', error);
	} else {
		console.log(res)
	}
})
