project = "Textstat"

master_doc = 'index'

extensions = ['releases']

releases_github_path = 'shivam5992/textstat'
releases_unstable_prehistory = True

html_theme = 'alabaster'

templates_path = [
    '_templates',
]

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'contribute.html',
    ]
}

html_theme_options = {
    'logo': 'textstat.png',
    'logo_name': True,
    'logo_text_align': 'center',
    'github_user': 'shivam5992',
    'github_repo': 'textstat',
    'github_type': 'star',
    'description': 'Calculate statistics from text',
}
