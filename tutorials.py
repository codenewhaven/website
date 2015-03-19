import os
import markdown
import md5
import collections

# def flatten(x):
#     if isinstance(x, collections.Iterable):
#         return [a for i in x for a in flatten(i)]
#     else:
#         return [x]

class Tutorial:

    def __init__(self, path_to_tutorial):

        self.directory = None
        self.slug = None
        self.tags = []
        self.title = None
        self.category = None
        self.markdown = None
        self.html = None
        self.subdirs = []
        self.subdir_info = {}

        self.parse(path_to_tutorial)

    def parse(self, path_to_tutorial):

        if os.path.exists(path_to_tutorial):
            self.directory = path_to_tutorial
            self.slug = os.path.basename(os.path.normpath(path_to_tutorial))
        else:
            raise KeyError("No tutorial at %s" % path_to_tutorial)

        self.parse_metadata()
        self.parse_tutorial()
        self.parse_subdirs()

    def parse_metadata(self):
        metadata_path = os.path.join(self.directory, self.slug + '.metadata')
        if not os.path.exists(metadata_path):
            raise KeyError("Could not find %s" % metadata_path)

        with open(metadata_path, mode='r') as fh:
            metadata_lines = fh.readlines()

        for line in metadata_lines:
            key, sep, val = line.partition('=')

            self.set_metadata(key, val)

    def parse_tutorial(self):
        tutorial_path = os.path.join(self.directory, self.slug + '.md')
        if not os.path.exists(tutorial_path):
            raise KeyError("Could not find %s" % tutorial_path)

        with open(tutorial_path, mode='r') as fh:
            self.markdown = fh.read()
            self.html = markdown.markdown(self.markdown)

    def parse_subdirs(self):
        for fn in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory, fn)):
                self.parse_subdir(fn)

    def parse_subdir(self, subdir):
        self.subdirs.append(subdir)
        fullpath = os.path.join(self.directory, subdir)

        def make_tree(path):
            name = os.path.basename(path)
            fullpath = os.path.join(path,name)
            tree = dict(name=name, fullpath=fullpath, file_id=md5.md5(fullpath).hexdigest(),children=[], dir_children=[], file_children=[])
            try: lst = os.listdir(path)
            except OSError:
                pass #ignore errors
            else:
                for name in lst:
                    fn = os.path.join(path, name)
                    if os.path.isdir(fn):
                        tree['dir_children'].append(make_tree(fn))
                    else:
                        fullpath = os.path.join(path,name)
                        tree['file_children'].append(dict(name=name,
                                                     fullpath=fullpath,
                                                     file_id=md5.md5(fullpath).hexdigest()))

            tree['children'] = tree['dir_children'] + tree['file_children']
            return tree

        self.subdir_info[subdir] = {
            'fullpath': fullpath,
            'tree': make_tree(fullpath)
        }

    def find_file_by_id(self, subdir, file_id):
        try:
            tree = self.subdir_info[subdir]['tree']
            path = self.subdir_info[subdir]['fullpath']
        except KeyError:
            print 'Cannot find tree for subdir %s' % subdir


        def find_recurse(children):
            for child in children:
                if child['file_id'] == file_id:
                    return child['fullpath']
                elif 'children' in child.keys() and len(child['children']) > 0:
                    find_recurse(child['children'])


        print 'children'
        return find_recurse(tree['children'])
        # from pprint import pprint
        # pprint(tree['children'])

        # return find_recurse(tree['children'])


        # def find_recurse(children):

        #     print 'CHILDREN'
        #     from pprint import pprint
        #     pprint(children)

        #     for child in children:
        #         if child['file_id'] == file_id:
        #             return child.fullpath
        #         if 'children' in child.keys():
        #             return find_recurse(child['fullpath'])
        #         else:
        #             return 'foundnone'

        # return find_recurse(tree['children'])

    def set_metadata(self, key, val):

        key = key.lower()

        if key == 'tags':
            self.tags = val.split()
        elif key == 'category':
            self.category = val
        elif key == 'title':
            self.title = val


def all_tutorials(tutorials_path):
    if not os.path.exists(tutorials_path):
        raise KeyError('Could not find tutorials_path %s' % tutorials_path)

    tutorials = []
    for fn in os.listdir(tutorials_path):
        fullpath = os.path.join(tutorials_path, fn)
        if os.path.isdir(fullpath):
            tutorials.append(Tutorial(fullpath))

    return tutorials
