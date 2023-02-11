import datetime

def make_screenshot(the_driver):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    the_driver.get_screenshot_as_file(screenshot)