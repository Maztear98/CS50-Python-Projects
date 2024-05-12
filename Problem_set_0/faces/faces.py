# convert emoticons in the text into emoji

def main():
    text = input("Enter your text here: ")
    print(convert(str(text)))



def convert(emoji):
    emoji = emoji.replace(":)","🙂")
    emoji = emoji.replace(":(","🙁")

    return (emoji)

main()

