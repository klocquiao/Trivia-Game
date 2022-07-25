import csv

class TriviaManager:
    Trivias = []

    def __init__(self, filename):
        with open('filename', newline='') as csvfile:
            trivia_reader = csv.reader(csvfile)

            question = ""
            answer = []
            for row in trivia_reader:
                if row["question"] != question:
                    # Create trvia question and place into Trivias array....
                    question = row["question"]
                    answer = []
                
                # Temporary until Trivia class is made
                answer.append({row["answer"]: eval(row["correct?"])})

