export default function getStudentIdsSum(studentsList) {
  return studentsList.reduce((acumulator, student) => acumulator + student.id, 0)
}
