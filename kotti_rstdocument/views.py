import colander
from kotti.views.edit import NodeSchema
from kotti.views.edit import generic_edit
from kotti.views.edit import generic_add
from kotti.views.view import view_node
from kotti.views.util import ensure_view_selector
from kotti.views.util import TemplateAPI
from deform.widget import TextAreaWidget

from docutils.core import publish_parts

from kotti_rstdocument.resources import RstDocument

class RstDocumentSchema(NodeSchema):
    body = colander.SchemaNode(
        colander.String(),
        widget=TextAreaWidget(cols=80, rows=40),
        missing=u"",
        )

@ensure_view_selector
def edit_rstdocument(context, request):
    return generic_edit(context, request, RstDocumentSchema())

def add_rstdocument(context, request):
    return generic_add(context, request, RstDocumentSchema(), RstDocument, u'rstdocument')

def view_rstdocument(context, request):
    # TODO:
    # look into http://www.arnebrodowski.de/blog/write-your-own-restructuredtext-writer.html

    overrides = {'file_insertion_enabled': False,
                 'raw_enabled': False,
                 'initial_header_level': 3,
                 'doctitle_xform': False}
    parts = publish_parts(context.body, writer_name='html4css1', settings_overrides=overrides)
    content_html = parts['html_body']

    return {
        'api': TemplateAPI(context, request),
        'html': content_html,
        }

def includeme_edit(config):
    config.add_view(
        edit_rstdocument,
        context=RstDocument,
        name='edit',
        permission='edit',
        renderer='kotti:templates/edit/node.pt',
        )

    config.add_view(
        add_rstdocument,
        name=RstDocument.type_info.add_view,
        permission='add',
        renderer='kotti:templates/edit/node.pt',
        )

def includeme_view(config):
    config.add_view(
        view_rstdocument,
        context=RstDocument,
        name='view',
        permission='view',
        renderer='templates/rstdocument-view.pt',
        )

    config.add_static_view('static-kotti_rstdocument', 'kotti_rstdocument:static')

def includeme(config):
    includeme_edit(config)
    includeme_view(config)
