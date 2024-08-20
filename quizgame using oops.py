question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
class quiz_game:
    score=0
    def __init__(self,game_questions,user_choice):
        self.game_questions=game_questions
        self.user_choice=user_choice
    def questions(self):
        for i in self.game_questions:
            answer=i['text']
            print(answer)
    def answer_validation(self):
        for question in self.game_questions: 
            user_answer = input("Enter your answer (True/False): ").capitalize()
            if user_answer == question['answer']:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

        print("Your score:", self.score)

               
total=quiz_game(question_data,["True", "False", "True", "True", "True", "False", "True", "False", "True", "True", "False", "True"])
total.questions()
total.answer_validation()
                
            