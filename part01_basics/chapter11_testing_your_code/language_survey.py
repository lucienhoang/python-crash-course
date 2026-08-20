from survey import AnonymousSurvey

# Define a qusetion, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == "q":
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()


# What language did you first learn to speak?
# Enter 'q' at any time to quit.

# Language: EngLish
# Language: Spanish
# Language: English
# Language: Vietnamese
# Language: Thailand
# Language: q

# Thank you to everyone who participated in the survey!
# Survey result:
# - EngLish
# - Spanish
# - English
# - Vietnamese
# - Thailand
