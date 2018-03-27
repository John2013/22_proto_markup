from staticjinja import make_site


if __name__ == "__main__":
    # site = make_site()
    index = make_site(contexts=[('index.html', {})])
    requests = make_site(contexts=[('requests.html', {'show_header_logo': True})])

    index.render()
    requests.render()
