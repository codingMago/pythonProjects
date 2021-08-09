class engineLogic:

    def scrollingText(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)