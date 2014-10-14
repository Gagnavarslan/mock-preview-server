from flask import Flask, Response, request, send_file

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return Response("OK")


@app.route('/info/<token>', methods=['GET'])
def preview_info(token):
    callback = request.args.get('callback', None)
    res_data = {
        "status": "DONE",
        "pages": 10,
        "sizes": [
            [595, 841],
            [595, 841],
            [595, 841],
            [595, 841],
            [595, 841],
            [595, 841],
            [595, 841],
            [595, 841],
            [595, 841],
            [595, 841]
            ]
        }
    return json_response(res_data, callback)


@app.route('/preview/<token>', methods=['GET'])
def serve_previews(token):
    mime = 'image/jpeg'
    width = request.args.get('w', '100')
    if width not in ['100', '600']:
        width = '600'

    res = send_file(
        '{}.jpg'.format(width),
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
        return Response(data, content_type="application/json", headers=headers)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8500)
