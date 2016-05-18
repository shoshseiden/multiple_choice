from models import Question


def calculate_total_points(self):
    total_points = 0

    point_value = Question.question_point_value
    total_points += point_value

    return self.total_points

def student_score(self):
    student_score = 0
    total_score = 0

    total_score += student_score

    return self.total_score

def calculate_percentage(self):
    percentage = 0
    percentage = 100 * (total_score / total_points)

    return self.percentage
