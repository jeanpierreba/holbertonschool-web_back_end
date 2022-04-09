const fs = require('fs');

function countStudents(path) {
  let filesystem;
  try {
    filesystem = fs.readFileSync(path, 'utf-8').trim().split('\n');
  } catch (e) {
    throw new Error('Cannot load the database');
  }
  let counter = 0;
  const tmp = f.slice(1).reduce((pat, c) => {
    counter += 1;
    const fields = c.split(',');
    if (!pat[fields[3]]) {
      Object.assign(pat, {
        [fields[3]]: []
      });
    }
    pat[fields[3]].push(fields[0]);
    return pat;
  }, {});
  console.log(`Number of students: ${counter}`);
  for (const key of Object.keys(tmp)) {
    console.log(`Number of students in ${key}: ${tmp[key].length}. List; ${c[key].join(', ')}`);
  }
}

module.export = countStudents;
