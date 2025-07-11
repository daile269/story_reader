def api_response(code=200, message="Thành công", result=None):
    return {
        "code": code,
        "message": message,
        "result": result
    }