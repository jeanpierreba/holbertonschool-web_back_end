import kue from 'kue';

const queue = kue.createQueue();
const data = {
  phoneNumber: '2025550156',
  message: 'This is the code to verify your account'
};

const job = queue.create('push_notification_code', data).save();

job.on('enqueue', () => {
	console.log(`Notification job created: ${job.id}`);
}).on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
})
