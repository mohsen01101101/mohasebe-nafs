from fasthtml.common import fast_app, serve


app, rt = fast_app(
    pico=False,
    static_path="static"
)


serve()
