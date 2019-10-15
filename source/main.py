import requests

if __name__ == "__main__":
    # send youtube login request & get response
    login_params = {
        "action_handle_signin": "true",
        "auth": "pQcutQPWHno2I04CzO62FNjNsvuXLeWLnOQnwHyh6_EP3_6u4GbQ4s2KUOW-aKSnch5nrg"
    }
    login_response = requests.get(
        "https://www.youtube.com/signin", params=login_params)
    if (login_response.status_code == 200):
        print(login_response.headers)
        # send youtube search request & get response
        search_params = {
            "search_query": "hello"
        }
        search_response = requests.get(
            "https://www.youtube.com/results", params=search_params)
        if(search_response.status_code == 200):
            with open("search_result.html", "w", encoding="utf-8") as resultFile:
                resultFile.write(search_response.text)
        else:
            print("search: ", search_response.status_code)
    else:
        print("login: ", login_response.status_code)
        print("failed")
