from flask import Flask, Response, request, send_file
from json import dumps
import os
import sys

app = Flask(__name__)
MOCK_PAGES = 10
PAGE_WIDTHS = ['100', '150', '300', '500', '600', '800',
               '1000', '1200', '1600', '1800', '2000']
(DONE, NOT_SUPPORTED, PASSWORD_PROTECTED, FAILED, ERROR) = (
    "DONE", "NOT_SUPPORTED", "PASSWORD_PROTECTED", "FAILED", "ERROR"
)


@app.route('/', methods=['GET'])
def main():
    return Response("OK")


@app.route('/info/<token>', methods=['GET'])
def preview_info(token):
    callback = request.args.get('callback', None)
    if token.upper() in (NOT_SUPPORTED, PASSWORD_PROTECTED, FAILED, ERROR):
        res_data = {
            "status": str(token.upper()),
        }
    else:
        res_data = {
            "status": DONE,
            "pages": MOCK_PAGES,
            "sizes": [[600, 848]] * MOCK_PAGES,
        }
    return json_response(res_data, callback)


@app.route('/preview/<token>', methods=['GET'])
def serve_previews(token):
    mime = 'image/jpeg'
    width = request.args.get('w', '100')
    if width not in PAGE_WIDTHS:
        width = '800'

    res = send_file(
        'images/{}.jpg'.format(width),
        mimetype=mime,
        cache_timeout=60*60*24*365,
        add_etags=False)
    return res


def json_response(data, callback):
    if callback:
        res = "{}({})".format(callback, data)
        return Response(res, content_type="application/json")
    else:
        headers = {
            "Access-Control-Allow-Origin": "*"
        }
        return Response(dumps(data), content_type="application/json",
                        headers=headers)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            num_pages = int(sys.argv[1])
            MOCK_PAGES = num_pages
            print "Number of pages set to {}".format(MOCK_PAGES)
        except ValueError:
            print ("Number of pages parameter must be an "
                   "integer\nDefaulting to {}".format(MOCK_PAGES))
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8500)))
