# Multiple print statements to format a message
def banner_text(text=" ", screen_width=80):
    # screen_width = 50
    if len(text) > screen_width - 4:
        # raise is akin to 'throw new exception'
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))
        # print("EEK!\nThe text is too long to fit in the specified width".upper())

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{}**".format(centered_text)
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bridge side of life...", 60)
banner_text("Jolly rotten you are", 60)
banner_text("There's something you've forgotten!", 60)
banner_text(screen_width=60)
banner_text("HAHA HAHA!", 60)
banner_text("phony you are when this prints", 60)
banner_text("*", 60)
