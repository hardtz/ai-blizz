# Libraries
import wolframalpha
import wikipedia
import wx

# Variables
app_id = "TT25E4-P949A9E2RG"
app = wx.App()
frm = wx.Frame(None, title="blizz")

# Infinite loop
while True:
    # Question window
    question = wx.TextEntryDialog(frm, 'May I help you?','blizz')
    # Setting question default value
    question.SetValue("")
    if question.ShowModal() == wx.ID_OK:
        print('You searched: %s\n' % question.GetValue())

    try:
        client = wolframalpha.Client(app_id)
        res = client.query(question.GetValue())

        # Show Wolframalpha result.
        wx.SafeShowMessage('Results', next(res.results).text)

    except:
        # Print Wikipedia summary result.
        wx.SafeShowMessage('Results', wikipedia.summary(question.GetValue()))

    question.Destroy()
