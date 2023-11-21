from aiohttp import web
import pathlib

html = pathlib.Path(__file__).parent.joinpath('index.html').read_text(encoding='utf-8')


async def handle(request: web.Request):
    real_url = str(request.url.with_host('bgm.tv').with_port(None))
    # raise web.HTTPFound(str(real_url))

    return web.Response(body=html.format(real_url), headers={
        'content-type': 'html'
    })


app = web.Application()
app.add_routes([
    web.get('/{tail:.*}', handle),
])

if __name__ == '__main__':
    web.run_app(app)
