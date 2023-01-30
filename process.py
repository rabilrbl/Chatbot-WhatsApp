import requests


class Message:
    def __init__(self, access_token: str, phone_number_id: str):
        self.url = f"https://graph.facebook.com/v15.0/{phone_number_id}/messages"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    def req(self, method: str = "POST", **kwargs):
        res = requests.request(method, self.url, headers=self.headers, **kwargs)
        res.raise_for_status()
        return res.json()

    def send_message(self, phone_number: str, message: str):
        res = self.req(
            json={
                "messaging_product": "whatsapp",
                "to": phone_number,
                "type": "text",
                "text": {"preview_url": False, "body": message},
            },
        )

    def send_image_url(self, phone_number: str, image_url: str):
        res = self.req(
            json={
                "messaging_product": "whatsapp",
                "to": phone_number,
                "type": "image",
                "image": {"link": image_url},
            },
        )

    def send_message_to_all(self, message):
        res = self.req(
            json={
                "messaging_product": "whatsapp",
                "to": "all",
                "type": "text",
                "text": {"preview_url": False, "body": message},
            },
        )
