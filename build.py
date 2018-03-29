from staticjinja import make_site


if __name__ == "__main__":
    # site = make_site()
    index = make_site(contexts=[('index.html', {})])
    requests = make_site(contexts=[('requests.html', {
        'show_header_logo': True,
        'pages': [
            {'number': 1, 'link': 'javascript:void(0)', 'is_active': True},
            {'number': 2, 'link': 'javascript:void(0)'},
            {'number': 3, 'link': 'javascript:void(0)'},
            {'number': '...', 'link': 'javascript:void(0)'},
            {'number': 10, 'link': 'javascript:void(0)'},
        ],
        'first_page_link': 'javascript:void(0)',
        'last_page_link': 'javascript:void(0)',
        'first_page': True
    })])

    index.render()
    requests.render()
