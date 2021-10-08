from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class HealthForm(FormAction):

    def name(self):
        return "detail_form"

    @staticmethod
    def required_slots(tracker):
        return ["name","contact","email","dept","institute"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [
                self.from_text(lookup="names"),
            ],
            "contact": [
                self.from_entity(entity="contact"),
            ],
            "email": [
                self.from_entity(entity="email"),
            ],
            "dept": [

                self.from_text(intent="inform",value=),
                self.from_intent(intent="deny", value="None"),
            ],
            "institute": [
                self.from_text(lookup="names")
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks, great job!")
        return []

