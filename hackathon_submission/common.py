from pathlib import Path

SITE_STATE = {
    "page_title": "Empire General Hospital Patient Portal",
    "initial_sidebar_state": "collapsed",
    "layout": "wide",
}

HIDDEN_SIDEBAR_CSS = {
    "body": """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    "unsafe_allow_html": True,
}

DB_PATH: Path = Path("storage/data.db")

MODEL_PATH: Path = Path("model")

PAGE_HEADER: str = """# Empire General Hospital Patient Self-Diagnosis Tool
> A prototype developed by Nicholas M. Synovic ([nsynovic@luc.edu](mailto:nsynovic@luc.edu))"""

PAGE_FOOTER: str = """To speak to a medical professional at Empire General Hospital, call `(xxx) xxx-xxxx`\n
For all medical emergencies, call `911`"""
