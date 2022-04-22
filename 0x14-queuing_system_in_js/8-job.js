function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }
  jobs.forEach(function (jobObj) {
    const job = queue.createJob('push_notification_code_3', jobObj).save();
    try {
      job.on('enqueue', () => {
        console.log(`Notification job created: ${job.id}`);
      }).on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      }).on('failed', (error) => {
        console.log(`Notification job ${job.id} failed: ${error}`);
      }).on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    } catch (err) {}
  });
}

module.exports = createPushNotificationsJobs;
