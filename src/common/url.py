def get_url_parametrized(get_url, module, params = None):
    return f"{get_url}{module}{params or ''}"