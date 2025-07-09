from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    tiles = [
        {"title": "Area Calculation Box", "description": "Calculate areas of different shapes", "route": "area_calculation"},
        {"title": "Lessons", "description": "Access math lessons", "route": "lessons"},
        {"title": "Mathematical Concepts", "description": "Mathematical concepts for area calculation.", "route": "mathematical_concepts"},
        {"title": "Assessments", "description": "Take math assessments", "route": "assessments"},
        {"title": "Feedbacks", "description": "View feedbacks for completed assessments.", "route": "feedbacks"},
        {"title": "Student Profile", "description": "Manage your student profile", "route": "student_profile"},
    ]
    return render_template('index.html', tiles=tiles)

@app.route('/<page>')
def render_page(page):
    return render_template(f'{page}.html', title=page.replace('_', ' ').title())

@app.route('/two_d_shapes')
def two_d_shapes():
    return render_template('two_d_shapes.html')

@app.route('/lessons')
def lessons():
    lessons_data = [
        {"name": "Introduction to Geometry", "objectives": "Learn basic geometric concepts like points, lines, and angles.", "difficulty": "Beginner"},
        {"name": "Calculating Area of Triangles", "objectives": "Understand how to calculate the area of different types of triangles.", "difficulty": "Intermediate"},
        {"name": "Understanding Quadrilaterals", "objectives": "Learn about squares, rectangles, and other quadrilaterals.", "difficulty": "Expert"},
        {"name": "Circles and Their Properties", "objectives": "Explore the properties of circles and calculate their area.", "difficulty": "Advanced"},
        {"name": "Introduction to 3D Shapes", "objectives": "Learn about cubes, spheres, and other 3D shapes.", "difficulty": "Beginner"},
    ]
    return render_template('lessons.html', lessons=lessons_data)

@app.route('/mathematical_concepts')
def mathematical_concepts():
    concepts = {
        "Arithmetic": ["Addition", "Multiplication"],
        "Algebra": ["Variables", "Equations"],
        "Geometry": ["Angle", "Length", "Perimeter", "Area", "Volume"]
    }
    return render_template('mathematical_concepts.html', concepts=concepts)

@app.route('/assessments')
def assessments():
    assessments_data = [
        {
            "name": "Basic Geometry Quiz",
            "learning_objects": ["Angles", "Triangles", "Quadrilaterals"]
        },
        {
            "name": "Area Calculation Test",
            "learning_objects": ["Circle Area", "Triangle Area", "Rectangle Area"]
        },
        {
            "name": "Algebra Fundamentals",
            "learning_objects": ["Variables", "Linear Equations", "Algebraic Expressions"]
        },
        {
            "name": "3D Shapes Assessment",
            "learning_objects": ["Cubes", "Spheres", "Cylinders"]
        },
        {
            "name": "Arithmetic Operations",
            "learning_objects": ["Addition", "Multiplication", "Division"]
        }
    ]
    return render_template('assessments.html', assessments=assessments_data)

@app.route('/feedbacks')
def feedbacks():
    feedback_data = [
        {
            "assessment_name": "Basic Geometry Quiz",
            "error_type": "ConceptualError",
            "feedback_type": "ElaborativeFeedback",
            "feedback": "Review the properties of triangles. Remember, the sum of interior angles is always 180 degrees."
        },
        {
            "assessment_name": "Area Calculation Test",
            "error_type": "CalculationError",
            "feedback_type": "CorrectiveFeedback",
            "feedback": "Check your multiplication steps when calculating the area of a rectangle. Remember: Area = length * width."
        },
        {
            "assessment_name": "Algebra Fundamentals",
            "error_type": "FormulaApplicationError",
            "feedback_type": "CorrectiveFeedback",
            "feedback": "When solving for x, make sure to apply the same operation to both sides of the equation."
        },
        {
            "assessment_name": "3D Shapes Assessment",
            "error_type": "ConceptualError",
            "feedback_type": "ElaborativeFeedback",
            "feedback": "Consider the difference between surface area and volume. Surface area is 2D, while volume is 3D."
        },
        {
            "assessment_name": "Arithmetic Operations",
            "error_type": "CalculationError",
            "feedback_type": "MotivationalFeedback",
            "feedback": "Great effort! Double-check your division steps. You're very close to the correct answer."
        }
    ]
    return render_template('feedbacks.html', feedbacks=feedback_data)

import random

@app.route('/student_profile')
def student_profile():
    student_data = {
        "name": "John Doe",
        "student_id": "STU12345",
        "level": "Intermediate",
        "learning_styles": random.sample(["Auditory", "Kinesthetic", "Reading/Writing", "Visual"], 2),
        "completed_learning_objects": [
            "Introduction to Geometry",
            "Basic Algebra Concepts",
            "Area Calculation for Rectangles",
            "Understanding Fractions",
            "Introduction to Trigonometry"
        ]
    }
    return render_template('student_profile.html', student=student_data)

    
if __name__ == '__main__':
    app.run(debug=True)
