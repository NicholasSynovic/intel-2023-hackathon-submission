from pathlib import Path

pageState = {
    "page_title": "Empire General Hospital Patient Portal",
    "initial_sidebar_state": "collapsed",
}

hideSidebarCSS = {
    "body": """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    "unsafe_allow_html": True,
}
dbPath: Path = Path("storage/data.db")
