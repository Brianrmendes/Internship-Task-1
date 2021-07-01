from plyer import notification
import time

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10,
    )


if __name__ == '__main__':
    while True:
        notifyMe("Hello", "Drink Water")
        time.sleep(30)
