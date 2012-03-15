from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import UnicodeText
from sqlalchemy import String
from kotti.resources import Content

class RstDocument(Content):
    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)
    body = Column(UnicodeText())
    mime_type = Column('mime_type', String(30))

    type_info = Content.type_info.copy(
        name=u'Restructured Text Document',
        title=u'Restructured Text Document',
        add_view=u'add_rstdocument',
        addable_to=[u'Document'],
        )

    def __init__(self, body=u"", mime_type="text/html", **kwargs):
        super(RstDocument, self).__init__(**kwargs)
        self.body = body
        self.mime_type = mime_type
