import csv
import random

NUMBER_OF_ROUNDS = 5

class TriviaManager:
    trivia_list = ["Hello"]

    def __init__(self, filename):
        with open(filename, newline='') as csvfile:
            trivia_reader = csv.DictReader(csvfile)

            question = ""
            answer = []
            for row in trivia_reader:
                if row["question"] != question:
                    # Create trvia question and place into Trivias array....
                    self.trivia_list.append(row["question"])
                    question = row["question"]
                    answer = []
                
                # Temporary until Trivia class is made
                answer.append({row["answer"]: eval(row["correct?"])})

    def getTriviaSet(self):
        random.shuffle(self.trivia_list)
        return self.trivia_list[:NUMBER_OF_ROUNDS + 1]

    def debugTriviaList(self):
        for item in self.trivia_list:
            print(item)
