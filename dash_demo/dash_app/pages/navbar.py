import dash_bootstrap_components as dbc

navigation = \
    dbc.NavbarSimple(
        children = \
            [
                dbc.NavItem(
                    dbc.NavLink(
                        "Home",
                        href="/",
                        external_link=True
                    )
                ),
                dbc.NavItem(
                    dbc.NavLink(
                        "Graph Demo",
                        href="/graph_demos",
                        external_link=True
                    )
                ),
                dbc.NavItem(
                    dbc.NavLink(
                        "About",
                        href="/about",
                        external_link=True
                    )
                ),
                dbc.NavItem(
                    dbc.NavLink(
                        "Contact",
                        href="/contact",
                        external_link=True
                    )
                )
            ],
        id='Menu',
        brand="Dash Demo",
        brand_href="#",
        color="primary",
        dark=True
    )