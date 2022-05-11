google_calendar_api = {
    "client_secret_file": "data_engineering_support_rota_creds.json",
    "api_name": "calendar",
    "api_version": "v3",
    "scopes": ["https://www.googleapis.com/auth/calendar"],
    "calendar_ids": {
        "dev": "qk7dfadvnmao3lgvb207pqd1bk@group.calendar.google.com",
        "prod": "9c720gjf06r8odu2vhsfvd7e9k@group.calendar.google.com",
    },
    "calendar": "prod",
}

support_team = {
    "start_cycle_with": "g_sevens",
    "g_sevens": [
        "Kimberley",
        "Priya",
        "Francesca",
        "Soumaya",
        "Stephen",
        "Tapan",
        "Gwion",
        "Alec",
    ],
    "everyone_else": [
        "Thomas",
        "Jacob",
        "Darius",
        "Anthony",
        "Danjiv",
        "Lora",
        "Matt",
        "Tamsin",
        "Mike",
        "Ant",
        "Tom",
    ],
}

date_range = {
    "start_date": "2022-05-16",
    "n_cycles": 5,
}
