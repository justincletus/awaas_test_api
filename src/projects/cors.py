class CorsMiddleware(object):
    def process_response(self, req, resp):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS,DELETE,PUT"
        return response
