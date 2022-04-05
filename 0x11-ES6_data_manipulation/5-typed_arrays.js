export default function createInt8TypedArray(length, position, value) {
  const newBuffer = new ArrayBuffer(length);
  const newDataview = new DataView(newBuffer);
  if (position > length) {
    throw Error('Position outside range');
  }
  newDataview.setInt8(position, value);
  return newDataview;
}
