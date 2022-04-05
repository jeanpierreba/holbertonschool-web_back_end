export default function cleanSet(set, startString) {
  if (!startString) {
    return '';
  }
  return [...set]
    .filter((element) => element.startswith(startString))
    .map((element) => element.slice(startString.length))
    .join('-');
}
