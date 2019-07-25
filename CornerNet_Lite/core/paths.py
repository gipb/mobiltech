import pkg_resources

_package_name = __name__

def get_file_path(*paths):
    path = "/".join(paths)
    if paths[0] == 'mnt':
        return '/'+path
    return pkg_resources.resource_filename(_package_name, path)

