from flask import Blueprint, request, jsonify

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/', methods=['GET'])
def get_quiz():
    lang = request.args.get('lang', 'python')
    quiz = {
        "lang": lang,
        "questions": [
            {"q": "What is 2+2?", "options": [2, 3, 4, 5], "answer": 4},
            {"q": "Print in Python?", "options": ["echo()", "print()", "log()", "say()"], "answer": "print()"},
            {"q": "How do you create a variable in Python?",
             "options": ["var x = 5", "let x = 5", "x = 5", "define x = 5"], "answer": "x = 5"},

            {"q": "How do you print text in Python?", "options": ["show()", "echo()", "print()", "output()"],
             "answer": "print()"},

            {"q": "What data type is the number 10?", "options": ["float", "string", "int", "bool"], "answer": "int"},

            {"q": "What symbol is used for comments in Python?", "options": ["//", "#", "<!--", "--"], "answer": "#"},

            {"q": "How do you create a list?", "options": ["list{}", "{1,2,3}", "[1,2,3]", "(1,2,3)"],
             "answer": "[1,2,3]"},

            {"q": "How do you get the length of a list?",
             "options": ["count(list)", "length(list)", "len(list)", "size(list)"], "answer": "len(list)"},

            {"q": "Which keyword is used for a loop?", "options": ["for", "repeat", "loop", "iterate"],
             "answer": "for"},

            {"q": "Which keyword is used to define a function?", "options": ["function", "func", "def", "create"],
             "answer": "def"},

            {"q": "How are strings written?",
             "options": ["In square brackets", "In curly braces", "In quotes", "In parentheses"],
             "answer": "In quotes"},

            {"q": "Which operator performs addition?", "options": ["-", "/", "+", "++"], "answer": "+"},

            {"q": "How do you convert a number to a string?",
             "options": ["str()", "toString()", "string()", "convert()"], "answer": "str()"},

            {"q": "What is the result of 3 > 2?", "options": ["3", "True", "False", "None"], "answer": "True"},

            {"q": "How do you create an empty dictionary?", "options": ["()", "[]", "{}", "<>"], "answer": "{}"},

            {"q": "How do you get the first element of a list?",
             "options": ["list[1]", "list[0]", "list.first()", "list.get(1)"], "answer": "list[0]"},

            {"q": "What type is True?", "options": ["int", "bool", "string", "float"], "answer": "bool"},

            {"q": "How do you create a tuple?", "options": ["[1,2,3]", "(1,2,3)", "{1,2,3}", "<1,2,3>"],
             "answer": "(1,2,3)"},

            {"q": "What does input() do?",
             "options": ["Prints text", "Gets user input", "Deletes a variable", "Saves a file"],
             "answer": "Gets user input"},

            {"q": "What does the == operator do?",
             "options": ["Assigns a value", "Compares values", "Creates a variable", "Returns a type"],
             "answer": "Compares values"},

            {"q": "How do you stop a program?", "options": ["stop()", "break()", "exit()", "end()"],
             "answer": "exit()"},

            {"q": "Which operator is used for multiplication?", "options": ["%", "*", "x", "**"], "answer": "*"}
        ]
    }
    return jsonify(quiz)
