import abc


class Interviewer(abc.ABC):
    @abc.abstractmethod
    def ask_questions(self):
        pass


class Developer(Interviewer):
    def ask_questions(self):
        print('Developer: asking about design patterns')


class CommunityExecutive(Interviewer):
    def ask_questions(self):
        print('Community Executive: asking about community building')


class HiringManager(abc.ABC):
    @abc.abstractmethod
    def make_interviewer(self) -> Interviewer:
        pass

    def take_interview(self):
        interviewer = self.make_interviewer()
        interviewer.ask_questions()


class DevelopmentManager(HiringManager):
    def make_interviewer(self):
        return Developer()


class MarketingManager(HiringManager):
    def make_interviewer(self):
        return CommunityExecutive()


if __name__ == '__main__':
    devManager = DevelopmentManager()
    devManager.take_interview()

    marketingManager = MarketingManager()
    marketingManager.take_interview()
