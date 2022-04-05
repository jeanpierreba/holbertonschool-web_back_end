export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  return studentsList
    .filter((student) => student.city === city)
    .map((student) => {
      const grade = newGrades
        .filter((item) => item.studentId === student.id)
        .map((grad) => grad.grade)[0];
      const gradeItem = grade || 'N/A';
      return { ...student, gradeItem };	
    });
}
