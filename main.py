"""

WARNING: IF YOU DON'T CREATE A WOLFRAMALPHA ACCOUNT, AND EITHER DON'T ENTER YOUR APP_ID, THE APPLICATION
WILL ONLY SEARCH ON WIKIPEDIA FOR RESULTS.

"""

# Libraries
import wolframalpha
import wikipedia
import wx

# Variables
app_id = "YOUR_APP_ID"
app = wx.App()
frm = wx.Frame()

# Infinite loop
while True:
    # Question window
    question = wx.TextEntryDialog(frm, 'How can I help you?', 'blizz')

    # Search if "Ok" was selected
    if question.ShowModal() == wx.ID_OK:
        print('You searched: %s\n' % question.GetValue())

        # WolframAlpha is the first search option, in case the user wants to solve an equation
        try:
            # WolframAlpha client using your app_id
            client = wolframalpha.Client(app_id)

            # Saves input query to be used as a parameter later
            res = client.query(question.GetValue())

            # Show WolframAlpha result
            wx.MessageBox(next(res.results).text, 'Results')

        # If WolframAlpha doesn't show any results, it will search on Wikipedia's summary
        except:
            # Print Wikipedia summary result
            wx.MessageBox(wikipedia.summary(question.GetValue()), 'Results')

    # Stops and close the application by clicking "Cancel" or X button
    else:
        break

    question.Destroy()

