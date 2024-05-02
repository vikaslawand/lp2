# Define a dictionary of common problems and their solutions 
problem_dict = { 
 "What if my flight is delayed?":"You may be eligible for compensation or assistance depending on the duration and reason for the delay.",
 "Can I get a refund for a canceled flight?":"Yes, you're entitled to a refund if the airline cancels your flight, although some airlines may offer alternative options.",
 "How do I rebook if I miss my connecting flight?":"Approach airline staff for assistance; they'll help you find an alternative flight.",
"Do I need to notify the airline about my medical condition before flying?":"It's advisable to inform the airline in advance to arrange any necessary accommodations or assistance.",
"What if my luggage is lost?":"Report it to the airline's baggage services, and they'll help track and deliver your luggage.",
"Can I get compensation for a flight delay?":"Depending on the circumstances, you may be entitled to compensation under passenger rights regulations.",
"What are my rights during a flight delay?":"You have rights outlined by aviation authorities, which typically include entitlements to compensation and assistance.",
 "How can I stay informed about changes to my flight?":"Download the airline's app or check their website for updates, or sign up for email or SMS notifications.",
 "Can I choose my seat?":"Yes, you can often choose your seat during the booking process or at check-in, subject to availability.",
"What if I need special assistance?":"Notify the airline in advance or inform staff at the airport, and they'll assist you accordingly."
}
# Define a function to handle user requests 
def handle_request(user_input): 
    if user_input.lower() == "exit": 
        return "Goodbye!" 
    for problem, solution in problem_dict.items():
        if user_input.lower() == problem.lower():
            return solution
    return "I'm sorry, I don't know how to help with that problem."

# Main loop to prompt user for input 
while True: 
    user_input = input("What's the problem? Type 'exit' to quit. ") 
    response = handle_request(user_input) 
    print(response)



