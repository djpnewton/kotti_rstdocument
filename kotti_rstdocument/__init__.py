def kotti_configure(settings):
    settings['kotti.includes'] += ' kotti_rstdocument.views'
    settings['kotti.available_types'] += ' kotti_rstdocument.resources.RstDocument'
