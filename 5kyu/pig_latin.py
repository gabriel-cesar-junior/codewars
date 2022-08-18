#https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):

    text = text.split(" ")
    abcd = ""
    for t in text:
        ui = ""
        if t.isalpha():
            for i in range(1,len(t)):
                ui += t[i]
            ui += (text[0] + 'ay')
            abcd += (ui + " ")
        else:
            print('not alpha')
            ui += (t)
            abcd += ui
    return abcd.strip()
print(pig_it('Pig latin is cool'))