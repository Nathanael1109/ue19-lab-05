"""Generate UUIDs using the public UUIDTools API."""

import requests

API_URL = "https://uuidtools.com/api/generate/v1/count/{}"
MAX_UUIDS = 20


def main():
    """Prompt for UUID counts and display the API results."""
    while True:
        try:
            count = int(input("Nombre d'UUID à générer (1-20) : "))
        except ValueError:
            print("Entrée invalide : indiquez un nombre entier.")
            continue

        # Keep each request within the range accepted by this application.
        if not 1 <= count <= MAX_UUIDS:
            print(f"Indiquez un nombre compris entre 1 et {MAX_UUIDS}.")
            continue

        try:
            # A timeout prevents an unavailable API from blocking the program indefinitely.
            response = requests.get(API_URL.format(count), timeout=10)
            response.raise_for_status()
            uuids = response.json()
        except requests.RequestException as error:
            print(f"Impossible de contacter l'API UUIDTools : {error}")
            continue
        except ValueError:
            print("L'API UUIDTools a renvoyé un JSON invalide.")
            continue

        if not isinstance(uuids, list) or not all(isinstance(value, str) for value in uuids):
            print("L'API UUIDTools a renvoyé une réponse inattendue.")
            continue

        print("UUID générés :\n" + "\n".join(uuids[:count]))
        print()

        if input("En générer d'autres ? (o/n) : ").strip().lower() != "o":
            break


if __name__ == "__main__":
    main()
