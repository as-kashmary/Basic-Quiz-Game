class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0;
        self.question_list=q_list;
        self.count=0;

    def still_has_questions(self):
        if len(self.question_list)> self.question_number :
            return True;
        else:
            return False;

    def next_question(self):
        current_question=self.question_list[self.question_number];
        self.question_number+=1;
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        check=self.check_answer(user_answer,current_question.answer);
        if check:
            self.count+=1;

    def check_answer(self,ua,cq):
        if ua.lower()==cq.lower() :
            print("you got it right");
            return True;
        else:
            print("you failed, better luck next time");
            return  False;


