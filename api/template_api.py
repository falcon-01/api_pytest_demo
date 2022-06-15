
class TemplateAPI:

    def api_add(self, session, url, headers, body):
        return session.post(url, headers=headers, json=body)

    def api_update(self, session, url, headers, body):
        return session.put(url, headers=headers, json=body)

    def api_get(self, session, url, headers, params):
        return session.get(url, headers=headers, params=params)

    def api_delete(self, session, url, headers, uid):
        return session.delete(url.format(id=uid), headers=headers)
