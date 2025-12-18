from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCourseFees(Action):
    def name(self):
        return "action_course_fees"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        user_message = tracker.latest_message.get("text", "").lower()

        # Basic course-fee mapping
        if "computer" in user_message:
            fees = "₹1,80,000 per year"
        elif "it" in user_message or "information" in user_message:
            fees = "₹1,75,000 per year"
        elif "extc" in user_message or "electronics" in user_message:
            fees = "₹1,70,000 per year"
        elif "instrumentation" in user_message:
            fees = "₹1,60,000 per year"
        else:
            fees = "Our course fees range between ₹1.6L to ₹1.8L per year depending on the branch."

        dispatcher.utter_message(text=f"The fees for that course is {fees}.")
        return []


class ActionCourseDuration(Action):
    def name(self):
        return "action_course_duration"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        dispatcher.utter_message(text="All B.E. courses at RAIT have a duration of 4 years (8 semesters).")
        return []
