# Libraries
import wolframalpha
import wikipedia

# Variables
app_id = "TT25E4-P949A9E2RG"

# Infinite loop
while True:
    question = input("May I help you? ")

    try:
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text

        # Print Wolframalpha result.
        print(answer)

    except:
        # Print Wikipedia summary result.
        print(wikipedia.summary(question))
