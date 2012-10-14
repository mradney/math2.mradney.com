# -*- coding: utf-8 -*-
#: settings for liquidluck

#: site information
#: all variables can be accessed in template with ``site`` namespace.
#: for instance: {{site.name}}
site = {
    'name': "SBCD Math 2 Int.", # your site name
    'url': "http://math2.mradney.com/",  # your site url
    'prefix': "blog",
}

#: this config defined information of your site
#: 1. where the resources  2. how should the site be generated
config = {
    'source': "content",
    'output': "output",
    'static': "output/static",
    'static_prefix': "/static/",
    'permalink': "{{date.year}}/{{filename}}.html",
    'relative_url': False,
    'perpage': 30,
    'feedcount': 20,
    'timezone': "+06:00",
}

author = {
    'default': "James Adney",
    'vars': {
        # key: value
    }
}

#: active readers
reader = {
    'active': [
        'liquidluck.readers.markdown.MarkdownReader',
        # uncomment to active rst reader.
        # but you need to install docutils by yourself
        #'liquidluck.readers.restructuredtext.RestructuredTextReader',
    ],
    'vars': {
        # key: value
    }
}

#: active writers
writer = {
    'active': [
        'liquidluck.writers.core.PostWriter',
        'liquidluck.writers.core.PageWriter',
        'liquidluck.writers.core.ArchiveWriter',
        'liquidluck.writers.core.ArchiveFeedWriter',
        'liquidluck.writers.core.FileWriter',
        'liquidluck.writers.core.StaticWriter',
        'liquidluck.writers.core.YearWriter',
        'liquidluck.writers.core.CategoryWriter',
        #'liquidluck.writers.core.CategoryFeedWriter',
        'liquidluck.writers.core.TagWriter',
        'liquidluck.writers.core.TagCloudWriter',
    ],
    'vars': {
        # uncomment if you want to reset archive page
        # 'archive_output': 'archive.html',
    }
}

#: theme variables
theme = {
    'name': 'default',

    # theme variables are defined by theme creator
    # you can access theme in template with ``theme`` namespace
    # for instance: {{theme.disqus}}
    'vars': {
        'disqus': "mradney",
        'analytics': "UA-35532935-1",
        'navigation': [ 
            {'name': "Blog", 'link': "/blog/"},
            {'name': "Files", 'link': "/pages/files.html"},
            {'name': "Resources", 'link': "/pages/resources.html"},
            {'name': "Schedule", 'link': "/pages/schedule.html"},
            {'name': "[topics]", 'link': "/blog/tag/"},
        ],
    }
}

#: template variables
template = {
    'vars': {
        # key: value
    },
    'filters': {
        # key: value
    }
}
