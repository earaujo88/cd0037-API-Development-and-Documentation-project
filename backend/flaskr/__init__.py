from operator import and_
import os
from tracemalloc import start
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random


from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    def query_categories():
        categories = Category.query.all()
        categories_formatted = [category.format() for category in categories]
        return categories_formatted
    
    def query_question_by_term(searchTerm):
        search = "%{}%".format(searchTerm)        
        questions = Question.query.filter(Question.question.like(search)).all()        
        question_formatted = [question.format() for question in questions]
        return question_formatted
    
    def query_questions_by_category(category_id):
        questions = Question.query.filter(Question.category == category_id).all()
        questions_formatted = [question.format() for question in questions]
        return questions_formatted

    def query_quiz(previousQuestions, category_id):
        print(category_id)
        print(previousQuestions)
        if(category_id is None):
            question = Question.query.filter(Question.id.notin_(previousQuestions)).first()
        else:
            question = Question.query.filter(and_(Question.id.notin_(previousQuestions), Question.category == category_id)).first()
        
        questions_formatted = question.format()
        return questions_formatted


    @app.route('/api/v1/categories')
    def get_categories():
        categories = query_categories()
        return jsonify({
            "categories": categories,
            "success": True
        })


    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/api/v1/questions')
    def get_questions():
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        questions = Question.query.all()
        
        if questions is None:
            abort(404)

        questions_formatted = [question.format() for question in questions]
        
        
        return jsonify({
            "questions": questions_formatted[start:end],
            "totalQuestions": len(questions_formatted),
            "categories": query_categories(),
            "success": True
        })

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    @app.route('/api/v1/questions/<int:question_id>', methods=["DELETE"])
    def delete_question(question_id):
        question = Question.query.filter(Question.id == question_id).one_or_none()
        if question is None:
            abort(404)

        question.delete()
        selection = Question.query.order_by(Question.id).all()        

        return jsonify(
            {
                "success": True,
                "deleted": question_id,                
                "total_questions": len(Question.query.all()),
            }
        )

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route('/api/v1/questions', methods=["POST"])
    def add_question():


        try:
            body = request.get_json()
            new_question = body.get("question", None)
            new_answer = body.get("answer", None)
            new_category = body.get("category", None)
            new_difficulty = body.get("difficulty", None)

            question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
            question.insert()        

            return jsonify(
                {
                    "success": True,
                    "created": question.id,                
                    "total_questions": len(Question.query.all())
                    
                }
            )
        except:
            abort(402)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/api/v1/questions/search', methods=["POST"])
    def get_questions_by_term():

        try:
            body = request.get_json()
            searchTerm = body.get("searchTerm", None)
            questions = query_question_by_term(searchTerm)

            return jsonify(
                {
                    "success": True,
                    "questions": questions,                
                    "total_questions": len(questions)
                    
                }
            )
        except:
            abort(402)


    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/api/v1/categories/<int:category_id>/questions', methods=["GET"])
    def get_questions_by_category(category_id):
        questions = query_questions_by_category(category_id)

        if questions is None:
            abort(404)
        
        return jsonify(
            {
                "success": True,
                "questions": questions,                
                "total_questions": len(questions)
                
            }
        )


    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/api/v1/quizzes', methods=["POST"])
    def get_quiz():

        try:
            body = request.get_json()
            previousQuestion = body.get("previous_questions", None)
            category = body.get("quiz_category", None)

            questions = query_quiz(previousQuestion, category)
            return jsonify(
                {
                    "success": True,
                    "question": questions,                
                    "total_questions": len(questions)
                    
                }
            )
        except:
            abort(402)



    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(405)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 405, "message": "method not allowed"}),
            405,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

  
    

    return app