from fasthtml.common import *
from fasthtml.svg import *
from app.web.layouts.base import auth_layout


def login(req: Request):
    page_content = Section(
        Form(
            Label(
                Span(
                    "شماره همراه",
                    cls="label"
                ),

                Input(
                    name="phone_number",
                    type="tel",
                    required=True,
                    placeholder="شماره همراه",
                    pattern="[0-9]*",
                    minlength="11",
                    maxlength="11",
                    title="Phone number must be 11 digits",
                    cls="input validator tabular-nums",
                    dir="rtl"
                ),

                Span(
                    "شماره همراه باید ۱۱ رقم باشد",
                    cls="validator-hint hidden"
                ),

                cls="fieldset"
            ),

            Label(
                Span(
                    "رمز عبور",
                    cls="label"
                ),

                Input(
                    name="password",
                    type="password",
                    required=True,
                    placeholder="رمز عبور",
                    minlength="8",
                    cls="input validator"
                ),

                Span(
                    "رمز عبور باید حداقل 8 کاراکتر باشد",
                    cls="validator-hint hidden"
                ),

                cls="fieldset"
            ),

            Button(
                "ورود",
                type="submit",
                cls="btn btn-primary mt-4"
            ),

            action="/login",
            method="post",
            cls="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4"
        ),

        cls="flex justify-self-center items-center h-dvh"
    )

    return auth_layout(
        req=req,
        page_content=page_content,
        title="صفحه ورود"
    )
