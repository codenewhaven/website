import os
import markdown

class Tutorial:

    def __init__(self, path_to_tutorial):

        directory = None
        slug      = None
        tags      = []
        demos     = []
        title     = None
        category  = None
        markdown  = None
        html      = None

        self.parse(path_to_tutorial)

    def parse(self, path_to_tutorial):

        if os.path.exists(path_to_tutorial):
            self.directory = path_to_tutorial
            self.slug = os.path.basename(os.path.normpath(path_to_tutorial))
        else:
            raise KeyError("No tutorial at %s" % path_to_tutorial)

        self.parse_metadata()
        self.parse_tutorial()
        self.parse_demos()

    def parse_metadata(self):
        metadata_path = os.path.join(self.directory, self.slug + '.metadata')
        if not os.path.exists(metadata_path):
            raise KeyError("Could not find %s" % metadata_path)

        with open(metadata_path, mode='r') as fh:
            metadata_lines = fh.readlines()

        for line in metadata_lines:
            key, sep, val = line.partition('=')

            # TODO put this into a dictionary

            key = key.lower()

            if key == 'tags':
                self.tags = val.split()
            elif key == 'category':
                self.category = val
            elif key == 'title':
                self.title = val

    def parse_tutorial(self):
        tutorial_path = os.path.join(self.directory, self.slug + '.md')
        if not os.path.exists(tutorial_path):
            raise KeyError("Could not find %s" % tutorial_path)

        with open(tutorial_path, mode='r') as fh:
            self.markdown = fh.read()
            self.html = markdown.markdown(self.markdown)

    def parse_demos(self):
        pass

path = 'tutorials/javascript'
tut = Tutorial(path)

print 'Tutorial parsed.'
print 'Tags: ',
print tut.tags

print 'Category: ' + tut.category
print 'Title: ' + tut.title
