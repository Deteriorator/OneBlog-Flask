# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class WpCommentmeta(db.Model):
    __tablename__ = 'wp_commentmeta'

    meta_id = db.Column(db.BigInteger, primary_key=True)
    comment_id = db.Column(db.BigInteger, nullable=False, index=True,
                           server_default=db.FetchedValue())
    meta_key = db.Column(db.String(255, 'utf8mb4_unicode_ci'), index=True)
    meta_value = db.Column(db.String(collation='utf8mb4_unicode_ci'))


class WpComment(db.Model):
    __tablename__ = 'wp_comments'
    __table_args__ = (
        db.Index('comment_approved_date_gmt', 'comment_approved', 'comment_date_gmt'),
    )

    comment_ID = db.Column(db.BigInteger, primary_key=True)
    comment_post_ID = db.Column(db.BigInteger, nullable=False, index=True,
                                server_default=db.FetchedValue())
    comment_author = db.Column(db.String(collation='utf8mb4_unicode_ci'), nullable=False)
    comment_author_email = db.Column(db.String(100, 'utf8mb4_unicode_ci'), nullable=False,
                                     index=True, server_default=db.FetchedValue())
    comment_author_url = db.Column(db.String(200, 'utf8mb4_unicode_ci'), nullable=False,
                                   server_default=db.FetchedValue())
    comment_author_IP = db.Column(db.String(100, 'utf8mb4_unicode_ci'), nullable=False,
                                  server_default=db.FetchedValue())
    comment_date = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    comment_date_gmt = db.Column(db.DateTime, nullable=False, index=True,
                                 server_default=db.FetchedValue())
    comment_content = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=False)
    comment_karma = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    comment_approved = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False,
                                 server_default=db.FetchedValue())
    comment_agent = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False,
                              server_default=db.FetchedValue())
    comment_type = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False,
                             server_default=db.FetchedValue())
    comment_parent = db.Column(db.BigInteger, nullable=False, index=True,
                               server_default=db.FetchedValue())
    user_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    comment_mail_notify = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class WpLink(db.Model):
    __tablename__ = 'wp_links'

    link_id = db.Column(db.BigInteger, primary_key=True)
    link_url = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False,
                         server_default=db.FetchedValue())
    link_name = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False,
                          server_default=db.FetchedValue())
    link_image = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False,
                           server_default=db.FetchedValue())
    link_target = db.Column(db.String(25, 'utf8mb4_unicode_ci'), nullable=False,
                            server_default=db.FetchedValue())
    link_description = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False,
                                 server_default=db.FetchedValue())
    link_visible = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False, index=True,
                             server_default=db.FetchedValue())
    link_owner = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    link_rating = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    link_updated = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    link_rel = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False,
                         server_default=db.FetchedValue())
    link_notes = db.Column(db.String(collation='utf8mb4_unicode_ci'), nullable=False)
    link_rss = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False,
                         server_default=db.FetchedValue())


class WpMsSnippet(db.Model):
    __tablename__ = 'wp_ms_snippets'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(collation='utf8mb4_unicode_520_ci'), nullable=False)
    description = db.Column(db.Text(collation='utf8mb4_unicode_520_ci'), nullable=False)
    code = db.Column(db.String(collation='utf8mb4_unicode_520_ci'), nullable=False)
    tags = db.Column(db.String(collation='utf8mb4_unicode_520_ci'), nullable=False)
    scope = db.Column(db.String(15, 'utf8mb4_unicode_520_ci'), nullable=False,
                      server_default=db.FetchedValue())
    priority = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    active = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    modified = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class WpOption(db.Model):
    __tablename__ = 'wp_options'

    option_id = db.Column(db.BigInteger, primary_key=True)
    option_name = db.Column(db.String(191, 'utf8mb4_unicode_ci'), nullable=False, unique=True,
                            server_default=db.FetchedValue())
    option_value = db.Column(db.String(collation='utf8mb4_unicode_ci'), nullable=False)
    autoload = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False, index=True,
                         server_default=db.FetchedValue())


class WpPostmeta(db.Model):
    __tablename__ = 'wp_postmeta'

    meta_id = db.Column(db.BigInteger, primary_key=True)
    post_id = db.Column(db.BigInteger, nullable=False, index=True,
                        server_default=db.FetchedValue())
    meta_key = db.Column(db.String(255, 'utf8mb4_unicode_ci'), index=True)
    meta_value = db.Column(db.String(collation='utf8mb4_unicode_ci'))


class WpPost(db.Model):
    __tablename__ = 'wp_posts'
    __table_args__ = (
        db.Index('type_status_date', 'post_type', 'post_status', 'post_date', 'ID'),
    )

    ID = db.Column(db.BigInteger, primary_key=True)
    post_author = db.Column(db.BigInteger, nullable=False, index=True,
                            server_default=db.FetchedValue())
    post_date = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    post_date_gmt = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    post_content = db.Column(db.String(collation='utf8mb4_unicode_ci'), nullable=False)
    post_title = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=False)
    post_excerpt = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=False)
    post_status = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False,
                            server_default=db.FetchedValue())
    comment_status = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False,
                               server_default=db.FetchedValue())
    ping_status = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False,
                            server_default=db.FetchedValue())
    post_password = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False,
                              server_default=db.FetchedValue())
    post_name = db.Column(db.String(200, 'utf8mb4_unicode_ci'), nullable=False, index=True,
                          server_default=db.FetchedValue())
    to_ping = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=False)
    pinged = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=False)
    post_modified = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    post_modified_gmt = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    post_content_filtered = db.Column(db.String(collation='utf8mb4_unicode_ci'), nullable=False)
    post_parent = db.Column(db.BigInteger, nullable=False, index=True,
                            server_default=db.FetchedValue())
    guid = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False,
                     server_default=db.FetchedValue())
    menu_order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    post_type = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False,
                          server_default=db.FetchedValue())
    post_mime_type = db.Column(db.String(100, 'utf8mb4_unicode_ci'), nullable=False,
                               server_default=db.FetchedValue())
    comment_count = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())


class WpQ2w3IncManager(db.Model):
    __tablename__ = 'wp_q2w3_inc_manager'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    location = db.Column(db.Integer, nullable=False)
    widget_title = db.Column(db.String(255))
    priority = db.Column(db.Integer)
    inc_pages = db.Column(db.Text, nullable=False)
    exc_pages = db.Column(db.Text)
    hide_from_admin = db.Column(db.Text)
    code_align = db.Column(db.Integer)
    code = db.Column(db.Text, nullable=False)


class WpSnippet(db.Model):
    __tablename__ = 'wp_snippets'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(collation='utf8mb4_unicode_520_ci'), nullable=False)
    description = db.Column(db.Text(collation='utf8mb4_unicode_520_ci'), nullable=False)
    code = db.Column(db.String(collation='utf8mb4_unicode_520_ci'), nullable=False)
    tags = db.Column(db.String(collation='utf8mb4_unicode_520_ci'), nullable=False)
    scope = db.Column(db.String(15, 'utf8mb4_unicode_520_ci'), nullable=False,
                      server_default=db.FetchedValue())
    priority = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    active = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    modified = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class WpTermRelationship(db.Model):
    __tablename__ = 'wp_term_relationships'

    object_id = db.Column(db.BigInteger, primary_key=True, nullable=False,
                          server_default=db.FetchedValue())
    term_taxonomy_id = db.Column(db.BigInteger, primary_key=True, nullable=False, index=True,
                                 server_default=db.FetchedValue())
    term_order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class WpTermTaxonomy(db.Model):
    __tablename__ = 'wp_term_taxonomy'
    __table_args__ = (
        db.Index('term_id_taxonomy', 'term_id', 'taxonomy'),
    )

    term_taxonomy_id = db.Column(db.BigInteger, primary_key=True)
    term_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    taxonomy = db.Column(db.String(32, 'utf8mb4_unicode_ci'), nullable=False, index=True,
                         server_default=db.FetchedValue())
    description = db.Column(db.String(collation='utf8mb4_unicode_ci'), nullable=False)
    parent = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    count = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())


class WpTermmeta(db.Model):
    __tablename__ = 'wp_termmeta'

    meta_id = db.Column(db.BigInteger, primary_key=True)
    term_id = db.Column(db.BigInteger, nullable=False, index=True,
                        server_default=db.FetchedValue())
    meta_key = db.Column(db.String(255, 'utf8mb4_unicode_ci'), index=True)
    meta_value = db.Column(db.String(collation='utf8mb4_unicode_ci'))


class WpTerm(db.Model):
    __tablename__ = 'wp_terms'

    term_id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(200, 'utf8mb4_unicode_ci'), nullable=False, index=True,
                     server_default=db.FetchedValue())
    slug = db.Column(db.String(200, 'utf8mb4_unicode_ci'), nullable=False, index=True,
                     server_default=db.FetchedValue())
    term_group = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())


class WpUsermeta(db.Model):
    __tablename__ = 'wp_usermeta'

    umeta_id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, index=True,
                        server_default=db.FetchedValue())
    meta_key = db.Column(db.String(255, 'utf8mb4_unicode_ci'), index=True)
    meta_value = db.Column(db.String(collation='utf8mb4_unicode_ci'))


class WpUser(db.Model):
    __tablename__ = 'wp_users'

    ID = db.Column(db.BigInteger, primary_key=True)
    user_login = db.Column(db.String(60, 'utf8mb4_unicode_ci'), nullable=False, index=True,
                           server_default=db.FetchedValue())
    user_pass = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False,
                          server_default=db.FetchedValue())
    user_nicename = db.Column(db.String(50, 'utf8mb4_unicode_ci'), nullable=False, index=True,
                              server_default=db.FetchedValue())
    user_email = db.Column(db.String(100, 'utf8mb4_unicode_ci'), nullable=False, index=True,
                           server_default=db.FetchedValue())
    user_url = db.Column(db.String(100, 'utf8mb4_unicode_ci'), nullable=False,
                         server_default=db.FetchedValue())
    user_registered = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    user_activation_key = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False,
                                    server_default=db.FetchedValue())
    user_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    display_name = db.Column(db.String(250, 'utf8mb4_unicode_ci'), nullable=False,
                             server_default=db.FetchedValue())
