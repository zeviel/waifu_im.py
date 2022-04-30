import requests


class WaifuClient:
    def __init__(self, token: str):
        self.api = "https://api.waifu.im"
        self.website = "https://waifu.im"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36",
            "Content-Type": "application/json",
            "Connection": "keep-alive"}
        if token:
            self.login_with_token(token)

    def login_with_token(self, token: str):
        self.token = token
        self.headers["Authorization"] = f"Bearer {self.token}"
        return self.token

    def get_tags_list(self, full: bool = False):
        return requests.get(
            f"{self.api}/tags?full={full}",
            headers=self.headers).json()

    def get_random_image(
            self,
            selected_tags: str = None,
            excluded_tags: str = None,
            is_nsfw: bool = False,
            is_gif: bool = False,
            orientation: str = "LANDSCAPE",
            is_many: bool = False):
        url = f"{self.api}/random?is_nsfw={is_nsfw}"
        if selected_tags:
            url += f"&selected_tags={selected_tags}"
        if excluded_tags:
            url += f"&excluded_tags={excluded_tags}"
        if is_gif:
            url += f"&gif={is_gif}"
        if orientation:
            url += f"&orientation={orientation}"
        if is_many:
            url += f"&many={is_many}"
        return requests.get(url, headers=self.headers).json()

    def report_image(self, image: str, description: str, user_id: int = None):
        url = f"{self.api}/report?image={image}&description={description}"
        if user_id:
            url += f"&user_id={user_id}"
        return requests.get(url, headers=self.headers).status_code

    # permissions: 1 - view_favourites, 2 - manage_favourites
    def generate_authorization_link(self, user_id: int, permissions: str):
        return requests.get(
            f"{self.website}/authorization",
            headers=self.headers).json()

    def get_favourites(
            self,
            user_id: int = None,
            selected_tags: str = None,
            excluded_tags: str = None,
            is_nsfw: bool = False,
            is_gif: bool = False,
            order_by: str = "FAVOURITES",
            orientation: str = "LANDSCAPE",
            is_many: bool = False):
        url = f"{self.api}/fav?is_nsfw={is_nsfw}"
        if user_id:
            url += f"&user_id={user_id}"
        if selected_tags:
            url += f"&selected_tags={selected_tags}"
        if excluded_tags:
            url += f"&excluded_tags={excluded_tags}"
        if is_gif:
            url += f"&gif={is_gif}"
        if order_by:
            url += f"&order_by={order_by}"
        if orientation:
            url += f"&orientation={orientation}"
        if is_many:
            url += f"&many={is_many}"
        return requests.get(url, headers=self.headers).json()

    def insert_favourite(self, image: str, user_id: str = None):
        url = f"{self.api}/fav/insert?image={image}"
        if user_id:
            url += f"&user_id={user_id}"
        return requests.post(url, headers=self.headers).status_code

    def delete_favourite(self, image: str, user_id: str = None):
        url = f"{self.api}/fav/delete?image={image}"
        if user_id:
            url += f"&user_id={user_id}"
        return requests.delete(url, headers=self.headers).status_code

    def toggle_favourite(self, image: str, user_id: str = None):
        url = f"{self.api}/fav/toggle?image={image}"
        if user_id:
            url += f"&user_id={user_id}"
        return requests.post(url, headers=self.headers).status_code

    def get_image_info(self, image: str):
        return requests.get(
            f"{self.api}/info?image={image}",
            headers=self.headers).json()
