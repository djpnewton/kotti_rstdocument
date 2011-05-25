from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import UnicodeText
from sqlalchemy import String
from sqlalchemy.orm import mapper
from kotti import metadata
from kotti.resources import Node

class RstDocument(Node):
    type_info = Node.type_info.copy(
        name=u'Restructured Text Document',
        add_view=u'add_rstdocument',
        addable_to=[u'Document'],
        )

    def __init__(self, body=u"", mime_type="text/html", **kwargs):
        super(RstDocument, self).__init__(**kwargs)
        self.body = body
        self.mime_type = mime_type

rstDocuments = Table('rstDocuments', metadata,
    Column('id', Integer, ForeignKey('nodes.id'), primary_key=True),
    Column('body', UnicodeText()),
    Column('mime_type', String(30)),
)

mapper(RstDocument, rstDocuments, inherits=Node, polymorphic_identity='rstDocument')
