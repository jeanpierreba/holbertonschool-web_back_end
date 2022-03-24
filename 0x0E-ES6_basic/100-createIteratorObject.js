export default function createIteratorObject(report) {
  let iterator = [];
  for (const value of Object.values(report.allEmployees)) {
    iterator = [...iterator, ...value];
  }

  return iterator;
}
