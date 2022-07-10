# API Development and Documentation Final Project

## Trivia App

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the project repository and [clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The [backend](./backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

> View the [Backend README](./backend/README.md) for more details.

### Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads?

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API.

> View the [Frontend README](./frontend/README.md) for more details.

## API Reference
### Getting Started

- Base URL: This app can olny run locally and is not hosted as a base URL. The default backend is http://127.0.01:5000
- Authentication: This version of the api does not require any kind of authentication

### Error Handling

Erros are returned as JSON objects in the following format:


```json
{
  "success": False,
  "error": 404,
  "message": "resource not found"
}
```
The API wil return four type when a particular request fails:
- 400: bad request
- 404: Resource not found
- 405: method not allowed
- 422: unprocessable

### Endpoints
#### GET /api/v1/questions
- General:
    - Returns a list of questions objects, success value, and total number of questions
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1. 
- Sample: `curl http://127.0.0.1:5000/api/v1/questions`
```
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "questions": [
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true, 
  "totalQuestions": 22
}
```

#### POST /api/v1/questions/questions
- General:
    - Creates a new question using the submitted question, answer, category and difficult. Returns the id of the created question, success value, total question on the database. 
- `curl http://127.0.0.1:5000/api/v1/questions -X POST -H "Content-Type: application/json" -d '{"question":"The Taj Mahal is located in which Indian city?", "answer":"Agra", "category":"3", "difficult":"2"}'`

```
{
  "created": 28, 
  "success": true, 
  "total_questions": 22
}
```

#### DELETE /api/v1/questions/{question_id}
- General:
    - Deletes the questions of the given ID if it exists. Returns the id of the deleted questions, success value, total questions remaining on database. 
- `curl -X DELETE http://127.0.0.1:5000/api/v1/questions/27`

```
{
  "deleted": 27, 
  "success": true, 
  "total_questions": 21
}
```


#### POST /api/v1/questions/search
- General:
    - Returns a list of questions objects, success value, and total number of questions based on a submitted search term related to the question text    
- Sample: `curl http://127.0.0.1:5000/api/v1/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm":"Taj"}'`

```
{
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }    
  ], 
  "success": true, 
  "total_questions": 2
}
```

#### GET /api/v1/categories/{category_id}/questions
- General:
    - Returns a list of questions objects, success value, and total number of questions based on a specific category id.    
- Sample: `curl http://127.0.0.1:5000/api/v1/categories/3/questions`
```
{
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }    
  ], 
  "success": true, 
  "total_questions": 4
}
```

#### GET /categories
- General:
    - Returns a list of categories objects and success value    
- Sample: `curl http://127.0.0.1:5000/api/v1/categories`
```
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ]
}
```

#### POST /api/v1/quizzes
- General:
    - Returns a list of questions objects, success value, and total number of questions based on a submitted search term related to the question text    
- Sample: `curl http://127.0.0.1:5000/api/v1/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[1,2,3], "quiz_category": "3"}'`

```
{
  "questions": {
    "answer": "Lake Victoria", 
    "category": 3, 
    "difficulty": 2, 
    "id": 13, 
    "question": "What is the largest lake in Africa?"
  }, 
  "success": true, 
  "total_questions": 5
}
```