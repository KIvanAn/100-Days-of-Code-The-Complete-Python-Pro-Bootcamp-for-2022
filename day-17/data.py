import requests


question_data = None

# Test data
test_data = [
    {"question": "A slug's blood is green.", "answer": "True"},
    {"question": "The loudest animal is the African Elephant.", "answer": "False"},
    {"question": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"question": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "question": "In West Virginia, USA, if you accidentally hit an animal with your car, "
                    "you are free to take it home to eat.",
        "answer": "True"},
    {"question": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"question": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"question": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"question": "Google was originally called 'Backrub'.", "answer": "True"},
    {"question": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"question": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"question": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

try:
    # All quizes generate random here: https://opentdb.com/api_config.php
    questions = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean").json()
    question_data = [{"question": item["question"], "answer": item["correct_answer"]} for item in questions["results"]]
except Exception as ex:
    question_data = test_data
    print("You are use test data because you get error: ", ex)
