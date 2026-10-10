class Notification:
    def send_alert(self, message, user=None):
        if user:
            print(f"Alert for {user}: {message}")
        else:
            print(f"General Alert: {message}")

n = Notification()
n.send_alert("System will restart soon.")
n.send_alert("Your password has been changed.", "Zayan")
