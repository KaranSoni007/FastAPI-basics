from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {
    "S01": {"name": "Karan", "marks": 85, "grade": "A+"},
    "S02": {"name": "Om", "marks": 67, "grade": "B"},
    "S03": {"name": "Jay", "marks": 76, "grade": "A"},
}


# Input Schema
class MarksSubmission(BaseModel):
    student_id: str
    marks: int
    subject: str


@app.get("/student/{student_id}")
def get_student(student_id: str):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail=f"Student having ID {student_id} does not exist",
        )

    return students[student_id]


@app.post("/submit-marks")
def submit_marks(submission: MarksSubmission):

    # Error 1: Student does not exist

    if submission.student_id not in students:
        raise HTTPException(
            status_code=404,
            detail=f"Student with ID {submission.student_id} does not exist",
        )

    # Error 2: Valid range 0-100

    if submission.marks < 0 or submission.marks > 100:
        raise HTTPException(
            status_code=400,
            detail={
                "error": f"Marks for student ID {submission.student_id} are not valid",
                "marks_received": submission.marks,
                "fix": "Enter valid marks between 0 and 100",
            },
        )

    # Error 3: Subject name is empty

    if submission.subject.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Subject name cannot be empty",
        )

    # Update marks

    students[submission.student_id]["marks"] = submission.marks

    return {
        "message": "Marks submitted successfully",
        "student": students[submission.student_id]["name"],
        "subject": submission.subject,
        "marks": submission.marks,
    }
