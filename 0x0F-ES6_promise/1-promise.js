export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (succes) resolve({ status: 200, body: 'Success' });
    reject(Error('The fake API is not working currently'));
  });
}
