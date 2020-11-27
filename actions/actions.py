# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guCompanye on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType
import smtplib
import pandas as pd
#
df = pd.read_csv("D:\GoBaskt-Intern\GC bot V5\GC_Database.csv")

class SendGiftCard(Action):

     def name(self) -> Text:
         return "send_gift_card"

     def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            site = tracker.get_slot("site"),
            to_mail = tracker.get_slot("email")
            amount = tracker.get_slot("amount")
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls() 
            s.login("sendergiftcard@gmail.com", "gift@123")
            message = "Your gift card code for {} of Rs. {} is ZZXC-1234_POIU".format(site,amount)
            s.sendmail("sendergiftcard@gmail.com", to_mail, message)
            s.quit()
class AskForSite(Action):
    def name(self) -> Text:
        return "action_ask_site"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        available_companies = df.Company.unique()
        
        
        dispatcher.utter_message(text='Please select from the following companies:{}'.format(available_companies))
        return []
        
class AskForAmount(Action):
    def name(self) -> Text:
        return "action_ask_amount"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        site = tracker.get_slot("site")
        avl_cards = df[df['Company'] == site].Amount.unique() #Getting unique values of the card
        avl_cards.sort()
       

        dispatcher.utter_message(text='We have the following cards available{}'.format(avl_cards))
        return []
