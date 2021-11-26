import urllib.parse
import urllib.request
import json
import books_csv
import functions

cert_key = "6efe44b0b9005ffc12d18b193ca79afb3641ecb7f64a1c4145f36ff1656264b8"


def isbn(isbn_number):
    encText = urllib.parse.quote(str(isbn_number))
    url = "http://seoji.nl.go.kr/landingPage/SearchApi.do?cert_key=" + urllib.parse.quote(
        str(cert_key)) + "&result_style=json&page_no=1&page_size=100&isbn=" + encText
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        if not json.loads(response_body.decode())['docs']:
            return "no_isbn"
        print(json.loads(response_body.decode())['docs'][0])
        return functions.change(json.loads(response_body.decode())['docs'][0])
    else:
        print(rescode)
        return "error"


if __name__ == "__main__":
    books_csv.add_to_csv(isbn(9791185553573))