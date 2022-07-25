import csv

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

    def debugTriviaList(self):
        for item in self.trivia_list:
            print(item)
