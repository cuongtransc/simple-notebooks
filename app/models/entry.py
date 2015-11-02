# -*- coding: utf-8 -*-
"""
Created on 2015-11-01 21:28:00

@author: Tran Huu Cuong <tranhuucuong91@gmail.com>

"""
import re
import datetime

from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from peewee import *
from micawber import parse_html
from flask import Markup

from app import app
from app import flask_db
from app import oembed_providers
from app import es

class Entry(flask_db.Model):
    title = CharField()
    slug = CharField(unique=True)
    content = TextField()
    published = BooleanField(index=True)
    timestamp = DateTimeField(default=datetime.datetime.utcnow, index=True)

    @property
    def html_content(self):
        """
        Generate HTML representation of the markdown-formatted blog entry,
        and also convert any media URLs into rich media objects such as video
        players or images.
        """
        hilite = CodeHiliteExtension(linenums=False, css_class='highlight')
        extras = ExtraExtension()
        markdown_content = markdown(self.content, extensions=[hilite, extras])

        oembed_content = parse_html(
            markdown_content,
            oembed_providers,
            urlize_all=True,
            maxwidth=app.config['SITE_WIDTH']
        )
        return Markup(oembed_content)

    def save(self, *args, **kwargs):
        # Generate a URL-friendly representation of the entry's title.
        if not self.slug:
            self.slug = re.sub('[^\w]+', '-', self.title.lower()).strip('-')
        ret = super(Entry, self).save(*args, **kwargs)

        # Store search content.
        if app.config.get('IS_ES_INDEX'):
            self.update_search_index()

        return ret

    def update_search_index(self):
        es.index(index=app.config.get('ES_INDEX_NAME'),
                 doc_type=app.config.get('ES_TYPE_NAME'),
                 id=self.id, body={
                'title': self.title,
                'content': self.content
            }
                 )
        app.logger.info('[ES] Index post {}: {}'.format(self.id, self.title))

    @classmethod
    def public(cls):
        return Entry.select().where(Entry.published == True)

    @classmethod
    def drafts(cls):
        return Entry.select().where(Entry.published == False)
